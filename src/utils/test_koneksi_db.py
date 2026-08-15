from sqlalchemy import text
from sqlalchemy.exc import OperationalError, SQLAlchemyError
from src.utils import logger as log
from src.utils import connect_db as cdb

def test_koneksi_db():
    try:
        with cdb.koneksi_database().connect() as conn:
            result = conn.execute(text("Select 1"))
            
            if result.scalar() == 1:
                print("Koneksi Database Berhasil")
                log.logger.info("Koneksi Database Berhasil")
                return True
    except OperationalError as e:
        log.logger.critical(f"Koneksi gagal: {e}")
    except SQLAlchemyError as e:
        log.logger.critical(f"Terjadi error pada SQLAlchemy: {e}")
    except Exception as e:
        log.logger.critical(f"Terjadi Error tidak terduga: {e}")
        
    return False