import asyncio
import aioredis
import random
import datetime

async def simulador():
    redis = aioredis.from_url("redis://host.docker.internal")
    while True:
        try:
            data = {
                "ID":"1234",
                "temperature": random.randint(10,100),
                "timestamp":str(datetime.datetime.now())
            }
            await redis.xadd("sensor", data)
            await asyncio.sleep(5)
        except Exception as e:
            print(e)

async def main():
    print("Starting simulator...")
    await asyncio.gather(simulador())


if __name__ == "__main__":
    asyncio.run(main())