import os
from fastapi import APIRouter, HTTPException
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, select
from dotenv import load_dotenv

# โหลดค่า .env
load_dotenv()

# 🔹 ใช้ DATABASE_URL จาก Render Environment Variable
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in environment variables")

engine = create_engine(DATABASE_URL, echo=True)
metadata = MetaData()

carsreviews = Table(
    'carsreviews', metadata,
    Column('id', Integer, primary_key=True),
    Column('car_id', String(20)),
    Column('exterior', Integer),
    Column('interior', Integer),
    Column('value', Integer),
    Column('fuel_economy', Integer),
    Column('performance', Integer)
)

router = APIRouter(prefix="/reviews", tags=["reviews"])

@router.get("/{car_id}")
def get_review(car_id: str):
    with engine.begin() as conn:
        result = conn.execute(
            select(carsreviews).where(carsreviews.c.car_id == car_id)
        ).first()
    
    if not result:
        raise HTTPException(status_code=404, detail="Review not found")
    
    return {
        "car_id": result.car_id,
        "exterior": result.exterior,
        "interior": result.interior,
        "value": result.value,
        "fuel_economy": result.fuel_economy,
        "performance": result.performance
    }
