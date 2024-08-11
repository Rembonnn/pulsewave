import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import uuid
from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.database import Base, engine
from app.models.user import User  # Pastikan model User Anda terletak di sini

# Inisialisasi Faker
fake = Faker()

# Buat Session
Session = sessionmaker(bind=engine)
session = Session()

# Buat 30 data user
def users_faker():
    for _ in range(30):
        user = User(
            id=uuid.uuid4(),
            name=fake.name(),
            email=fake.unique.email(),
            password=fake.password(),
            email_verified_at=fake.date_time_this_year(),
            created_at=fake.date_time_this_year(),
            updated_at=fake.date_time_this_year()
        )
        session.add(user)

    session.commit()

if __name__ == "__main__":
    # Jalankan seeder
    users_faker()
    print("30 users have been seeded.")
