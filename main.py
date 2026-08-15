import src.utils.logger as log
import src.extract as extract
import src.transform as trns

if __name__ == "__main__":
    log.log_aktivitas()
    extract.ekstraksi_data()
    print(trns.transform_data())