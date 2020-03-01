import const

class Schedule(object):
	
	def __init__(self):
		self.game_list = []

	def add_game(self, game):
		self.game_list.append(game)


	def get_game_list(self):
		return self.game_list