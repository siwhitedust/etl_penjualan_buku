import pandas as pd
from src import extract as extrc
from src.utils import logger as log
import time

def transform_data():
    log.logger.info("Proses mengambil data untuk diolah")
    ambil_data = extrc.ekstraksi_data()
    time.sleep(5)
    
    log.logger.info("Proses menghapus data yang duplikat")
    ambil_data = ambil_data.drop_duplicates()
    time.sleep(5)
    log.logger.info("Berhasil menghapus data duplikat")
    
    log.logger.info("Proses mengubah data type tanggal menjadi datetime")
    ambil_data["Tanggal"] = pd.to_datetime(ambil_data["Tanggal"], format="mixed", dayfirst=True)
    time.sleep(5)
    log.logger.info("Berhasil mengubah tipe data")
    time.sleep(3)
    
    return ambil_data