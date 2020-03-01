from schedule import Schedule
from teamlist import TeamList
from team import Team
from game import Game
from rgbmatrix import graphics
import requests
import const
import time
from datetime import datetime, timedelta
from PIL import Image


class MainRenderer:
	def __init__(self, matrix):
		self.matrix = matrix
		self.canvas = self.matrix.CreateFrameCanvas()
	
	def render(self):
		font6x9 = graphics.Font()
		font6x9.LoadFont("6x9.bdf")
		font6x10 = graphics.Font()
		font6x10.LoadFont("6x10.bdf")
		teams = TeamList()
		

		
		while True:
			self.draw_retrieving_schedule(font6x10)

			todays_schedule = Schedule()

			url = '{0}/schedule'.format(const.NHL_API_URL)

			max_retries = 5
			retries = 0
			response = None
			while retries < max_retries:
				try:
					response = requests.get(url)
				except (requests.exceptions.Timeout, requests.exceptions.TooManyRedirects, requests.exceptions.RequestException) as e:
					print("Failed to fetch {0} (attempt {1} of {2})".format(url, retries+1, max_retries))
					print(e)
					retries += 1
					time.sleep(20)
				else:
					break

			if response == None:
				print("Exiting.")
				exit(0)

			data = response.json()
			
			if data['totalGames'] == 0:
				current_time = datetime.now()
				if current_time.hour < 12:
					schedule_date = datetime.strptime(str(current_time.year) + "-" + str(current_time.month) + "-" + str(current_time.day-1) + "-00:00", '%Y-%m-%d-%H:%M')
				else:
					schedule_date = datetime.strptime(str(current_time.year) + "-" + str(current_time.month) + "-" + str(current_time.day) + "-00:00", '%Y-%m-%d-%H:%M')

				reset_time = schedule_date + timedelta(hours=36)

				self.draw_offday(font6x9)
				
				while datetime.now() < reset_time:
					time.sleep(15)

			else:
				schedule_date = datetime.strptime(data['dates'][0]['date'] + "-00:00", '%Y-%m-%d-%H:%M')
				reset_time = schedule_date + timedelta(hours=36)
	
				for game in data['dates'][0]['games']:
					time.sleep(3)
					game_object = Game(game['link'])
					todays_schedule.add_game(game_object)
					print(game_object.to_string())

				game_list = todays_schedule.get_game_list()

				while datetime.now() < reset_time:
					print("Now: " + str(datetime.now()))
					print("Reset @ " + str(reset_time))
					print("Continue displaying scores?                 " + str(datetime.now() < reset_time))
					for game in game_list:
						game.update()

						for x in range(10):
							graphics.DrawLine(self.matrix, 0, 22+x, self.matrix.width, 22+x, graphics.Color(0, 0, 0))

						away_team = teams.get_team(game.away_id)
						home_team = teams.get_team(game.home_id)

						for x in range(11):
							graphics.DrawLine(self.matrix, 0, x, self.matrix.width, x, away_team.color)
							graphics.DrawLine(self.matrix, 0, x+11, self.matrix.width, x+11, home_team.color)

						graphics.DrawText(self.matrix, font6x10, 3, 9, away_team.text_color, away_team.abbreviation)
						graphics.DrawText(self.matrix, font6x10, 3, 9+11, home_team.text_color, home_team.abbreviation)
				
						if game.game_started == True:
							if game.away_score < 10:
								graphics.DrawText(self.matrix, font6x10, self.matrix.width - 7, 9, away_team.text_color, str(game.away_score))
							else:
								graphics.DrawText(self.matrix, font6x10, self.matrix.width - 13, 9, away_team.text_color, str(game.away_score))
				
							if game.home_score < 10:
								graphics.DrawText(self.matrix, font6x10, self.matrix.width - 7, 9+11, home_team.text_color, str(game.home_score))
							else:
								graphics.DrawText(self.matrix, font6x10, self.matrix.width - 13, 9+11, home_team.text_color, str(game.home_score))

						if game.game_started == False:
							graphics.DrawText(self.matrix, font6x9, 2, 8+22, graphics.Color(255, 255, 255), game.start_time)

						elif game.game_finished == True:
							final_text = "Final"
							if game.current_period == "OT" or game.current_period == "SO":
								final_text += " " + game.current_period
							graphics.DrawText(self.matrix, font6x9, 2, 8+22, graphics.Color(255, 255, 255), final_text)
				
						else:
							if game.current_period == "SO":
								graphics.DrawText(self.matrix, font6x9, 2, 8+22, graphics.Color(255, 255, 255), game.current_period)
							else:
								graphics.DrawText(self.matrix, font6x9, 2, 8+22, graphics.Color(255, 255, 255), game.time_in_period + " " + game.current_period)

						time.sleep(5)
					

	def draw_retrieving_schedule(self, font):
		for x in range(self.matrix.height):
			graphics.DrawLine(self.matrix, 0, x, self.matrix.width, x, graphics.Color(0, 0, 0))
		graphics.DrawText(self.matrix, font, 3, 10, graphics.Color(255, 255, 255), "Retrieving")
		graphics.DrawText(self.matrix, font, 3, 20, graphics.Color(255, 255, 255), "today's")
		graphics.DrawText(self.matrix, font, 3, 30, graphics.Color(255, 255, 255), "schedule.")

	def draw_offday(self, font):
		for x in range(self.matrix.height):
			graphics.DrawLine(self.matrix, 0, x, self.matrix.width, x, graphics.Color(0, 0, 0))
		nhl_logo_img = Image.open("nhl_logo.png")
		nhl_logo_img.thumbnail((self.matrix.height, self.matrix.height), Image.ANTIALIAS)
		self.matrix.SetImage(nhl_logo_img.convert('RGB'))
		graphics.DrawText(self.matrix, font, 40, 10, graphics.Color(255, 255, 255), "No")
		graphics.DrawText(self.matrix, font, 31, 17, graphics.Color(255, 255, 255), "games")
		graphics.DrawText(self.matrix, font, 40, 26, graphics.Color(255, 255, 255), ":(")