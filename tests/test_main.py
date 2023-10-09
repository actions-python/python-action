import unittest
from unittest.mock import patch

from src.main import main

TIME_REGEX_PATTERN = r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{5}"


class TestMain(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.patches = {
            "actions.core.debug": patch("actions.core.debug").start(),
            "actions.core.get_input": patch("actions.core.get_input").start(),
            "actions.core.set_failed": patch("actions.core.set_failed").start(),
            "actions.core.set_output": patch("actions.core.set_output").start(),
        }

    async def asyncTearDown(self):
        for patch_func in self.patches.values():
            patch_func.start()

    async def test_sets_the_time_input(self):
        def mock_get_input(name, **options):
            return "500" if name == "milliseconds" else ""

        with patch("actions.core.get_input", side_effect=mock_get_input):
            await main()

        call_args_list = self.patches["actions.core.debug"].call_args_list
        self.assertEqual(call_args_list[0].args[0], "Waiting 500 milliseconds ...")
        self.assertRegex(call_args_list[1].args[0], TIME_REGEX_PATTERN)
        self.assertRegex(call_args_list[2].args[0], TIME_REGEX_PATTERN)

        call_arg = self.patches["actions.core.set_output"].call_args[0]
        self.assertEqual(call_arg[0], "time")
        self.assertRegex(call_arg[1], TIME_REGEX_PATTERN)

    async def test_sets_a_failed_status(self):
        def mock_get_input(name, **options):
            return "this is not a number" if name == "milliseconds" else ""

        with patch("actions.core.get_input", side_effect=mock_get_input):
            await main()

        self.patches["actions.core.set_failed"].assert_called_once()

    async def test_fails_if_no_input_is_provided(self):
        def mock_get_input(name, **options):
            if name == "milliseconds":
                raise Exception("Input required and not supplied: milliseconds")
            return ""

        with patch("actions.core.get_input", side_effect=mock_get_input):
            await main()

        self.patches["actions.core.set_failed"].assert_called_once()
