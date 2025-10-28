from db import get_db_connection

def fetch_car_prices_by_id(car_id: str):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT year, price_new, price_twohand, price_in_2024
        FROM carssales
        WHERE id=%s
        ORDER BY year ASC
    """, (car_id,))
    data = cursor.fetchall()
    conn.close()
    return data
