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

# get roster
roster_person_id = []
    
for team in team_list:
    r = requests.get(url + f'teams/{team}/roster')
    data = r.json()
    
    for i in range(0,len(data['roster'])):
        
        print(i)

        roster_person_id.append(data['roster'][i]['person']['id'])

# get list of goalies and non-goalies
# need a better way to get this
players = pd.read_csv('data/people/people.csv')
non_goalie = players[players['primary_position_code'] != 'G'].id
roster_person_non_goalie = list(non_goalie)

people_stats_id = []
people_stats_timeOnIce = []
people_stats_assists = []
people_stats_goals = []
people_stats_pim = []
people_stats_shots = []
people_stats_games = []
people_stats_hits = []
people_stats_powerPlayGoals = []
people_stats_powerPlayPoints = []
people_stats_powerPlayTimeOnIce = []
people_stats_evenTimeOnIce = []
people_stats_penaltyMinutes = []
people_stats_faceOffPct = []
people_stats_shotPct = []
people_stats_gameWinningGoals = []
people_stats_overTimeGoals = []
people_stats_shortHandedGoals = []
people_stats_shortHandedPoints = []
people_stats_shortHandedTimeOnIce = []
people_stats_blocked = []
people_stats_plusMinus = []
people_stats_points = []
people_stats_shifts = []
people_stats_timeOnIcePerGame = []
people_stats_evenTimeOnIcePerGame = []
people_stats_shortHandedTimeOnIcePerGame = []
people_stats_powerPlayTimeOnIcePerGame = []

for person in roster_person_non_goalie:
            
    r = requests.get(url + f'people/{person}/stats?stats=statsSingleSeason')
    data = r.json()
    
    if data['stats'][0]['splits']:
        
        data_path = data['stats'][0]['splits'][0]['stat']
        
        people_stats_id.append(person)
        people_stats_timeOnIce.append(data_path['timeOnIce'])
        people_stats_assists.append(data_path['assists'])
        people_stats_goals.append(data_path['goals'])
        people_stats_pim.append(data_path['pim'])
        people_stats_shots.append(data_path['shots'])
        people_stats_games.append(data_path['games'])
        people_stats_hits.append(data_path['hits'])
        people_stats_powerPlayGoals.append(data_path['powerPlayGoals'])
        people_stats_powerPlayPoints.append(data_path['powerPlayPoints'])
        people_stats_powerPlayTimeOnIce.append(data_path['powerPlayTimeOnIce'])
        people_stats_evenTimeOnIce.append(data_path['evenTimeOnIce'])
        people_stats_penaltyMinutes.append(data_path['penaltyMinutes'])
        people_stats_faceOffPct.append(data_path['faceOffPct'])
        people_stats_shotPct.append(data_path['shotPct'])
        people_stats_gameWinningGoals.append(data_path['gameWinningGoals'])
        people_stats_overTimeGoals.append(data_path['overTimeGoals'])
        people_stats_shortHandedGoals.append(data_path['shortHandedGoals'])
        people_stats_shortHandedPoints.append(data_path['shortHandedPoints'])
        people_stats_shortHandedTimeOnIce.append(data_path['shortHandedTimeOnIce'])
        people_stats_blocked.append(data_path['blocked'])
        people_stats_plusMinus.append(data_path['plusMinus'])
        people_stats_points.append(data_path['points'])
        people_stats_shifts.append(data_path['shifts'])
        people_stats_timeOnIcePerGame.append(data_path['timeOnIcePerGame'])
        people_stats_evenTimeOnIcePerGame.append(data_path['evenTimeOnIcePerGame'])
        people_stats_shortHandedTimeOnIcePerGame.append(data_path['shortHandedTimeOnIcePerGame'])
        people_stats_powerPlayTimeOnIcePerGame.append(data_path['powerPlayTimeOnIcePerGame'])
    else:
        people_stats_id.append(person)
        people_stats_timeOnIce.append('N/A')
        people_stats_assists.append('N/A')
        people_stats_goals.append('N/A')
        people_stats_pim.append('N/A')
        people_stats_shots.append('N/A')
        people_stats_games.append('N/A')
        people_stats_hits.append('N/A')
        people_stats_powerPlayGoals.append('N/A')
        people_stats_powerPlayPoints.append('N/A')
        people_stats_powerPlayTimeOnIce.append('N/A')
        people_stats_evenTimeOnIce.append('N/A')
        people_stats_penaltyMinutes.append('N/A')
        people_stats_faceOffPct.append('N/A')
        people_stats_shotPct.append('N/A')
        people_stats_gameWinningGoals.append('N/A')
        people_stats_overTimeGoals.append('N/A')
        people_stats_shortHandedGoals.append('N/A')
        people_stats_shortHandedPoints.append('N/A')
        people_stats_shortHandedTimeOnIce.append('N/A')
        people_stats_blocked.append('N/A')
        people_stats_plusMinus.append('N/A')
        people_stats_points.append('N/A')
        people_stats_shifts.append('N/A')
        people_stats_timeOnIcePerGame.append('N/A')
        people_stats_evenTimeOnIcePerGame.append('N/A')
        people_stats_shortHandedTimeOnIcePerGame.append('N/A')
        people_stats_powerPlayTimeOnIcePerGame.append('N/A')

    
people_stats_df = pd.DataFrame(
{
    'id':people_stats_id,
    'timeOnIce':people_stats_timeOnIce, 
    'assists':people_stats_assists, 
    'goals':people_stats_goals, 
    'pim':people_stats_pim, 
    'shots':people_stats_shots, 
    'games':people_stats_games, 
    'hits':people_stats_hits, 
    'powerPlayGoals':people_stats_powerPlayGoals, 
    'powerPlayPoints':people_stats_powerPlayPoints, 
    'powerPlayTimeOnIce':people_stats_powerPlayTimeOnIce, 
    'evenTimeOnIce':people_stats_evenTimeOnIce, 
    'penaltyMinutes':people_stats_penaltyMinutes, 
    'faceOffPct':people_stats_faceOffPct, 
    'shotPct':people_stats_shotPct, 
    'gameWinningGoals':people_stats_gameWinningGoals, 
    'overTimeGoals':people_stats_overTimeGoals, 
    'shortHandedGoals':people_stats_shortHandedGoals, 
    'shortHandedPoints':people_stats_shortHandedPoints, 
    'shortHandedTimeOnIce':people_stats_shortHandedTimeOnIce, 
    'blocked':people_stats_blocked, 
    'plusMinus':people_stats_plusMinus, 
    'points':people_stats_points, 
    'shifts':people_stats_shifts, 
    'timeOnIcePerGame':people_stats_timeOnIcePerGame, 
    'evenTimeOnIcePerGame':people_stats_evenTimeOnIcePerGame, 
    'shortHandedTimeOnIcePerGame':people_stats_shortHandedTimeOnIce, 
    'powerPlayTimeOnIcePerGame':people_stats_powerPlayTimeOnIcePerGame
}
)

# export data to csv
people_stats_df.to_csv(f'data/player-stats/player_stats_{today}.csv',index=False)
people_stats_df.to_csv(f'data/player-stats/player_stats.csv',index=False)