from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/reviews", tags=["reviews"])

# Mock reviews (list ของ dict)
mock_reviews = [
    {"car_id": "1",   "exterior": 7, "interior": 7, "value": 9, "fuel_economy": 9, "performance": 6},
    {"car_id": "1.1", "exterior": 8, "interior": 7, "value": 8, "fuel_economy": 8, "performance": 7},
    {"car_id": "1.2", "exterior": 8, "interior": 8, "value": 8, "fuel_economy": 9, "performance": 7},
    {"car_id": "1.3", "exterior": 9, "interior": 9, "value": 8, "fuel_economy": 8, "performance": 9},
    {"car_id": "2",   "exterior": 8, "interior": 7, "value": 8, "fuel_economy": 9, "performance": 7},
    {"car_id": "2.1", "exterior": 9, "interior": 8, "value": 8, "fuel_economy": 8, "performance": 9},
    {"car_id": "2.2", "exterior": 9, "interior": 9, "value": 8, "fuel_economy": 9, "performance": 8},
    {"car_id": "2.3", "exterior": 8, "interior": 8, "value": 8, "fuel_economy": 8, "performance": 7},
    {"car_id": "3",   "exterior": 6, "interior": 6, "value": 8, "fuel_economy": 8, "performance": 6},
    {"car_id": "3.1", "exterior": 8, "interior": 8, "value": 8, "fuel_economy": 8, "performance": 8},
    {"car_id": "3.2", "exterior": 8, "interior": 7, "value": 8, "fuel_economy": 7, "performance": 8},
    {"car_id": "3.3", "exterior": 9, "interior": 8, "value": 8, "fuel_economy": 6, "performance": 8},
    {"car_id": "4",   "exterior": 7, "interior": 7, "value": 8, "fuel_economy": 8, "performance": 6},
    {"car_id": "4.1", "exterior": 8, "interior": 8, "value": 8, "fuel_economy": 6, "performance": 8},
    {"car_id": "5",   "exterior": 9, "interior": 9, "value": 7, "fuel_economy": 5, "performance": 8},
    {"car_id": "5.1", "exterior": 8, "interior": 8, "value": 8, "fuel_economy": 6, "performance": 8},
    {"car_id": "5.2", "exterior": 9, "interior": 7, "value": 7, "fuel_economy": 6, "performance": 10},
    {"car_id": "5.3", "exterior": 9, "interior": 7, "value": 7, "fuel_economy": 7, "performance": 10},
    {"car_id": "6",   "exterior": 8, "interior": 7, "value": 7, "fuel_economy": 5, "performance": 7},
    {"car_id": "6.1", "exterior": 7, "interior": 7, "value": 8, "fuel_economy": 8, "performance": 6},
    {"car_id": "6.2", "exterior": 6, "interior": 6, "value": 8, "fuel_economy": 7, "performance": 5},
]

# แปลงเป็น dict สำหรับ lookup
mock_reviews_dict = {review["car_id"]: review for review in mock_reviews}

# Route สำหรับดึง review ตาม car_id
@router.get("/{car_id}")
def get_review(car_id: str):
    review = mock_reviews_dict.get(car_id)
    if not review:
        raise HTTPException(status_code=404, detail="Review not found")
    return review
