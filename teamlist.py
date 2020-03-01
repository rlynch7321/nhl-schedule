from rgbmatrix import graphics
from team import Team

class TeamList(object):
	team_list = []
	
	def __init__(self):
		black = graphics.Color(0, 0, 0)
		white = graphics.Color(255, 255, 255)


		self.team_list.append(Team("NULL", "NULL", "NUL", graphics.Color(0, 0, 0), white))			#  0
		self.team_list.append(Team("New Jersey", "Devils", "NJD", graphics.Color(206, 17, 38), white))		#  1
		self.team_list.append(Team("New York", "Islanders", "NYI", graphics.Color(0, 83, 155), white))		#  2
		self.team_list.append(Team("New York", "Rangers", "NYR", graphics.Color(0, 56, 168), white))		#  3
		self.team_list.append(Team("Philadelphia", "Flyers", "PHI", graphics.Color(247, 73, 2), white))		#  4
		self.team_list.append(Team("Pittsburgh", "Penguins", "PIT", graphics.Color(252, 181, 20), black))	#  5
		self.team_list.append(Team("Boston", "Bruins", "BOS", graphics.Color(252, 181, 20), black))		#  6
		self.team_list.append(Team("Buffalo", "Sabres", "BUF", graphics.Color(0, 38, 84), white))		#  7
		self.team_list.append(Team("Montreal", "Canadiens", "MTL", graphics.Color(175, 30, 45), white))		#  8
		self.team_list.append(Team("Ottawa", "Senators", "OTT", graphics.Color(200, 16,46), white))		#  9
		self.team_list.append(Team("Toronto", "Maple Leafs", "TOR", graphics.Color(0, 62, 126), white))		# 10
		self.team_list.append(Team("NULL", "NULL", "NUL", graphics.Color(0, 0, 0), white))			# 11	# DEFUNCT
		self.team_list.append(Team("Carolina", "Hurricanes", "CAR", graphics.Color(226, 24, 54), white))	# 12
		self.team_list.append(Team("Florida", "Panthers", "FLA", graphics.Color(4, 30, 66), white))		# 13
		self.team_list.append(Team("Tampa Bay", "Lightning", "TBL", graphics.Color(0, 40, 104), white))		# 14
		self.team_list.append(Team("Washington", "Capitals", "WSH", graphics.Color(200, 16, 46), white))	# 15
		self.team_list.append(Team("Chicago", "Blackhawks", "CHI", graphics.Color(207, 10, 44), white))		# 16
		self.team_list.append(Team("Detroit", "Red Wings", "DET", graphics.Color(206, 17, 38), white))		# 17
		self.team_list.append(Team("Nashville", "Predators", "NSH", graphics.Color(255, 184, 28), black))	# 18
		self.team_list.append(Team("St. Louis", "Blues", "STL", graphics.Color(0, 47, 135), white))		# 19
		self.team_list.append(Team("Calgary", "Flames", "CGY", graphics.Color(200, 16, 46), white))		# 20
		self.team_list.append(Team("Colorado", "Avalanche", "COL", graphics.Color(111, 38, 61), white))		# 21
		self.team_list.append(Team("Edmonton", "Oilers", "EDM", graphics.Color(4, 30, 66), white))		# 22
		self.team_list.append(Team("Vancouver", "Canucks", "VAN", graphics.Color(0, 31, 91), white))		# 23
		self.team_list.append(Team("Anaheim", "Ducks", "ANA", graphics.Color(176, 152, 98), black))		# 24
		self.team_list.append(Team("Dallas", "Stars", "DAL", graphics.Color(0, 104, 71), white))		# 25
		self.team_list.append(Team("Los Angeles", "Kings", "LAK", graphics.Color(17, 17, 17), white))		# 26
		self.team_list.append(Team("NULL", "NULL", "NUL", graphics.Color(0, 0, 0), white))			# 27	# DEFUNCT
		self.team_list.append(Team("San Jose", "Sharks", "SJS", graphics.Color(0, 109, 117), white))		# 28
		self.team_list.append(Team("Columbus", "Blue Jackets", "CBJ", graphics.Color(0, 38, 84), white))	# 29
		self.team_list.append(Team("Minnesota", "Wild", "MIN", graphics.Color(2, 73, 48), white))		# 30
		self.team_list.append(Team("NULL", "NULL", "NUL", graphics.Color(0, 0, 0), white))			# 31	# DEFUNCT
		self.team_list.append(Team("NULL", "NULL", "NUL", graphics.Color(0, 0, 0), white))			# 32	# DEFUNCT
		self.team_list.append(Team("NULL", "NULL", "NUL", graphics.Color(0, 0, 0), white))			# 33	# DEFUNCT
		self.team_list.append(Team("NULL", "NULL", "NUL", graphics.Color(0, 0, 0), white))			# 34	# DEFUNCT
		self.team_list.append(Team("NULL", "NULL", "NUL", graphics.Color(0, 0, 0), white))			# 35	# DEFUNCT
		self.team_list.append(Team("NULL", "NULL", "NUL", graphics.Color(0, 0, 0), white))			# 36	# DEFUNCT
		self.team_list.append(Team("NULL", "NULL", "NUL", graphics.Color(0, 0, 0), white))			# 37	# DEFUNCT
		self.team_list.append(Team("NULL", "NULL", "NUL", graphics.Color(0, 0, 0), white))			# 38	# DEFUNCT
		self.team_list.append(Team("NULL", "NULL", "NUL", graphics.Color(0, 0, 0), white))			# 39	# DEFUNCT
		self.team_list.append(Team("NULL", "NULL", "NUL", graphics.Color(0, 0, 0), white))			# 40	# DEFUNCT
		self.team_list.append(Team("NULL", "NULL", "NUL", graphics.Color(0, 0, 0), white))			# 41	# DEFUNCT
		self.team_list.append(Team("NULL", "NULL", "NUL", graphics.Color(0, 0, 0), white))			# 42	# DEFUNCT
		self.team_list.append(Team("NULL", "NULL", "NUL", graphics.Color(0, 0, 0), white))			# 43	# DEFUNCT
		self.team_list.append(Team("NULL", "NULL", "NUL", graphics.Color(0, 0, 0), white))			# 44	# DEFUNCT
		self.team_list.append(Team("NULL", "NULL", "NUL", graphics.Color(0, 0, 0), white))			# 45	# DEFUNCT
		self.team_list.append(Team("NULL", "NULL", "NUL", graphics.Color(0, 0, 0), white))			# 46	# DEFUNCT
		self.team_list.append(Team("NULL", "NULL", "NUL", graphics.Color(0, 0, 0), white))			# 47	# DEFUNCT
		self.team_list.append(Team("NULL", "NULL", "NUL", graphics.Color(0, 0, 0), white))			# 48	# DEFUNCT
		self.team_list.append(Team("NULL", "NULL", "NUL", graphics.Color(0, 0, 0), white))			# 49	# DEFUNCT
		self.team_list.append(Team("NULL", "NULL", "NUL", graphics.Color(0, 0, 0), white))			# 50	# DEFUNCT
		self.team_list.append(Team("NULL", "NULL", "NUL", graphics.Color(0, 0, 0), white))			# 51	# DEFUNCT
		self.team_list.append(Team("Winnipeg", "Jets", "WPG", graphics.Color(4, 30, 66), white))		# 52
		self.team_list.append(Team("Arizona", "Coyotes", "ARI", graphics.Color(140, 38, 51), white))		# 53
		self.team_list.append(Team("Vegas", "G. Knights", "VGK", graphics.Color(176, 152, 98), black))		# 54
		self.team_list.append(Team("Seattle", "Unknown", "SEA", graphics.Color(0, 0, 0), white))		# 55	# INACTIVE

	def get_team(self, id):
		return self.team_list[id]