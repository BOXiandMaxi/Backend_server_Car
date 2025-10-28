from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from models import Car
from data import cars_db
from utils.putDB import fetch_car_prices_by_id  # เปลี่ยนเป็น fetch by id


router = APIRouter()

# รถทั้งหมด
@router.get("/cars", response_model=list[Car])
async def get_cars():
    return cars_db

# รถแต่ละคัน
@router.get("/cars/{car_id}", response_model=Car)
async def get_car(car_id: str):
    for car in cars_db:
        if car["id"] == car_id:
            return car
    raise HTTPException(status_code=404, detail="Car not found")

# กราฟราคาตาม car_id
@router.get("/cars/{car_id}/price-data")
async def get_price_data(car_id: str):
    data = fetch_car_prices_by_id(car_id)
    if not data:
        raise HTTPException(status_code=404, detail=f"No price data found for car id {car_id}")
    return {
        "car_id": car_id,
        "prices": data
    }