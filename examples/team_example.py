import sys
sys.path.append('../')

from fifa_py.team import Team

from fifa_py import _get_key
from pprint import pprint

api_key = _get_key()

t = Team(team_id=53, api_key=api_key, include='stats')
info = t.info()
print(info.T)
print(t.include().T)

info.to_csv('csv/teams.csv')