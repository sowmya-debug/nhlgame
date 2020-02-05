import numpy as np
import pandas as pd
import requests
import datetime

# capture today's date
today = str(datetime.datetime.now().strftime("%Y%m%d"))

# base url
url = 'https://statsapi.web.nhl.com/api/v1/'

# create new url and convert to json
r = requests.get(url + 'schedule?season=20192020')
data = r.json()

gamePk = []
game_date = []
home_team_id = []
home_team_name = []
away_team_id = []
away_team_name = []
game_type = []

for date in data['dates']:

    for game in date['games']:

        game_date.append(date['date'])
        gamePk.append(game['gamePk'])
        game_type.append(game['gameType'])
        home_team_id.append(game['teams']['home']['team']['id'])
        away_team_id.append(game['teams']['away']['team']['id'])
        home_team_name.append(game['teams']['home']['team']['name'])
        away_team_name.append(game['teams']['away']['team']['name'])
        
game_df = pd.DataFrame({
    
    'date':game_date,
    'gamePk':gamePk,
    'game_type':game_type,
    'home_team_id':home_team_id,
    'home_team_name':home_team_name,
    'away_team_id':away_team_id,
    'away_team_name':away_team_name
})

# export data to csv
game_df.to_csv(f'data/games/games.csv', index=False)
