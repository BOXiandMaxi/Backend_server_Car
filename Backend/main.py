from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from routes.cars_routes import router as cars_router
from Review.review_routes import router as review_router
from data import cars_db
import os

app = FastAPI()

# ✅ CORS ให้ React บน vercel เรียกได้
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://search-car-project.vercel.app",
        "http://localhost:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ เปิดให้ดูภาพใน /images
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app.mount("/images", StaticFiles(directory=os.path.join(BASE_DIR, "images")), name="images")

# ✅ รวม routers
app.include_router(cars_router, prefix="/cars", tags=["Cars"])
app.include_router(review_router, prefix="/reviews", tags=["Reviews"])

# ✅ Root message
@app.get("/")
def root():
    return {"message": "Backend server is running ✅ Use /cars or /reviews"}
