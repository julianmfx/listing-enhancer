#!/usr/bin/env python
# coding: utf-8

# In[1]:

import pandas as pd

from utils.paths import get_root_dir

# In[2]:

ROOT_DIR = get_root_dir()
print(ROOT_DIR)

# In[3]:

DATA_DIR = ROOT_DIR / "data"

# In[ ]:

url = (
    "https://data.insideairbnb.com/mexico/df/mexico-city/2025-09-27/data/reviews.csv.gz"
)
url = "https://data.insideairbnb.com/mexico/df/mexico-city/2025-09-27/data/listings.csv.gz"
url = "https://data.insideairbnb.com/mexico/df/mexico-city/2025-09-27/data/calendar.csv.gz"

# In[18]:

df = pd.read_csv(url, compression="gzip")

# In[19]:
df[["id", "listing_url"]]

df.head()

df.info()

# In[20]:

df.shape

# In[29]:

df["calendar_updated"]

# In[21]:

df.info()

# In[30]:

dictionary_path = "data/Inside Airbnb Data Dictionary.xlsx"

# In[33]:

all_sheets = pd.read_excel(f"{ROOT_DIR}/{dictionary_path}", sheet_name=None)
all_sheets


# In[36]:

for sheet_name, df in all_sheets.items():
    print(f"{sheet_name}")
    print(f"{df.shape}")

# In[ ]:


listings_dictionary = pd.read_excel(
    f"{ROOT_DIR}/{dictionary_path}", sheet_name="listings.csv detail v4.3"
)
reviews_dictionary = pd.read_excel(
    f"{ROOT_DIR}/{dictionary_path}", sheet_name="reviews.csv v1"
)
calendar_dictionary = pd.read_excel(
    f"{ROOT_DIR}/{dictionary_path}", sheet_name="calendar.csv v2"
)


# In[ ]:


listings_dictionary.to_csv(f"{DATA_DIR}/listings_dictionary.csv", index=False)
reviews_dictionary.to_csv(f"{DATA_DIR}/reviews_dictionary.csv", index=False)
calendar_dictionary.to_csv(f"{DATA_DIR}/calendar_dictionary.csv", index=False)
print("✅ Exported 3 files successfully!")

# view dictionaries
## dictionaries are not correctly parsed in csv
## probably a manual cleaning would be a fit for them
## Let's start with listings_dictionary as it will be our main data source
listings_dictionary.head()
listings_dictionary.shape
listings_dictionary.info()
listings_dictionary.describe()

reviews_dictionary.head()
reviews_dictionary.shape
reviews_dictionary.info()
reviews_dictionary.describe()

calendar_dictionary.head()
calendar_dictionary.shape
calendar_dictionary.info()
calendar_dictionary.describe()
