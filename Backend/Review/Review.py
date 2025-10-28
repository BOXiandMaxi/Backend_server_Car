# Backend/Review/Review.py
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData

DATABASE_URL = "mysql+pymysql://root:@localhost/searchforsales"
engine = create_engine(DATABASE_URL, echo=True)
metadata = MetaData()

carsreviews = Table(
    'carsreviews', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('car_id', String(20), nullable=False),
    Column('exterior', Integer),
    Column('interior', Integer),
    Column('value', Integer),
    Column('fuel_economy', Integer),
    Column('performance', Integer),
)

# ✅ Mock review data
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

with engine.connect() as conn:
    for review in mock_reviews:
        insert_stmt = carsreviews.insert().values(
            car_id=review[0],
            exterior=review[1],
            interior=review[2],
            value=review[3],
            fuel_economy=review[4],
            performance=review[5]
        )
        conn.execute(insert_stmt)
    conn.commit()

print("✅ Insert mock reviews into carsreviews table successfully!")
