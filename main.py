import src.utils.logger as log
import src.load as load
import src.utils.connect_db as conn_db

if __name__ == "__main__":
    log.log_aktivitas()
    conn_db.koneksi_database()