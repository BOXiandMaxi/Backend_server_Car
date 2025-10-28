# import matplotlib.pyplot as plt
# import io
# from .putDB import fetch_car_prices_by_id

# def generate_price_chart_img(model: str):
#     prices = fetch_car_prices_by_id(model)
#     if not prices:
#         return None

#     years = [p["year"] for p in prices]
#     price_new = [p["price_new"] for p in prices]
#     price_twohand = [p["price_twohand"] for p in prices]

#     plt.figure(figsize=(8,5))
#     plt.plot(years, price_new, marker='o', label='ราคามือ 1')
#     plt.plot(years, price_twohand, marker='o', label='ราคามือ 2')
#     plt.title(f"ราคา {model} ตั้งแต่ปี 2023")
#     plt.xlabel("ปี")
#     plt.ylabel("ราคา (บาท)")
#     plt.legend()
#     plt.grid(True)

#     buf = io.BytesIO()
#     plt.savefig(buf, format="png")
#     buf.seek(0)
#     plt.close()
#     return buf