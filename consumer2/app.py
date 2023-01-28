import asyncio
import json
import aioredis


async def get_data(redis_connection):
    last_id = 0
    while True:
        try:
            resp = await redis_connection.xread(
                {"sensor": last_id}, count=1
            )
            if resp:
                key, message = resp[0]
                last_id, data = message[0]
                data_json = json.loads(
                    str(data).replace("b'", "'").replace("'", '"'))
                temp = int(data_json['temperature'])
                if temp >= 50:
                    print("ALERT TEMPERATURE OUT OF RANGE")
                    await redis_connection.xadd("alerts", data_json)

        except ConnectionError as e:
            print("ERROR REDIS CONNECTION: {}".format(e))


async def main():
    redis = aioredis.from_url("redis://host.docker.internal")  # host.docker.internal
    await asyncio.gather(get_data(redis))

# Iniciar el consumidor
asyncio.run(main())
