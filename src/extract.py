import pandas as pd
from pathlib import Path
from src.utils import logger as log
import time

def ekstraksi_data():
    ROOT_DIR = Path(__file__).resolve().parent.parent
    FILE_PATH =ROOT_DIR / "data" / "data_penjualan_buku.csv"
    
    log.logger.info("Proses mengambil data...")
    time.sleep(5)
    
    sumber_data = pd.read_csv(FILE_PATH, sep=";")
    df = pd.DataFrame(sumber_data)
    
    log.logger.info("Berhasil mendapatkan data")

    return df