from flask import json
from pymongo import MongoClient

from core.config import logger  # isort: skip

client = MongoClient("mongodb://mongo:27017/mydatabase")
db = client["form_db"]
collection = db["forms"]


def load_data_to_db():
    with open("core/db_data.json", "r") as f:
        data = json.load(f)
    try:
        collection.insert_many(data)
    except Exception:
        logger.info("Данные уже внесены в базу!")
