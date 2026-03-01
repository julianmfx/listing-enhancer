# src/extract/download.py

# import libraries
import logging
import re
from pathlib import Path

import pandas as pd

from utils.paths import get_root_dir

# intialize logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)
logger = logging.getLogger(__name__)

# define constants
ROOT_DIR = get_root_dir()
DATA_DIR = ROOT_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"

URLS = [
    "https://data.insideairbnb.com/mexico/df/mexico-city/2025-09-27/data/reviews.csv.gz",
    "https://data.insideairbnb.com/mexico/df/mexico-city/2025-09-27/data/listings.csv.gz",
    "https://data.insideairbnb.com/mexico/df/mexico-city/2025-09-27/data/calendar.csv.gz",
]

# define functions

## helpers
def _extract_filename(url:str) -> str:
    url_filename = Path(url).stem.split(".")[0]
    return url_filename

def _extract_date(url:str) -> str:
    cohort_date = re.search(r"\d{4}-\d{2}-\d{2}", url)
    
    if not cohort_date:
        raise ValueError(f"No date found in URL: {url}")
    
    return cohort_date.group()

def download_airbnb_data(url: str, raw_data_dir: Path = RAW_DATA_DIR) -> Path:
    """
    Download a gzipped CSV from Inside Airbnb, tag it with its cohort date,
    and save it as a CSV in raw_data_dir.
    
    Args:
        url:          Direct URL to a .csv.gz file on Inside Airbnb.
        raw_data_dir: Destination folder (created if it doesn't exist).

    Returns:
        Path to the saved CSV file.
    """
    # extract url info and mount path
    filename = _extract_filename(url)
    cohort_date = _extract_date(url)
    csv_path = raw_data_dir / f"{filename}.csv"

    # create directory
    raw_data_dir.mkdir(parents=True, exist_ok=True)

    # check for existing files
    if csv_path.exists():
        logger.info(f"Already exists, skipping → {csv_path}")
        return csv_path

    # download and output to raw directory
    logger.info(f"Downloading {filename} (cohort: {cohort_date})...")

    try:
        df = pd.read_csv(url, compression='gzip')
        
        # add cohort date
        df["cohort_date"] = cohort_date
        
        # output
        df.to_csv(csv_path, index=False)
        logger.info(f"Saved -> {csv_path} with ({len(df):,} rows)")

    except Exception as e:
        logger.error(f"Failed to download {url}: {e}")
        raise

    return csv_path

# entrypoint
if __name__ == "__main__":
    for url in URLS:
        download_airbnb_data(url)