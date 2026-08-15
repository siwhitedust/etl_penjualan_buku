from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
from sqlalchemy.engine import URL

def koneksi_database():
    load_dotenv()
    
    connection_db = URL.create(
        drivername="mysql+pymysql",
        username=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT"),
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME")
    )
    
    engine = create_engine(connection_db)
    
    return engine