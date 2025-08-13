from fastapi import FastAPI
from typing import List
from pydantic import BaseModel

app = FastAPI()

class Car(BaseModel):
    id: int
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
    {
        "id": 1,
        "brand": "Toyota",
        "model": "yaris",
        "year": 2023,
        "price_new": 539000,
        "price_twohand": 469000,
        "fuel_consumption": 23.3,
        "engine":"Dual VVT-iE ขนาด 1.2 ลิตร 4 สูบ แถวเรียง DOHC 16 วาล์ว",
        "maximum_power": "แรงบิดสูงสุด 110 นิวตัน-เมตร (11.2 กก.- เมตร) ที่ 4,400 รอบต่อนาที ",
        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSIkVegSaOG01jzoHCqFWBWSotkYnKPA4CnSw&s",
    },
    {
     "id": 2,
        "brand": "Honda",
        "model": "city",
        "year": 2023,
        "price_new": 599000,
        "price_twohand": 549000,
        "fuel_consumption": 23.8,
        "engine":"เครื่องยนต์เบนซิน 3 สูบ DOHC 12 วาล์ว 988 ซีซี พร้อมระบบแปรผันวาล์ว VTEC และ Dual VTC กำลังแรงม้าสูง 122 แรงม้า ที่ 5,500 รอบ/นาที และแรงบิดสูงสุด 173 นิวตันเมตร ที่ 2,000–4,500 รอบ/นาที ระบบขับเคลื่อนล้อหน้า ทำงานคู่กับเกียร์อัตโนมัติ CVT",
        "maximum_power": "ระบบการขับแบบ e:HEV ทำงานร่วมกับมอเตอร์ไฟฟ้า 2 ตัว ให้กำลังแรงม้าสูง 109 แรงม้า ที่ 3,500 – 8,000 รอบ/นาที และแรงบิดสูงสุด 253 นิวตันเมตร ที่ 0-3,000 รอบ/นาที ทำงานคู่กับเกียร์อัตโนมัติ e-CVT",
        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQiEDkdArumZwlCkO_ZIpbalGJpDQ9gtXRx9w&s",   
    }
]
@app.get("/cars",response_model=List[Car])
async def root():
    return cars_db