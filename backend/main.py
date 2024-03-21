from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Union
import redis, json, os, requests, datetime
from anime_api_calls import *
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")

app = FastAPI()


origins = [
    "http://localhost",
    "http://localhost:5173",
    "http://localhost:4173",
    "https://charles-hong520.github.io",
    "https://charles-hong520.github.io/",
    "https://charles-hong520.github.io/AnimeAirDayTracker/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
redis_client = redis.Redis(host='localhost', port=6379, decode_responses=True)

@app.get("/test/{username}")
async def read_root(username: str):
    cached_data = redis_client.get(username)
    if cached_data is not None:
        print("cached")
        return cached_data
    redis_client.set(name=username, value=f"get__{username}__get", ex=10)
    print("not cached")
    return f"get__{username}__get"


@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/AnimeAirDayTracker")
async def get_airing(username: str) -> dict:
    user_watching_url = getAnimeList(username)
    
    json_output = redis_client.get(username)
    

    if json_output is not None:
        print("returning cached", username)
        
        return json.loads(json_output)

    anime_dict = requests.get(user_watching_url, headers = {'X-MAL-CLIENT-ID': CLIENT_ID}).json()
    if "error" in anime_dict:
        redis_client.set(name=username)
        raise HTTPException(status_code=404, detail=anime_dict["error"])
    l = []
    for anime in anime_dict["data"]:
        anime_url = getAnimeDetailsURL(anime["node"]["id"])
        response = requests.get(anime_url, headers = {'X-MAL-CLIENT-ID': CLIENT_ID})
        response = response.json()
        start_date = response["start_date"]
        year, month, day = [int(string) for string in start_date.split('-')]
        weekday = datetime.datetime(year,month,day).weekday()
        title = response["title"]
        if response['alternative_titles']['en'] != '':
            title = response['alternative_titles']['en']
        l.append((weekday, title))
    json_output = {}
    for i, (weekday, title) in enumerate(sorted(l)):
        if weekday not in json_output.keys():
            json_output[weekday] = []
        json_output[weekday].append(title)
    for i in range(7):
        if i not in json_output.keys():
            json_output[i] = []
    redis_client.set(username, json.dumps(json_output), ex=datetime.timedelta(hours=144))
    print("returning non-cached", username)
    return json_output
