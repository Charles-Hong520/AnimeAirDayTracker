from typing import Union
import json
from fastapi import FastAPI
import os
import requests
import datetime
import calendar
from anime_api_calls import *

CLIENT_ID = os.getenv("CLIENT_ID")

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/anime")
def get_airing(username: str) -> dict:
    user_watching_url = getAnimeList(username)
    anime_dict = requests.get(user_watching_url, headers = {'X-MAL-CLIENT-ID': CLIENT_ID}).json()
    l = []
    for anime in anime_dict["data"]:
        anime_url = getAnimeDetailsURL(anime["node"]["id"])
        response = requests.get(anime_url, headers = {'X-MAL-CLIENT-ID': CLIENT_ID}).json()
        start_date = response["start_date"]
        year, month, day = [int(string) for string in start_date.split('-')]
        weekday = datetime.datetime(year,month,day).weekday()
        title = response["title"]
        if response['alternative_titles']['en'] != '':
            title = response['alternative_titles']['en']
        l.append((weekday, title))
        today = datetime.date.today()
    json_output = {}
    for i, (weekday, title) in enumerate(sorted(l)):
        if weekday not in json_output.keys():
            json_output[weekday] = []
        json_output[weekday].append(title)
    return json_output
