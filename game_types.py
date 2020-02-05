import pandas as pd
import numpy as np
import requests
from datetime import datetime

# capture today's date
today = str(datetime.now().strftime('%Y%m%d'))

# base URL
url = 'https://statsapi.web.nhl.com/api/v1/'

r = requests.get(url + 'gameTypes')
data = r.json()
data

game_type_id = []
game_type_description = []
game_type_postseason = []

for gtype in data:
    game_type_id.append(gtype['id'])
    game_type_description.append(gtype['description'])
    game_type_postseason.append(gtype['postseason'])
    
    
game_types = {
    'game_type_id':game_type_id,
    'game_type_description':game_type_description,
    'game_type_postseason':game_type_postseason
}

game_types_df = pd.DataFrame(game_types)

game_types_df.to_csv('data/game-types/game_types.csv', index=False)