import os
from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # หรือ ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve รูปจากโฟลเดอร์ images แบบ absolute path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app.mount("/images", StaticFiles(directory=os.path.join(BASE_DIR, "images")), name="images")


class Car(BaseModel):
    id: float
    brand: str
    model: str
    year: int
    price_new: int
    price_twohand: int
    fuel_consumption: float
    engine: str
    maximum_power:str
    image_url: str

cars_db = [
    # Toyota /////
    {
        "id": 1,
        "brand": "Toyota",
        "model": "yaris",
        "year": 2023,
        "price_new": 539000,
        "price_twohand": 469000,
        "fuel_consumption": 23.3,
        "engine":"Dual VVT-iE 1.2L",
        "maximum_power": "110 Nm",
        "image_url": "http://127.0.0.1:8001/images/toyota/y-2023/toyota-yaris-ativ.png",
    },
    {
        "id": 1.1,
        "brand": "Toyota",
        "model": "vios",
        "year": 2023,
        "price_new": 609000,
        "price_twohand": 260000,
        "fuel_consumption": 20,
        "engine":"เบนซิน 1.5 ลิตร, 4 สูบ, DOHC, 16 วาล์ว, Dual VVT-i ",
        "maximum_power": " 108 แรงม้า ที่ 6,000 รอบ/นาที ",
        "image_url": "http://127.0.0.1:8001/images/toyota/y-2023/toyota-vios-2023.jpg",
    },
    {
       "id": 1.2,
        "brand": "Toyota",
        "model": "corolla-altis",
        "year": 2023,
        "price_new": 894000,
        "price_twohand": 400000,
        "fuel_consumption": 23.3,
        "engine":"ครื่องยนต์ 1ZR-FBE,เกียร์ Super CVT-i",
        "maximum_power": " 125 แรงม้า, แรงบิด 156 นิวตันเมตร",
        "image_url": "http://127.0.0.1:8001/images/toyota/y-2023/toyota-corolla-altis-2023.jpg", 
    },
    {
       "id": 1.3,
        "brand": "Toyota",
        "model": "camary",
        "year": 2023,
        "price_new": 1475000,
        "price_twohand": 900000,
        "fuel_consumption": 20,
        "engine":"เครื่องยนต์เบนซิน 2.5 ลิตร",
        "maximum_power": "ให้กำลังสูงสุด 209 แรงม้า.",
        "image_url": "http://127.0.0.1:8001/images/toyota/y-2023/toyota-camry-2023.jpg", 
    },
    # Honda /////
    {
        "id": 2,
        "brand": "Honda",
        "model": "city",
        "year": 2023,
        "price_new": 599000,
        "price_twohand": 549000,
        "fuel_consumption": 23.8,
        "engine":"3-cyl DOHC 12v",
        "maximum_power": "109 HP",
        "image_url": "http://127.0.0.1:8001/images/honda/y-2023/honda-city-2023.jpg",   
    },
    {
        "id": 2.1,
        "brand": "Honda",
        "model": "civic",
        "year": 2023,
        "price_new": 1239000,
        "price_twohand": 744000,
        "fuel_consumption": 33,
        "engine":"เบนซิน 1.5 ลิตร เทอร์โบ ",
        "maximum_power": "กำลังสูงสุด 178 แรงม้า",
        "image_url": "http://127.0.0.1:8001/images/honda/y-2023/honda-civic-2023.jpg",
    },
    {
        "id": 2.2,
        "brand": "Honda",
        "model": "accord",
        "year": 2023,
        "price_new": 1529000,
        "price_twohand": 1089000,
        "fuel_consumption": 25,
        "engine":"เบนซิน 4 สูบ Atkinson cycle ขนาด 2.0 ลิตร ทำงานร่วมกับมอเตอร์ไฟฟ้า 2 ตัว",
        "maximum_power": "184 แรงม้า (มอเตอร์ไฟฟ้า)",
        "image_url": "http://127.0.0.1:8001/images/honda/y-2023/honda-accord-2023.png",
    },
    {
        "id": 2.3,
        "brand": "Honda",
        "model": "hr-v",
        "year": 2023,
        "price_new": 979000,
        "price_twohand": 739000,
        "fuel_consumption": 25,
        "engine":"รุ่นเบนซิน: เครื่องยนต์ 4 สูบ 1.5 ลิตร i-VTEC. ",
        "maximum_power": "106 แรงม้า",
        "image_url": "http://127.0.0.1:8001/images/honda/y-2023/honda-hrv-2023.jpg",
    },
    # Mitsubishi /////
    {
        "id": 3,
        "brand": "Mitsubishi",
        "model": "attrage",
        "year": 2023,
        "price_new": 529000,
        "price_twohand": 349000,
        "fuel_consumption": 23,
        "engine":"รุ่นเบนซิน: เบนซิน 3 สูบ DOHC MIVEC 12 วาล์ว ความจุ 1.2 ลิตร ",
        "maximum_power": "78 แรงม้า ที่ 6,000 รอบ/นาที ",
        "image_url": "http://127.0.0.1:8001/images/mitsubishi/y-2023/mitsubishi-attrage-2023.jpg",  
    },
    {
        "id": 3.1,
        "brand": "Mitsubishi",
        "model": "outlander",
        "year": 2023,
        "price_new": 1749000,
        "price_twohand": 699000,
        "fuel_consumption": 20,
        "engine":"เครื่องยนต์ 4 สูบ ขนาด 2.4 ลิตร",
        "maximum_power": "248 แรงม้า. ระบบขับเคลื่อนปลั๊กอินไฮบริด",
        "image_url": "http://127.0.0.1:8001/images/mitsubishi/y-2023/mitsubishi-outlander-2023.png",
    },
    {
        "id": 3.2,
        "brand": "Mitsubishi",
        "model": "triton",
        "year": 2023,
        "price_new": 820000,
        "price_twohand": 559000,
        "fuel_consumption": 20,
        "engine":"เครื่องยนต์ดีเซล 4 สูบ ขนาด 2.4 ลิตร เทอร์โบแปรผัน (VG-Turbo) อินเตอร์คูลเลอร์",
        "maximum_power": "184 แรงม้า ที่ 3,500 รอบ/นาที ",
        "image_url": "http://127.0.0.1:8001/images/mitsubishi/y-2023/mitsubishi-triton-2023.jpg",
    },
    {
        "id": 3.3,
        "brand": "Mitsubishi",
        "model": "pajero",
        "year": 2023,
        "price_new": 1200000,
        "price_twohand": 849000,
        "fuel_consumption": 15.2,
        "engine":"มาพร้อมเครื่องยนต์ดีเซล 2.4 ลิตร เทอร์โบ",
        "maximum_power": "181 แรงม้า แรงบิด 430 นิวตันเมตร",
        "image_url": "http://127.0.0.1:8001/images/mitsubishi/y-2023/mitsubishi-pajero-2023.png",
    },
]

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!"}

# Route สำหรับรถทั้งหมด
@app.get("/cars", response_model=List[Car])
async def get_cars():
    return cars_db

# Route สำหรับรถแต่ละคัน
@app.get("/cars/{car_id}", response_model=Car)
async def get_car(car_id: float):
    for car in cars_db:
        if car["id"] == car_id:
            return car
    return {"error": "Car not found"}
