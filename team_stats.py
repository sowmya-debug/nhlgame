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

# create new url and convert to json
team_stats_id = []
team_stats_games_played = []
team_stats_wins = []
team_stats_losses = []
team_stats_ot = []
team_stats_pts = []
team_stats_pt_pctg = []
team_stats_goals_per_game = []
team_stats_goals_against_per_game = []
team_stats_ev_gga_ratio = []
team_stats_power_play_percentage = []
team_stats_power_play_goals = []
team_stats_power_play_goals_against = []
team_stats_power_play_opportunities = []
team_stats_penalty_kill_percentage = []
team_stats_shots_per_game = []
team_stats_shots_allowed = []
team_stats_win_score_first = []
team_stats_win_opp_score_first = []
team_stats_win_lead_first_per = []
team_stats_win_lead_second_per = []
team_stats_win_outshoot_opp = []
team_stats_win_outshot_by_opp = []
team_stats_face_offs_taken = []
team_stats_face_offs_won = []
team_stats_face_offs_lost = []
team_stats_face_off_win_percentage = []
team_stats_shooting_pctg = []
team_stats_save_pctg = []

for team in team_list:
    r = requests.get(url + f'teams/{team}/stats')
    data = r.json()
    
    data_path = data['stats'][0]['splits'][0]['stat']
    
    team_stats_id.append(team)
    team_stats_games_played.append(data_path['gamesPlayed'])
    team_stats_wins.append(data_path['wins'])
    team_stats_losses.append(data_path['losses'])
    team_stats_ot.append(data_path['ot'])
    team_stats_pts.append(data_path['pts'])
    team_stats_pt_pctg.append(data_path['ptPctg'])
    team_stats_goals_per_game.append(data_path['goalsPerGame'])
    team_stats_goals_against_per_game.append(data_path['goalsAgainstPerGame'])
    team_stats_ev_gga_ratio.append(data_path['evGGARatio'])
    team_stats_power_play_percentage.append(data_path['powerPlayPercentage'])
    team_stats_power_play_goals.append(data_path['powerPlayGoals'])
    team_stats_power_play_goals_against.append(data_path['powerPlayGoalsAgainst'])
    team_stats_power_play_opportunities.append(data_path['powerPlayOpportunities'])
    team_stats_penalty_kill_percentage.append(data_path['penaltyKillPercentage'])
    team_stats_shots_per_game.append(data_path['shotsPerGame'])
    team_stats_shots_allowed.append(data_path['shotsAllowed'])
    team_stats_win_score_first.append(data_path['winScoreFirst'])
    team_stats_win_opp_score_first.append(data_path['winOppScoreFirst'])
    team_stats_win_lead_first_per.append(data_path['winLeadFirstPer'])
    team_stats_win_lead_second_per.append(data_path['winLeadSecondPer'])
    team_stats_win_outshoot_opp.append(data_path['winOutshootOpp'])
    team_stats_win_outshot_by_opp.append(data_path['winOutshotByOpp'])
    team_stats_face_offs_taken.append(data_path['faceOffsTaken'])
    team_stats_face_offs_won.append(data_path['faceOffsWon'])
    team_stats_face_offs_lost.append(data_path['faceOffsLost'])
    team_stats_face_off_win_percentage.append(data_path['faceOffWinPercentage'])
    team_stats_shooting_pctg.append(data_path['shootingPctg'])
    team_stats_save_pctg.append(data_path['savePctg'])
                                
team_stats_df = pd.DataFrame(
{
    'team_id':team_stats_id,
    'games_played':team_stats_games_played,
    'wins':team_stats_wins,
 'losses':team_stats_losses,
 'ot':team_stats_ot ,
 'pts':team_stats_pts,
 'pt_pctg':team_stats_pt_pctg,
 'goals_per_game':team_stats_goals_per_game,
 'goals_against_per_game':team_stats_goals_against_per_game,
 'ev_gga_ratio':team_stats_ev_gga_ratio,
 'power_play_percentage':team_stats_power_play_percentage,
 'power_play_goals':team_stats_power_play_goals,
 'power_play_goals_against':team_stats_power_play_goals_against,
 'power_play_opportunities':team_stats_power_play_opportunities,
 'penalty_kill_percentage':team_stats_penalty_kill_percentage,
 'shots_per_game':team_stats_shots_per_game,
 'shots_allowed':team_stats_shots_allowed,
 'win_score_first':team_stats_win_score_first,
 'win_opp_score_first':team_stats_win_opp_score_first,
 'win_lead_first_per':team_stats_win_lead_first_per,
 'win_lead_second_per':team_stats_win_lead_second_per,
 'win_outshoot_opp':team_stats_win_outshoot_opp,
 'win_outshot_by_opp':team_stats_win_outshot_by_opp,
 'face_offs_taken':team_stats_win_outshot_by_opp,
 'face_offs_won':team_stats_face_offs_won,
 'face_offs_lost':team_stats_face_offs_lost,
 'face_off_win_percentage':team_stats_face_off_win_percentage,
 'shooting_pctg':team_stats_shooting_pctg,
 'save_pctg':team_stats_save_pctg
}


)

# export data to csv
team_stats_df.to_csv(f'data/team-stats/team_stats_{today}.csv',index=False)