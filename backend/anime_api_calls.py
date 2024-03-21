def getAnimeList(username: str) -> str:
    return f'https://api.myanimelist.net/v2/users/{username}/animelist?fields=id,anime_start_date&status=watching&limit=20&nsfw=true'

def getAnimeDetailsURL(id: str) -> str:
	return f'https://api.myanimelist.net/v2/anime/{id}?fields=id,title,alternative_titles,start_date,end_date'
