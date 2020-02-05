import numpy as np
import pandas as pd
import requests
import datetime

# NEED TO CONVERT HEIGHT TO INCHES

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

# get roster
roster_person_id = []
    
for team in team_list:
    r = requests.get(url + f'teams/{team}/roster')
    data = r.json()
    
    for i in range(0,len(data['roster'])):
        roster_person_id.append(data['roster'][i]['person']['id'])

# create new url and convert to json
people_id = []
people_full_name = []
people_first_name = []
people_last_name = []
people_primary_number = []
people_birth_date = []
people_current_age = []
people_birth_city = []
people_birth_state_province = []
people_birth_country = []
people_nationality = []
people_height = []
people_weight = []
people_active = []
people_alternate_captain = []
people_captain = []
people_rookie = []
people_shoots = []
people_roster_status = []
people_current_team_id = []
people_primary_position_code = []

for person in roster_person_id:
        
    r = requests.get(url + f'people/{person}')
    data = r.json()


    for person in data['people']:
    
        people_id.append(person['id'])
        people_full_name.append(person['fullName'])
        people_first_name.append(person['firstName'])
        people_last_name.append(person['lastName'])
        people_birth_date.append(person['birthDate'])
        people_current_age.append(person['currentAge'])
        people_birth_city.append(person['birthCity'])
        people_birth_country.append(person['birthCountry'])
        people_nationality.append(person['nationality'])
        people_height.append(person['height'])
        people_weight.append(person['weight'])
        people_active.append(person['active'])
        people_alternate_captain.append(person['alternateCaptain'])
        people_captain.append(person['captain'])
        people_rookie.append(person['rookie'])
        people_shoots.append(person['shootsCatches'])
        people_roster_status.append(person['rosterStatus'])
        people_current_team_id.append(person['currentTeam']['id'])
        people_primary_position_code.append(person['primaryPosition']['code'])
        
        if 'birthStateProvince' in person.keys():
            people_birth_state_province.append(person['birthStateProvince'])
        else:
            people_birth_state_province.append('N/A')

        if 'primaryNumber' in person.keys():
            people_primary_number.append(person['primaryNumber'])
        else:
            people_primary_number.append('N/A')
    
    people_df = pd.DataFrame(
    {
        "id" : people_id,
        "fullName" : people_full_name,
        "firstName" : people_first_name,
        "lastName" : people_last_name,
        "primaryNumber" : people_primary_number,
        "birthDate" : people_birth_date,
        "currentAge" : people_current_age,
        "birthCity" : people_birth_city,
        "birthStateProvince" : people_birth_state_province,
        "birthCountry" : people_birth_country,
        "nationality" : people_nationality,
        "height" : people_height,
        "weight" : people_weight,
        "active" : people_active,
        "alternateCaptain" : people_alternate_captain,
        "captain" : people_captain,
        "rookie" : people_rookie,
        "shootsCatches" : people_shoots,
        "rosterStatus" : people_roster_status,
        "current_team_id": people_current_team_id,
        "primary_position_code": people_primary_position_code
    }


    )
  

# export data to csv
people_df.to_csv(f'data/people/people_{today}.csv', index=False)
people_df.to_csv(f'data/people/people.csv', index=False)