from database import Base, engine
import models

def init_database():
    Base.metadata.create_all(bind=engine)
    print("table created successfully")

if __name__ == "__main__":
    init_database()