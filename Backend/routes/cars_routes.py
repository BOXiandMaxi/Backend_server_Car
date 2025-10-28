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

# Mock price data
mock_prices = {
    "1": {"price_new": 539000, "price_in_2024": 485000, "price_twohand": 469000},
    "1.1": {"price_new": 609000, "price_in_2024": 548000, "price_twohand": 260000},
    "1.2": {"price_new": 894000, "price_in_2024": 804600, "price_twohand": 400000},
    "1.3": {"price_new": 1475000, "price_in_2024": 1327500, "price_twohand": 900000},
    "2": {"price_new": 599000, "price_in_2024": 539100, "price_twohand": 458235},
    "2.1": {"price_new": 1239000, "price_in_2024": 1115100, "price_twohand": 947800},
    "2.2": {"price_new": 1529000, "price_in_2024": 1376100, "price_twohand": 1169600},
    "2.3": {"price_new": 979000, "price_in_2024": 881100, "price_twohand": 748900},
    "3": {"price_new": 529000, "price_in_2024": 476100, "price_twohand": 349000},
    "3.1": {"price_new": 1749000, "price_in_2024": 1574100, "price_twohand": 699000},
    "3.2": {"price_new": 820000, "price_in_2024": 738000, "price_twohand": 559000},
    "3.3": {"price_new": 1200000, "price_in_2024": 1080000, "price_twohand": 849000},
    "4": {"price_new": 529000, "price_in_2024": 476100, "price_twohand": 415000},
    "4.1": {"price_new": 770000, "price_in_2024": 693000, "price_twohand": 557000},
    "5": {"price_new": 2990000, "price_in_2024": 2691000, "price_twohand": 1500000},
    "5.1": {"price_new": 1185000, "price_in_2024": 1066500, "price_twohand": 879000},
    "5.2": {"price_new": 3000000, "price_in_2024": 2700000, "price_twohand": 2690000},
    "5.3": {"price_new": 2699000, "price_in_2024": 2429100, "price_twohand": 1899000},
    "6": {"price_new": 1760000, "price_in_2024": 158400, "price_twohand": 130000},
    "6.1": {"price_new": 567000, "price_in_2024": 510300, "price_twohand": 439000},
    "6.2": {"price_new": 319900, "price_in_2024": 287910, "price_twohand": 250000}

}

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
