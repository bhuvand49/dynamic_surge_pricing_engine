from fastapi import FastAPI
from storage.db_client import DBClient

app = FastAPI()

db = DBClient()


@app.get("/")
def home():
    return {"message": "Dynamic Surge Pricing API Running"}


# 🔹 Get all records
@app.get("/surge/all")
def get_all_surge():
    data = db.get_all_records()
    return {"data": data}


# 🔹 Get by zone
@app.get("/surge/zone/{zone}")
def get_by_zone(zone: str):
    data = db.get_records_by_zone(zone)
    return {"data": data}


# 🔹 Get recent records
@app.get("/surge/recent")
def get_recent():
    data = db.get_recent_records()
    return {"data": data}