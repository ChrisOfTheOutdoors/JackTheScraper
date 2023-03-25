import csv
import logging
import os
import re
import sys

from bs4 import BeautifulSoup
from pysitemap import crawler

if __name__ == '__main__':
    if '--iocp' in sys.argv:
        from asyncio import events, windows_events
        sys.argv.remove('--iocp')
        logging.info('using iocp')
        el = windows_events.ProactorEventLoop()
        events.set_event_loop(el)
   #####################################################################
   ## UPDATE THE = root_url BELOW THIS LINE TO SCRAPE DIFFERENT SITES ##
   ##                                                                 ##
    root_url = 'https://www.mortgagecenter.com'
   ##                                                                 ##
   ## UPDATE THE = root_url ABOVE THIS LINE TO SCRAPE DIFFERENT SITES ##
   #####################################################################
    crawler(root_url, out_file='SiteMap.xml')
    print("SiteMap.xml Created!")

import re

text = re.sub('<[^<]+>', "", open("SiteMap.xml").read())
with open("SiteMap.csv", "w") as f:
    f.write(text)
    print("SiteMap.csv Created!")
    f.close()
