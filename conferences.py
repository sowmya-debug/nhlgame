import numpy as np
import pandas as pd
import requests
import datetime

# capture today's date
today = str(datetime.datetime.now().strftime("%Y%m%d"))

# base url
url = 'https://statsapi.web.nhl.com/api/v1/'

# create new url and convert to json
r = requests.get(url + 'conferences')
data = r.json()

conference_id = []
conference_name = []
conference_short_name = []

for conf in data['conferences']:
    conference_id.append(conf['id'])
    conference_name.append(conf['name'])
    conference_short_name.append(conf['shortName'])
    
conference_df = pd.DataFrame(
    {
        'id':conference_id,
        'name':conference_name,
        'short_name':conference_short_name
    }

)

# export data to csv
conference_df.to_csv(f'data/conference/conference_{today}.csv', index=False)
conference_df.to_csv(f'data/conference/conference.csv', index=False)