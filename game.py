import const
import requests
from datetime import datetime, timedelta
import time

class Game(object):
	away_team = ""
	away_id = 0
	away_score = 0
	home_team = ""
	home_id = 0
	home_score = 0
	start_time = ""
	game_started = False
	current_period = ""
	time_in_period = ""
	game_finished = False
	game_api_link = ""

	def __init__(self, game_api_link):
		self.game_api_link = game_api_link
		url = '{0}{1}'.format(const.NHL_API_URL_BASE, game_api_link)

		max_retries = 5
		retries = 0
		response = None
		while retries < max_retries:
			try:
				response = requests.get(url)
			except (requests.exceptions.Timeout, requests.exceptions.TooManyRedirects, requests.exceptions.RequestException) as e:
				print("Failed to fetch {0} (attempt {1} of {2})".format(url, retries+1, max_retries))
				retries += 1
				time.sleep(10)
			else:
				break

		if response == None:
			print("Exiting.")
			exit(0)

		data = response.json()
		
		self.away_team = data['gameData']['teams']['away']['name']
		self.away_id = data['gameData']['teams']['away']['id']
		self.away_score = data['liveData']['linescore']['teams']['away']['goals']
		self.home_team = data['gameData']['teams']['home']['name']
		self.home_id = data['gameData']['teams']['home']['id']
		self.home_score = data['liveData']['linescore']['teams']['home']['goals']
		start_time = datetime.strptime(data['gameData']['datetime']['dateTime'], '%Y-%m-%dT%H:%M:%SZ')
		if time.localtime().tm_isdst == 1:
			timezone_offset = -4
		else:
			timezone_offset = -5
		start_time = start_time + timedelta(hours=timezone_offset)
		self.start_time = start_time.strftime('%-I:%M%p')


	def update(self):
		url = '{0}{1}'.format(const.NHL_API_URL_BASE, self.game_api_link)
		
		max_retries = 5
		retries = 0
		while retries < max_retries:
			try:
				response = requests.get(url)
			except (requests.exceptions.Timeout, requests.exceptions.TooManyRedirects, requests.exceptions.RequestException) as e:
				print("Failed to fetch {0} (attempt {1} of {2})".format(url, retries+1, max_retries))
				retries += 1
				time.sleep(10)
			else:
				break
		
		if response == None:
			print("Exiting.")
			exit(0)

		data = response.json()

		self.away_score = data['liveData']['linescore']['teams']['away']['goals']
		self.home_score = data['liveData']['linescore']['teams']['home']['goals']
		if data['liveData']['linescore']['currentPeriod'] > 0:
			self.game_started = True
			self.current_period = data['liveData']['linescore']['currentPeriodOrdinal']
			self.time_in_period = data['liveData']['linescore']['currentPeriodTimeRemaining']
		if data['gameData']['status']['abstractGameState'] == "Final":
			self.game_finished = True


	def to_string(self):
		string_to_return = self.away_team + " " + str(self.away_score) + " vs. " + self.home_team + " " + str(self.home_score) + " - "
		if self.game_finished == 1:
			string_to_return += "FINAL"
		elif self.game_started == 1:
			if self.current_period == "SO":
				string_to_return += self.current_period
			else:
				string_to_return += self.time_in_period + " " + self.current_period
		else:
			string_to_return += self.start_time

		return string_to_return