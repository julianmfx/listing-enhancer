#!/usr/bin/env python
# coding: utf-8
# extract/dictionary.py

# import libraries

import pandas as pd

from utils.paths import get_root_dir

# define constants
ROOT_DIR = get_root_dir()
DATA_DIR = ROOT_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

# Load data

calendar = pd.read_csv(PROCESSED_DATA_DIR / "calendar_dictionary_clean.csv")
listings = pd.read_csv(PROCESSED_DATA_DIR / "listings_dictionary_clean.csv")
reviews = pd.read_csv(PROCESSED_DATA_DIR / "reviews_dictionary_clean.csv")

# View data
calendar.head()
listings.head()
reviews.head()
# Evaluate listings dictionary
for row in listings.itertuples():
    print(f"{row.field}: {row.description}")
# Option 3: if you just want to inspect, return the df as the last expression
with pd.option_context("display.max_rows", None):
    display(listings[["field", "description"]])
