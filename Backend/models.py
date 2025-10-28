from pydantic import BaseModel
class Car(BaseModel):
    id: str
    brand: str
    model: str
    year: int
    price_new: int
    price_twohand: int
    fuel_consumption: float
    engine: str
    maximum_power:str
    image_url: str
    price_in_2024 : int