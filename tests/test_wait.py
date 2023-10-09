import datetime
import unittest

from src.wait import wait


class TestWait(unittest.IsolatedAsyncioTestCase):
    async def test_raises_an_invalid_integer(self):
        with self.assertRaisesRegex(Exception, "milliseconds not a integer"):
            await wait("foo")  # type: ignore

    async def test_wait_with_a_valid_integer(self):
        start = datetime.datetime.now()
        await wait(500)
        end = datetime.datetime.now()
        delta = end - start
        self.assertGreaterEqual(delta, datetime.timedelta(milliseconds=450))
