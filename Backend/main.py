from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from routes.cars_routes import router as cars_router
from Review.review_routes import router as review_router
from data import cars_db
import os

app = FastAPI()

# 🔹 CORS - ให้เฉพาะ frontend โดเมนเข้าถึงได้
frontend_url = "https://search-car-project.vercel.app"
app.add_middleware(
    CORSMiddleware,
    allow_origins=[frontend_url],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔹 Serve รูปจากโฟลเดอร์ images
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app.mount("/images", StaticFiles(directory=os.path.join(BASE_DIR, "images")), name="images")

# 🔹 Include routers
app.include_router(cars_router)
app.include_router(review_router)

# 🔹 Route สำหรับดูข้อมูลรถทั้งหมด
@app.get("/cars_db")
def get_cars():
    return cars_db

# 🔹 Route สำหรับดูข้อมูลรถตาม id
@app.get("/cars/{car_id}")
def get_car(car_id: str):
    for car in cars_db:
        if car["id"] == str(car_id):
            return car
    return {"error": "Car not found"}

# 🔹 Route สำหรับข้อมูลราคารถตาม id
@app.get("/cars/{car_id}/price-data")
def get_car_price_data(car_id: str):
    for car in cars_db:
        if car["id"] == str(car_id):
            # ตัวอย่างส่งราคาต่างๆ (คุณสามารถปรับตามจริง)
            return {"prices": [car.get("price_new", 0), car.get("price_twohand", 0)]}
    return {"prices": []}

# 🔹 Optional: Route root
@app.get("/")
def root():
    return {"message": "Backend server is running. Use /cars_db or /cars/{id} to check routes"}
