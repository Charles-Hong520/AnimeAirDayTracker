def getAnimeList(username: str) -> str:
    return f'https://api.myanimelist.net/v2/users/{username}/animelist?status=watching&limit=15&nsfw=true'

def getAnimeDetailsURL(id: str) -> str:
	return f'https://api.myanimelist.net/v1/anime/{id}?fields=id,title,main_picture,alternative_titles,start_date,end_date,synopsis,mean,rank,popularity,num_list_users,num_scoring_users,nsfw,created_at,updated_at,media_type,status,genres,my_list_status,num_episodes,start_season,broadcast,source,average_episode_duration,rating,pictures,background,related_anime,related_manga,recommendations,studios,statistics'
