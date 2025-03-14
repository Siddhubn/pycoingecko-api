from pycoingecko import CoinGeckoAPI
cg=CoinGeckoAPI()
bitcoin_data=cg.get_coin_market_chart_by_id(id="bitcoin",vs_currency='usd',days=30)
import pandas as pd
data=pd.DataFrame(bitcoin_data['prices'],columns=['Timestamp','Price'])
data['Date']=pd.to_datetime(data['Timestamp'],unit='ms')
print(data['Date'])
candlestick_data=data.groupby(data.Date.dt.data).agg({'Price':['min','max','first','last']})
print(candlestick_data) 
from nba_api.stats.static import teams
import matplotlib.pyplot as plt

def json_to_dict(json):
    ids=json[0].keys()
    dict={id:[] for id in ids}
    for objects in json:
        for key,value in objects.items():
            dict[key].append(value)
    return dict

nba_teams=teams.get_teams()
import pandas as pd
dict_nba_teams=json_to_dict(nba_teams)
df_teams=pd.DataFrame(dict_nba_teams)
print(df_teams.head())

df_warriors=df_teams[df_teams['nickname']=='Warriors']

id_warriors=df_warriors[[id]].values[0][0]

from nba_api.stats.endpoints import leaguegamefinder
gamefinder=leaguegamefinder.LeagueGameFinder(team_id_nullable=id_warriors)
gamefinder.get_json()
games=gamefinder.get_data_frames()[0]
games.head()

import matplotlib.pyplot as plt
fig,ax=plt.subplots()
games_away.plot(x='Games Data',y='Plus_Minus',ax=ax)
games_home.plot(x='Games Data')