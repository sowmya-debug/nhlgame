import pandas as pd
import numpy as np
import requests
from datetime import datetime

# capture today's date
today = str(datetime.now().strftime('%Y%m%d'))

# base URL
url = 'https://statsapi.web.nhl.com/api/v1/'
season = 20182019

r = requests.get(url + f'schedule?season={season}')
data = r.json()

game_id = []
season_id = []
game_date = []
game_type = []
away_team_id = []
home_team_id = []
away_team_goals = []
home_team_goals = []
venue_name = []

for date in data['dates']:
    
    for game in date['games']:
        
        game_date.append(game['gameDate'])
        season_id.append(season)
        game_id.append(game['gamePk'])
        game_type.append(game['gameType'])
        away_team_id.append(game['teams']['away']['team']['id'])
        home_team_id.append(game['teams']['home']['team']['id'])
        away_team_goals.append(game['teams']['away']['score'])
        home_team_goals.append(game['teams']['home']['score'])
        venue_name.append(game['venue']['name'])
        

game = {
    'game_id':game_id,
    'season_id':season,
    'game_date':game_date,
    'game_type':game_type,
    'away_team_id':away_team_id,
    'home_team_id':home_team_id,
    'away_team_goals':away_team_goals,
    'home_team_goals':home_team_goals,
    'venue_name':venue_name
}

game_df.to_csv('data/games/games_new.csv')
