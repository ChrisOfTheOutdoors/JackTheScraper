import os
import sys
import csv
import logging
from pysitemap import crawler
from bs4 import BeautifulSoup

import re

allURLs = re.sub('<[^<]+>', "", open("sitemap.xml").read())
with open("SiteMap.csv", "w") as f:
    f.write(allURLs)
    
import pandas as pd

siteMap = 'SiteMap.csv'
sheet1 = pd.read_csv(siteMap, sheet_name="sheet1")
print(sheet1.head(10))

f.close