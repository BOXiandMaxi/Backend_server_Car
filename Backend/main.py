from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from routes.cars_routes import router as cars_router
from Review.review_routes import router as review_router
from data import cars_db
import os

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve รูปจากโฟลเดอร์ images
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app.mount("/images", StaticFiles(directory=os.path.join(BASE_DIR, "images")), name="images")

# Include router
app.include_router(cars_router)

# 🔹 Include review router
app.include_router(review_router)


# Route สำหรับดูข้อมูลรถ
@app.get("/cars")
def get_cars():
    return {"data": cars_db}

# 🔹 Optional: Route root
@app.get("/")
def root():
    return {"message": "Backend server is running. Use /test to check routes"}