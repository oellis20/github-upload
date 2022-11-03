import pytest
import requests

url = "https://api.duckduckgo.com"
pres_list = ["Adams", "Arthur", "Biden", "Buchanan", "Bush",
             "Carter", "Cleveland", "Clinton", "Coolidge", "Eisenhower",
             "Filmore", "Ford", "Garfield", "Grant", "Harding",
             "Harrison", "Hayes", "Hoover", "Jackson", "Jefferson",
             "Johnson", "Kennedy", "Lincoln", "Madison", "McKinley",
             "Monroe", "Nixon", "Obama", "Pierce", "Polk",
             "Reagan", "Roosevelt", "Taft", "Taylor", "Truman",
             "Trump", "Tyler", "Van Buren", "Washington", "Woodrow"]


def test_ddg():
    resp = requests.get(url + "?q=presidents+of+the+united+states&format=json")
    rsp_data = resp.json()
    text_list = []
    for item in rsp_data['RelatedTopics']:
        text_list.append(item['Text'].rsplit(" -")[0])

    for last_name in pres_list:
        for name in text_list:
            if last_name == name:
                assert True
