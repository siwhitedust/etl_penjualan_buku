import pandas as pd
from pathlib import Path

def ekstraksi_data():
    ROOT_DIR = Path(__file__).resolve().parent.parent
    FILE_PATH =ROOT_DIR / "data" / "data_penjualan_buku.csv"
    
    sumber_data = pd.read_csv(FILE_PATH, sep=";")
    df = pd.DataFrame(sumber_data)

    return df