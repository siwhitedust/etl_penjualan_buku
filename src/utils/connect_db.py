from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
from sqlalchemy.engine import URL
from src.utils import logger as log

def koneksi_database():
    log.logger.info("Memulai koneksi ke database MySql")
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
    log.logger.info("Berhasil connect ke database")
    
    return engine