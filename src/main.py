import datetime

from actions import core

from src.wait import wait


async def main():
    """
    The main function for the action.
    """
    try:
        ms = core.get_input("milliseconds", required=True)

        # Debug logs are only output if the `ACTIONS_STEP_DEBUG` secret is true
        core.debug(f"Waiting {ms} milliseconds ...")

        # Log the current timestamp, wait, then log the new timestamp
        core.debug(datetime.datetime.now().isoformat())
        await wait(milliseconds=int(ms))
        core.debug(datetime.datetime.now().isoformat())

        # Set outputs for other workflow steps to use
        core.set_output("time", datetime.datetime.now().isoformat())
    except Exception as e:
        core.set_failed(e)
