import asyncio
import asyncore
import csv
from email import parser
import logging
import os
import re
import sys
from usp.tree import sitemap_tree_for_homepage
from asyncore import write
from tkinter import END
from urllib import response

import bs4
import pandas as pd
import requests
from bs4 import BeautifulSoup
from pysitemap import crawler

url = 'http://books.toscrape.com'
response = requests.get(url)

redAlert = "Critical Error - URL Not Available - Try a new URL"

print(response)
if response.status_code == 200:
        print("Success!")
        
else: 
    with open("ErrorLog.txt", "w") as errorLog:
        errorLog.write(redAlert)
        print(redAlert)
        errorLog.close()
