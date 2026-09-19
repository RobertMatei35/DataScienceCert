import pandas as pd 
from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder
import requests
import matplotlib.pyplot as plt

def one_dict(list_dict):
    keys = list_dict[0].keys()
    out_dict = {key:[] for key in keys}
    for dict_ in list_dict:
        for key, value in dict_.items():
            out_dict[key].append(value)

    return out_dict

nba_teams = teams.get_teams()
dict_nba_team = one_dict(nba_teams)
df_teams = pd.DataFrame(dict_nba_team)
#print(df_teams.head())

df_warriors = df_teams[df_teams['nickname'] == 'Warriors']
df_raptors = df_teams[df_teams['nickname'] == 'Raptors']

#Get the team identifier to use in other parts
id_warriors = df_warriors.iloc[0,0]
#id_warriors = df_warriors[['id']].values[0,0] - another way of accesing the id
id_raptors = df_raptors[['id']].values[0,0]

#Find the game of the warriors

gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=id_warriors)

games= gamefinder.get_data_frames()[0] # nu inteleg de ce aici trebuie pus [0]
print(games.head())

# filename = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%205/Labs/Golden_State.pkl"

# def download(url, filename):
#     response = requests.get(url)
#     if response.status_code == 200:
#         with open(filename, 'wb') as f:
#             f.write(response.content)

# download(filename, "Golden_State.pk1")

# file_name = "Golden_State.pk1"
# games = pd.read_pickle(file_name)
# games.head()

#Retrieve the games GSW vs Toronto, home and away
games_home = games[games['MATCHUP'] == 'GSW vs. TOR']
games_away = games[games['MATCHUP'] == 'GSW @ TOR']


#Get the average point difference at home and away
games_home['PLUS_MINUS'].mean()
games_away['PLUS_MINUS'].mean()

fig, ax = plt.subplots()

games_away.plot(x = "GAME_DATE", y= 'PLUS_MINUS', ax = ax)
games_home.plot(x = "GAME_DATE", y= 'PLUS_MINUS', ax = ax)
ax.legend(['away', 'home'])
plt.show()

