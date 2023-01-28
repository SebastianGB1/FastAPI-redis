from fastapi import FastAPI
import aioredis
from models.record import Record

app = FastAPI()
redis = aioredis.from_url("redis://host.docker.internal")
#redis = aioredis.from_url("redis://localhost")

@app.get("/sensor/data")
async def get_all_data():
    try:
        data = await redis.xrange("sensor_data", "-", "+")
        return data
    except Exception as e:
        return {"error":str(e)}

@app.post("/sensor/add", response_model = Record)
async def create_record(record:Record):
    try:
        await redis.xadd("sensor_data", record.to_json())
        return record
    except Exception as e:
        return {"error":str(e)}

@app.delete("/sensor/delete/{id}")
async def remove_record(id):
    try:
        rows_modified = await redis.xdel("sensor_data", id)
        return {"rows_modified": rows_modified}
    except Exception as e:
        return {"error":str(e)}


