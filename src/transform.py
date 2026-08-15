import pandas as pd
from src import extract as extrc
from src.utils import logger as log

def transform_data():
    log.logger.info("Proses mengambil data untuk diolah")
    ambil_data = extrc.ekstraksi_data()
    
    log.logger.info("Proses menghapus data yang duplikat")
    ambil_data = ambil_data.drop_duplicates()
    
    log.logger.info("Proses mengubah data type tanggal menjadi datetime")
    ambil_data["Tanggal"] = pd.to_datetime(ambil_data["Tanggal"], format="mixed", dayfirst=True)
    
    return ambil_data