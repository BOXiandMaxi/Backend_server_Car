from fastapi import APIRouter, HTTPException
from models import Car
from data import cars_db
from utils.putDB import fetch_car_prices_by_id

router = APIRouter()

# # ✅ รถทั้งหมด
# @router.get("/", response_model=list[Car])
# async def get_cars():
#     return cars_db

# รถทั้งหมด (lightweight) สำหรับหน้า Home
@router.get("/summary")
async def get_cars_summary():
    return [
        {
            "id": car["id"],
            "brand": car["brand"],
            "model": car["model"],
            "image_url": car["image_url"],
            "price_new": car["price_new"],
            "price_twohand": car["price_twohand"],
        } for car in cars_db
    ]


# รถแต่ละคัน
@router.get("/{car_id:path}", response_model=Car)
async def get_car(car_id: str):
    for car in cars_db:
        if car["id"] == car_id:
            return car
    raise HTTPException(status_code=404, detail="Car not found")

# ราคา
@router.get("/{car_id:path}/price-data")
async def get_price_data(car_id: str):
    data = fetch_car_prices_by_id(car_id)
    if not data:
        raise HTTPException(status_code=404, detail=f"No price data found for car id {car_id}")
    return {"car_id": car_id, "prices": data}
