import numpy as np
import pandas as pd
import requests
from datetime import date, timedelta, datetime

# capture today's date
today = str(datetime.now().strftime('%Y%m%d'))

# base url
url = 'https://statsapi.web.nhl.com/api/v1/'

# create new url and convert to json
r = requests.get(url + 'teams')
data = r.json()

team_id = []
team_name = []
team_venue_name = []
team_abbreviation = []
team_short_name = []
team_location_name = []
team_year_founded = []
team_division_id = []
team_conference_id = []
team_franchise_id = []

for team in data['teams']:
    
    team_id.append(team['id'])
    team_name.append(team['name'])
    team_venue_name.append(team['venue']['name'])
    team_abbreviation.append(team['abbreviation'])
    team_short_name.append(team['teamName'])
    team_location_name.append(team['locationName'])
    team_year_founded.append(team['firstYearOfPlay'])
    team_division_id.append(team['division']['id'])
    team_conference_id.append(team['conference']['id'])
    team_franchise_id.append(team['franchiseId'])
    
team_df = pd.DataFrame(
    {
        'id':team_id,
        'name':team_name,
        'venue':team_venue_name,
        'abbreviation':team_abbreviation,
        'short_name':team_short_name,
        'location':team_location_name,
        'year_founded':team_year_founded,
        'team_division':team_division_id,
        'team_conference':team_conference_id,
        'franchise_id':team_franchise_id
    }

)

# export data to csv
team_df.to_csv(f'data/team/team_{today}.csv', index=False)
team_df.to_csv(f'data/team/team.csv', index=False)