from db import get_db_connection
from data import cars_db  # ไฟล์ที่เก็บข้อมูลรถทั้งหมด

def save_cars_to_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    for car in cars_db:
        # ตรวจสอบค่า price_in_2024 ถ้า None ให้เป็น 0
        price_in_2024 = car.get("price_in_2024") or 0

        cursor.execute("""
            INSERT INTO carssales
            (id, brand, model, year, price_new, price_twohand, price_in_2024)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
                brand=VALUES(brand),
                model=VALUES(model),
                year=VALUES(year),
                price_new=VALUES(price_new),
                price_twohand=VALUES(price_twohand),
                price_in_2024=VALUES(price_in_2024)
        """, (
            car.get("id"),
            car.get("brand"),
            car.get("model"),
            car.get("year"),
            car.get("price_new") or 0,
            car.get("price_twohand") or 0,
            price_in_2024
        ))

    conn.commit()
    cursor.close()
    conn.close()
    print("✅ Save cars_db to DB successfully!")

if __name__ == "__main__":
    save_cars_to_db()
