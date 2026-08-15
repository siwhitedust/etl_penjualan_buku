import logging
from pathlib import Path

def log_aktivitas():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    
    if logger.hasHandlers():
        logger.handlers.clear()
        
    ROOT_DIR = Path(__file__).resolve().parent.parent.parent
    LOG_FILE = ROOT_DIR / "ETL.log"

    template_log = logging.Formatter("%(asctime)s - [%(levelname)s] - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

    console = logging.StreamHandler()
    console.setLevel(logging.INFO)

    file_handler = logging.FileHandler(LOG_FILE, mode="a")
    file_handler.setLevel(logging.INFO)

    console.setFormatter(template_log)
    file_handler.setFormatter(template_log)

    logger.addHandler(console)
    logger.addHandler(file_handler)

    logger.info("test masuk dari main")
    
    return logger