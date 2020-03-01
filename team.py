
class Team(object):
	location = ""
	name = ""
	abbreviation = ""
	color = ""

	def __init__(self, location, name, abbreviation, color, text_color):
		self.location = location
		self.name = name
		self.abbreviation = abbreviation
		self.color = color
		self.text_color = text_color