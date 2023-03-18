import pandas as pd
import numpy as np


# Dataset
matches = pd.read_csv('ipl-matches.csv')


def teamsAPI():
    teams = list(set(list(matches['Team1']) + list(matches['Team2'])))
    team_dict = {
        'teams': teams
    }
    return team_dict


def teamVteamAPI(team1, team2):
    valid_teams = list(set(list(matches['Team1']) + list(matches['Team2'])))
    if team1 in valid_teams and team2 in valid_teams:
        temp_df = matches[(matches['Team1'] == team1) & (matches['Team2'] == team2) | (
            matches['Team1'] == team2) & (matches['Team2'] == team1)]
        total_matches = temp_df.shape[0]
        matches_won_team1 = temp_df['WinningTeam'].value_counts()[team1]
        matches_won_team2 = temp_df['WinningTeam'].value_counts()[team2]
        draw = total_matches - (matches_won_team1 + matches_won_team2)
        response = {
            'total_matches': str(total_matches),
            team1: str(matches_won_team1),
            team2: str(matches_won_team2),
            'draw': str(draw)
        }
        return response
    else:
        return {'message': 'Invalid team name'}
