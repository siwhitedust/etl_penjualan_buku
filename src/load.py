from src import transform as hasil_olahan_data
import pandas as pd
from src.utils import logger as log
import time
from pathlib import Path

def load_data():
    ROOT_DIR = Path(__file__).parent.parent
    PATH_DIR = ROOT_DIR / "data" / "data_penjualan_(bersih).csv"
    
    hasil = hasil_olahan_data.transform_data()
    log.logger.info("Proses mengambil hasil olahan data")
    time.sleep(5)
    log.logger.info("Berhasil menyimpan data")
    
    simpan_data = hasil.to_csv(PATH_DIR, index=False)
    
    return simpan_data