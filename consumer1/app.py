import asyncio
import httpx
import aioredis

# redis = aioredis.from_url("redis://localhost") 

async def addEventData(data):
    try:
        async with httpx.AsyncClient() as client:
            url = "http://host.docker.internal:8000/sensor/add"
            res = await client.post(url, data=data)
            print(res)
            if res.status_code == 200:
                return True
            else:
                return False
    except:
        return False

async def get_data(redis_connection):
    last_id = 0
    while True:
        try:
            resp = await redis_connection.xread({"sensor": last_id}, count=1)
            if resp:
                key, message = resp[0]
                last_id, data = message[0]
                data_json = str(data).replace("b'", '"').replace("'", '"')
                response = await addEventData(data_json)
                print(data_json)
                print(response)
                if response:
                    await redis_connection.xdel("sensor", last_id)

        except ConnectionError as e:
            print("ERROR REDIS CONNECTION: {}".format(e))


async def main():
    print("Starting")
    redis = aioredis.from_url("redis://host.docker.internal")
    await asyncio.gather(get_data(redis))

asyncio.run(main())