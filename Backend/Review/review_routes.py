from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/reviews", tags=["reviews"])

# Mock reviews
mock_reviews = [
    ('1', 7, 7, 9, 9, 6),
    ('1.1', 8, 7, 8, 8, 7),
    ('1.2', 8, 8, 8, 9, 7),
    ('1.3', 9, 9, 8, 8, 9),
    ('2', 8, 7, 8, 9, 7),
    ('2.1', 9, 8, 8, 8, 9),
    ('2.2', 9, 9, 8, 9, 8),
    ('2.3', 8, 8, 8, 8, 7),
    ('3', 6, 6, 8, 8, 6),
    ('3.1', 8, 8, 8, 8, 8),
    ('3.2', 8, 7, 8, 7, 8),
    ('3.3', 9, 8, 8, 6, 8),
    ('4', 7, 7, 8, 8, 6),
    ('4.1', 8, 8, 8, 6, 8),
    ('5', 9, 9, 7, 5, 8),
    ('5.1', 8, 8, 8, 6, 8),
    ('5.2', 9, 7, 7, 6, 10),
    ('5.3', 9, 7, 7, 7, 10),
    ('6', 8, 7, 7, 5, 7),
    ('6.1', 7, 7, 8, 8, 6),
    ('6.2', 6, 6, 8, 7, 5)
]

# แปลงเป็น dict
mock_reviews_dict = {
    car_id: {
        "car_id": car_id,
        "exterior": exterior,
        "interior": interior,
        "value": value,
        "fuel_economy": fuel,
        "performance": performance
    }
    for car_id, exterior, interior, value, fuel, performance in mock_reviews
}

@router.get("/{car_id}")
def get_review(car_id: str):
    review = mock_reviews_dict.get(car_id)
    if not review:
        raise HTTPException(status_code=404, detail="Review not found")
    return review
