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
        roster_person_id.append(data['roster'][i]['person']['id'])

# get list of goalies and non-goalies
# need a better way to get this
players = pd.read_csv('data/people/people.csv')
non_goalie = players[players['primary_position_code'] != 'G'].id
roster_person_non_goalie = list(non_goalie)

skater_stats_vs_id = []
skater_stats_vs_opponent_id = []
skater_stats_vs_timeOnIce = []
skater_stats_vs_assists = []
skater_stats_vs_goals = []
skater_stats_vs_pim = []
skater_stats_vs_shots = []
skater_stats_vs_games = []
skater_stats_vs_hits = []
skater_stats_vs_powerPlayGoals = []
skater_stats_vs_powerPlayPoints = []
skater_stats_vs_powerPlayTimeOnIce = []
skater_stats_vs_evenTimeOnIce = []
skater_stats_vs_penaltyMinutes = []
skater_stats_vs_faceOffPct = []
skater_stats_vs_faceOffWins = []
skater_stats_vs_shotPct = []
skater_stats_vs_gameWinningGoals = []
skater_stats_vs_overTimeGoals = []
skater_stats_vs_shortHandedGoals = []
skater_stats_vs_shortHandedPoints = []
skater_stats_vs_shortHandedTimeOnIce = []
skater_stats_vs_blocked = []
skater_stats_vs_plusMinus = []
skater_stats_vs_points = []
skater_stats_vs_shifts = []
skater_stats_vs_timeOnIcePerGame = []
skater_stats_vs_evenTimeOnIcePerGame = []
skater_stats_vs_shortHandedTimeOnIcePerGame = []
skater_stats_vs_powerPlayTimeOnIcePerGame = []

for person in roster_person_non_goalie:
            
    r = requests.get(url + f'people/{person}/stats?stats=vsTeam')
    data = r.json()

    print(person)

    for team in data['stats'][0]['splits']:
        
        skater_stats_vs_id.append(person)
        skater_stats_vs_opponent_id.append(team['opponent']['id'])
        skater_stats_vs_timeOnIce.append(team['stat']['timeOnIce'])
        skater_stats_vs_assists.append(team['stat']['assists'])
        skater_stats_vs_goals.append(team['stat']['goals'])
        skater_stats_vs_pim.append(team['stat']['pim'])
        skater_stats_vs_shots.append(team['stat']['shots'])
        skater_stats_vs_games.append(team['stat']['games'])
        skater_stats_vs_hits.append(team['stat']['hits'])
        skater_stats_vs_powerPlayGoals.append(team['stat']['powerPlayGoals'])
        skater_stats_vs_powerPlayPoints.append(team['stat']['powerPlayPoints'])
        skater_stats_vs_powerPlayTimeOnIce.append(team['stat']['powerPlayTimeOnIce'])
        skater_stats_vs_evenTimeOnIce.append(team['stat']['evenTimeOnIce'])
        skater_stats_vs_penaltyMinutes.append(team['stat']['penaltyMinutes'])
        skater_stats_vs_faceOffWins.append(team['stat']['faceOffWins'])
        skater_stats_vs_gameWinningGoals.append(team['stat']['gameWinningGoals'])
        skater_stats_vs_overTimeGoals.append(team['stat']['overTimeGoals'])
        skater_stats_vs_shortHandedGoals.append(team['stat']['shortHandedGoals'])
        skater_stats_vs_shortHandedPoints.append(team['stat']['shortHandedPoints'])
        skater_stats_vs_shortHandedTimeOnIce.append(team['stat']['shortHandedTimeOnIce'])
        skater_stats_vs_blocked.append(team['stat']['blocked'])
        skater_stats_vs_plusMinus.append(team['stat']['plusMinus'])
        skater_stats_vs_points.append(team['stat']['points'])
        skater_stats_vs_shifts.append(team['stat']['shifts'])
        skater_stats_vs_timeOnIcePerGame.append(team['stat']['timeOnIcePerGame'])
        skater_stats_vs_evenTimeOnIcePerGame.append(team['stat']['evenTimeOnIcePerGame'])
        skater_stats_vs_shortHandedTimeOnIcePerGame.append(team['stat']['shortHandedTimeOnIcePerGame'])
        skater_stats_vs_powerPlayTimeOnIcePerGame.append(team['stat']['powerPlayTimeOnIcePerGame'])

        if 'faceOffPct' in team.keys():
            skater_stats_vs_faceOffPct.append(team['stat']['faceOffPct'])
        else:
            skater_stats_vs_faceOffPct.append('N/A')

        if 'shotPct' in team.keys():
            skater_stats_vs_shotPct.append(team['stat']['shotPct'])
        else:
            skater_stats_vs_shotPct.append('N/A')

    else:
        skater_stats_vs_id.append(person)
        skater_stats_vs_opponent_id.append(team['opponent']['id'])
        skater_stats_vs_timeOnIce.append('N/A')
        skater_stats_vs_assists.append('N/A')
        skater_stats_vs_goals.append('N/A')
        skater_stats_vs_pim.append('N/A')
        skater_stats_vs_shots.append('N/A')
        skater_stats_vs_games.append('N/A')
        skater_stats_vs_hits.append('N/A')
        skater_stats_vs_powerPlayGoals.append('N/A')
        skater_stats_vs_powerPlayPoints.append('N/A')
        skater_stats_vs_powerPlayTimeOnIce.append('N/A')
        skater_stats_vs_evenTimeOnIce.append('N/A')
        skater_stats_vs_penaltyMinutes.append('N/A')
        skater_stats_vs_faceOffPct.append('N/A')
        skater_stats_vs_shotPct.append('N/A')
        skater_stats_vs_gameWinningGoals.append('N/A')
        skater_stats_vs_overTimeGoals.append('N/A')
        skater_stats_vs_shortHandedGoals.append('N/A')
        skater_stats_vs_shortHandedPoints.append('N/A')
        skater_stats_vs_shortHandedTimeOnIce.append('N/A')
        skater_stats_vs_blocked.append('N/A')
        skater_stats_vs_plusMinus.append('N/A')
        skater_stats_vs_points.append('N/A')
        skater_stats_vs_shifts.append('N/A')
        skater_stats_vs_timeOnIcePerGame.append('N/A')
        skater_stats_vs_evenTimeOnIcePerGame.append('N/A')
        skater_stats_vs_shortHandedTimeOnIcePerGame.append('N/A')
        skater_stats_vs_powerPlayTimeOnIcePerGame.append('N/A')

    
skater_stats_vs_df = pd.DataFrame(
{
    'id':skater_stats_vs_id,
    'opponentId':skater_stats_vs_opponent_id,
    'timeOnIce':skater_stats_vs_timeOnIce, 
    'assists':skater_stats_vs_assists, 
    'goals':skater_stats_vs_goals, 
    'pim':skater_stats_vs_pim, 
    'shots':skater_stats_vs_shots, 
    'games':skater_stats_vs_games, 
    'hits':skater_stats_vs_hits, 
    'powerPlayGoals':skater_stats_vs_powerPlayGoals, 
    'powerPlayPoints':skater_stats_vs_powerPlayPoints, 
    'powerPlayTimeOnIce':skater_stats_vs_powerPlayTimeOnIce, 
    'evenTimeOnIce':skater_stats_vs_evenTimeOnIce, 
    'penaltyMinutes':skater_stats_vs_penaltyMinutes, 
    'faceOffPct':skater_stats_vs_faceOffPct, 
    'shotPct':skater_stats_vs_shotPct, 
    'gameWinningGoals':skater_stats_vs_gameWinningGoals, 
    'overTimeGoals':skater_stats_vs_overTimeGoals, 
    'shortHandedGoals':skater_stats_vs_shortHandedGoals, 
    'shortHandedPoints':skater_stats_vs_shortHandedPoints, 
    'shortHandedTimeOnIce':skater_stats_vs_shortHandedTimeOnIce, 
    'blocked':skater_stats_vs_blocked, 
    'plusMinus':skater_stats_vs_plusMinus, 
    'points':skater_stats_vs_points, 
    'shifts':skater_stats_vs_shifts, 
    'timeOnIcePerGame':skater_stats_vs_timeOnIcePerGame, 
    'evenTimeOnIcePerGame':skater_stats_vs_evenTimeOnIcePerGame, 
    'shortHandedTimeOnIcePerGame':skater_stats_vs_shortHandedTimeOnIce, 
    'powerPlayTimeOnIcePerGame':skater_stats_vs_powerPlayTimeOnIcePerGame
}
)

# export data to csv
skater_stats_vs_df.to_csv(f'data/skater-stats-vs-team/skater_stats_vs_team_{today}.csv',index=False)
skater_stats_vs_df.to_csv(f'data/skater-stats-vs-team/skater_stats_vs_team.csv',index=False)