import requests,json,datetime,calendar

season = "Winter"
year = 2024

CLIENT_ID = "e35f268cb013b3bafac987ca19a81b58"
username = "basketbals"
seasonal_url = f"https://api.myanimelist.net/v2/anime/season/{year}/{season.lower()}?limit=2"
top_airing_url = "https://api.myanimelist.net/v2/anime/ranking?ranking_type=airing&limit=13"
user_watching_url = f'https://api.myanimelist.net/v2/users/{username}/animelist?status=watching&limit=15&nsfw=true'

def getAnimeDetails(id):
	return f'https://api.myanimelist.net/v1/anime/{id}?fields=id,title,main_picture,alternative_titles,start_date,end_date,synopsis,mean,rank,popularity,num_list_users,num_scoring_users,nsfw,created_at,updated_at,media_type,status,genres,my_list_status,num_episodes,start_season,broadcast,source,average_episode_duration,rating,pictures,background,related_anime,related_manga,recommendations,studios,statistics'
response = requests.get(user_watching_url, headers = {'X-MAL-CLIENT-ID': CLIENT_ID})
jsonobject = response.json()
print(len(jsonobject["data"]))
l=[]
for anime in jsonobject["data"]:
	anime_url = getAnimeDetails(anime["node"]["id"])
	response = requests.get(anime_url, headers = {'X-MAL-CLIENT-ID': CLIENT_ID}).json()
	start_date = response["start_date"]
	year, month, day = [int(string) for string in start_date.split('-')]
	weekday = datetime.datetime(year,month,day).weekday()
	title = response["title"]
	if response['alternative_titles']['en'] != '':
		title = response['alternative_titles']['en']
	l.append((weekday, title))

today = datetime.date.today()
print(calendar.day_abbr[today.weekday()], today)
for i, (weekday, title) in enumerate(sorted(l)):
	print(f"{i+1}. {calendar.day_abbr[weekday]}: {title}")
