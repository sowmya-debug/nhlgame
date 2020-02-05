import numpy as np
import pandas as pd
import requests
import datetime

# capture today's date
today = str(datetime.datetime.now().strftime("%Y%m%d"))

# base url
url = 'https://statsapi.web.nhl.com/api/v1/'

# create new url and convert to json
r = requests.get(url + 'divisions')
data = r.json()

division_id = []
division_name = []
conference_id = []

# extract data from api
for div in data['divisions']:
    division_id.append(div['id'])
    division_name.append(div['name'])
    conference_id.append(div['conference']['id'])
    
# create dataframe
division_df = pd.DataFrame(
    {
        'id':division_id,
        'name':division_name,
        'conference_id':conference_id
    }

)

# export data to csv
division_df.to_csv(f'data/division/division_{today}.csv', index=False)
division_df.to_csv(f'data/division/division.csv', index=False)