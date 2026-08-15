from src import transform as hasil_olahan_data
import pandas as pd
from src.utils import logger as log
import time
from pathlib import Path
from src.utils import connect_db as conn_db

def load_data():
    ROOT_DIR = Path(__file__).parent.parent
    PATH_DIR = ROOT_DIR / "data" / "processed" / "data_penjualan_(bersih).csv"
    
    hasil = hasil_olahan_data.transform_data()
    log.logger.info("Proses mengambil hasil olahan data")
    time.sleep(5)
    
    simpan_data = hasil.to_csv(PATH_DIR, index=False)
    hasil.to_sql(
        name="data_penjualan_buku",
        con=conn_db.koneksi_database(),
        if_exists="append",
        index=False,
        chunksize=1000
    )
    log.logger.info("Berhasil menyimpan data ke dalam csv dan database")
    
    return simpan_data