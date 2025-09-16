import asyncio
import random


async def retry(func, attempts=3, base=0.2, factor=2.0):
    delay = base
    for i in range(attempts):
        try:
            return await func()
        except Exception as e:
            if i == attempts - 1:
                raise
            await asyncio.sleep(delay + random.random() * 0.1)
            delay *= factor
