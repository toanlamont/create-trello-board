import json
import requests
from datetime import datetime


with open("trello.json", "rt") as f:
    pwrd = json.load(f)
key = pwrd["key"]
token = pwrd["token"]


def create_board(board_name):
    url = "https://api.trello.com/1/boards/"
    querystring = {"name": board_name, "key": key, "token": token}
    response = requests.request("POST", url, params=querystring)
    board_id = response.json()["shortUrl"].split("/")[-1].strip()
    print(response.json()["url"])
    return board_id


def create_list(board_id, list_name):
    url = f"https://api.trello.com/1/boards/{board_id}/lists"
    querystring = {"name": list_name, "key": key, "token": token}
    response = requests.request("POST", url, params=querystring)
    list_id = response.json()["id"]
    return list_id


def create_card(list_id, card_name, due):
    url = "https://api.trello.com/1/cards"
    querystring = {
        "name": card_name,
        "idList": list_id,
        "key": key,
        "token": token,
        "due": due,
    }
    response = requests.request("POST", url, params=querystring)
    card_id = response.json()["id"]
    return card_id


board_id = create_board("Pymi 9_5")

tuesday_id = create_list(board_id, "Thu 3")
thursday_id = create_list(board_id, "Thu 5")
day = 86400
due_date = 1652893200  # 19/5/2022


def timestamp_to_string(ts):
    dt = datetime.fromtimestamp(ts)
    return dt.strftime("%m/%d/%Y")


for i in range(1, 13):
    if i % 2 != 0:
        create_card(
            thursday_id,
            "Buoi {}".format(str(i)), timestamp_to_string(due_date))
        due_date = due_date + 5 * day
    else:
        create_card(
            tuesday_id,
            "Buoi {}".format(str(i)), timestamp_to_string(due_date))
        due_date = due_date + 2 * day
