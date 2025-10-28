# Backend/Review/review_routes.py
from fastapi import APIRouter, HTTPException
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, select

DATABASE_URL = "mysql+pymysql://root:@localhost/searchforsales"
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

router = APIRouter(
    prefix="/reviews",
    tags=["reviews"]
)

@router.get("/{car_id}")
def get_review(car_id: str):
    # ใช้ engine.begin() เพื่อสร้าง transaction context
    with engine.begin() as conn:
        result = conn.execute(
            select(carsreviews).where(carsreviews.c.car_id == car_id)
        ).first()  # ดึงแถวแรก
    
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