# ดึงข้อมูลจาก MySQL
import os
from dotenv import load_dotenv
import mysql.connector

# โหลดค่าจาก .env
load_dotenv()

def get_db_connection():
    return mysql.connector.connect(
        host=os.environ.get("DB_HOST"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASS"),
        database=os.environ.get("DB_NAME")
    )