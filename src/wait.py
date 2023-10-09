import asyncio


async def wait(milliseconds: int) -> str:
    """
    Wait for a number of milliseconds.
    """
    if not isinstance(milliseconds, int):
        raise Exception("milliseconds not a integer")

    await asyncio.sleep(milliseconds / 1_000)
    return "done!"
