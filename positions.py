import numpy as np
import pandas as pd
import requests
import datetime

# capture today's date
today = str(datetime.datetime.now().strftime("%Y%m%d"))

# base url
url = 'https://statsapi.web.nhl.com/api/v1/'

# create new url and convert to json
r = requests.get(url + 'positions')
data = r.json()

positions_df = pd.DataFrame(data)

# export data to csv
positions_df.to_csv(f'data/position/position_{today}.csv', index=False)
positions_df.to_csv(f'data/position/position.csv', index=False)
