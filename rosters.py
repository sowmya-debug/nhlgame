import numpy as np
import pandas as pd
import requests
import datetime

# capture today's date
today = str(datetime.datetime.now().strftime("%Y%m%d"))

# base url
url = 'https://statsapi.web.nhl.com/api/v1/'

# get teams list
r = requests.get(url + 'teams')
data = r.json()

team_list = []
for team in data['teams']:
    team_list.append(team['id'])

team_list

# create new url and convert to json
roster_team_id = []
roster_person_id = []
roster_person_full_name = []
    
for team in team_list:
    r = requests.get(url + f'teams/{team}/roster')
    data = r.json()
    
    for i in range(0,len(data['roster'])):
        roster_team_id.append(team)
        roster_person_id.append(data['roster'][i]['person']['id'])
        roster_person_full_name.append(data['roster'][i]['person']['fullName'])
    
roster_df = pd.DataFrame(
{
    'team_id':roster_team_id,
    'id':roster_person_id,
    'full_name':roster_person_full_name
})

# export data to csv
roster_df.to_csv(f'data/roster/roster_{today}.csv',index=False)
roster_df.to_csv(f'data/roster/roster.csv',index=False)