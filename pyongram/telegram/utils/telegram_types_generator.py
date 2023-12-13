# class TelegramTypesGenerator:
#     pass
import json

import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(requests.get("https://core.telegram.org/bots/api").text, "html.parser")
headers = soup.find_all("h4")
tables = soup.find_all("table")
skip = 0
res = {}
edit_headers = []
for header in headers:
    if skip < 5:
        skip += 1
        continue
    if " " in header.text:
        continue
    edit_headers.append(header)

for header, table in zip(edit_headers, tables):
    res_table = []
    for tag_tr in table.find_all("tr"):
        split = tag_tr.text.split("\n")
        del split[0]
        del split[len(split) - 1]
        if len(split) == 3:
            res_table.append({split[0]: split[1]})

        if len(split) == 4:
            res_table.append({split[0]: {split[1]: split[2]}})
    res[header.text] = res_table
print(json.dumps(res, indent=4))
