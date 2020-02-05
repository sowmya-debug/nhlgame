import pandas as pd
import numpy as np
import requests
from datetime import datetime

# capture today's date
today = str(datetime.now().strftime('%Y%m%d'))

# base URL
url = 'https://statsapi.web.nhl.com/api/v1/'

r = requests.get(url + 'playTypes')
data = r.json()

name = []
play_id = []
cms_key = []
player_type = []
code = []

for event in data:
    
    if event['playerTypes']:
        for pt in event['playerTypes']:
            
            player_type.append(pt['playerType'])
            name.append(event['name'])
            play_id.append(event['id'])
            cms_key.append(event['cmsKey'])
            code.append(event['code'])

play_type_df = pd.DataFrame({
    'name':name,
    'play_id':play_id,
    'cms_key':cms_key,
    'player_type':player_type,
    'code':code
})

play_type_df.to_csv('data/play-types/play_types.csv',index=False)