import requests
from datetime import datetime, timedelta
import const
import time

NHL_API_URL = "http://statsapi.web.nhl.com/api/v1/"
NHL_API_URL_BASE = "http://statsapi.web.nhl.com"

def main():
	print("Running the program...")
	schedule = get_todays_schedule()

	for game in schedule:
		game_info = str(game[0]) + " " + str(game[1]) + " - " + game[2] + " " + str(game[3])
		game_info += " - " + game[4]
		print(game_info)

def get_teams():

	url = '{0}/teams'.format(NHL_API_URL)
	response = requests.get(url)
	results = response.json()
	teams = []
	
	for team in results['teams']:
		teams.append(team['locationName'] + " " + team['franchise']['teamName'])
	
	return teams

def get_todays_schedule():
	url = '{0}/schedule'.format(NHL_API_URL)
	print("Requesting Schedule...")
	response = requests.get(url)
	results = response.json()
	schedule = []

	for game in results['dates'][0]['games']:
		game_details = []
		game_details.append(game['teams']['away']['team']['name'])		#append HOME_TEAM
		game_details.append(game['teams']['away']['score'])			#append HOME_SCORE
		game_details.append(game['teams']['home']['team']['name'])		#append AWAY_TEAM
		game_details.append(game['teams']['home']['score'])			#append AWAY_SCORE
		
		game_link = game['link']
		url = '{0}{1}'.format(NHL_API_URL_BASE, game_link)
		print(url)
		
		time.sleep(3)
		print("Requesting game data...")
		response = requests.get(url)
		results = response.json()
		
		game_time = datetime.strptime(results['gameData']['datetime']['dateTime'], '%Y-%m-%dT%H:%M:%SZ')
		if time.localtime().tm_isdst == 1:
			offset = 4
		else:
			offset = 5
		game_time = game_time + timedelta(hours=-offset)
			
		game_time = game_time.strftime('%I:%M%p')
		game_details.append(game_time)

		schedule.append(game_details)
	
	return schedule







if __name__ == '__main__':
	main()
