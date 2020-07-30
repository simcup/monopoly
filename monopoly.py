# -*- coding:utf-8 -*-
import random
from enum import Enum

#once upon a blue moon, well not exactly at night, and the stellar
#object visible wasn't apearing blue, anyway i saw a reddit post
#visualizing the probabilities to hit each field in a monopoly 
#game board and decided i want to implement that myself.
# so with no close look at the code on the origial site i started this
#if you ever come across this code and want to use it,
#do with it what you want, execpt killing and/or opress people

#feldnamen:

	


class Fieldtype(Enum):
	STREET		= 1
	START 		= 3
	OTHER 		= 3
	GOTOJAIL 	= 4
	JAIL		= 5
	COMMUNITY 	= 6
	EVENT 		= 7
	

class Dice:

	firstdie = 0
	seconddie = 0

	def roll(self):
		self.firstdie = random.randint(1,6)
		self.seconddie = random.randint(1,6)

	def getval(self):
		return (self.firstdie+self.seconddie)

	def isdouble(self):
		return self.firstdie == self.seconddie

	def __init__(self):
		self.roll()

class Player:

	
	color = ""
	currentfield = 0
	isinjail = False
	injailsince = 0
	doublesrolled = 0

	def __init__(self, color):
		self.color = color

class Field:
		
        name = ""
        typeoffield = 0
        numberoftimesbeenvisited = 0

	def __init__(self, data):
		self.name = data[0]

		self.typeoffield = data[1]
	
#        def haseffect(self):
#            if self.typeoffield  in [Fieldtype.COMMUNITY, Fieldtype.EVENT, Fieldtype.GOTOJAIL]:
#                return True
#            return False



class ComunityCardDeck:
	#poc
	cards = [
		"",
		"blub",
		"peng"
		]

	def drawcard(self):
		val = self.cards.pop(0)
		self.cards.append(val)
		return val
		

class Board:

	streets = [
	('Los', Fieldtype.START ),
	('Badstraße', Fieldtype.STREET),
	('Gemeinschaftsfeld', Fieldtype.COMMUNITY),
	('Turmstraße', Fieldtype.STREET),
	('Einkommenssteuer', Fieldtype.OTHER),
	('Südbahnhof', Fieldtype.STREET),
	('Chausseestraße', Fieldtype.STREET),
	('Ereignisfeld', Fieldtype.EVENT),
	('Elisenstraße', Fieldtype.STREET),
	('Poststraße', Fieldtype.STREET),
	('Gefängnis', Fieldtype.JAIL),
	('Seestraße', Fieldtype.STREET),
	('Elektrizitätswerk', Fieldtype.STREET),
	('Hafenstraße', Fieldtype.STREET ),
	('Neue Straße', Fieldtype.STREET),
	('Westbahnhof', Fieldtype.STREET),
	('Münchner Straße', Fieldtype.STREET),
	('Gemeinschaftsfeld', Fieldtype.COMMUNITY),
	('Wiener Straße', Fieldtype.STREET),
	('Berliner Straße', Fieldtype.STREET),
	('Frei Parken', Fieldtype.OTHER),
	('Theaterstraße', Fieldtype.STREET),
	('Ereignisfeld', Fieldtype.EVENT),
	('Museumstraße', Fieldtype.STREET),
	('Opernplatz', Fieldtype.STREET),
	('Nordbahnhof', Fieldtype.STREET),
	('Lessingstraße', Fieldtype.STREET),
	('Schillerstraße', Fieldtype.STREET),
	('Wasserwerk', Fieldtype.STREET),
	('Goethestraße', Fieldtype.STREET),
	('Gehen Sie in das Gefängnis', Fieldtype.GOTOJAIL),
	('Rathausplatz', Fieldtype.STREET),
	('Hauptstraße', Fieldtype.STREET),
        ('Gemeinschaftsfeld', Fieldtype.COMMUNITY),
	('Bahnhofsstraße', Fieldtype.STREET),
	('Hauptbahnhof', Fieldtype.STREET),
	('Ereignisfeld', Fieldtype.EVENT),
	('Parkstraße', Fieldtype.STREET),
	('Zusatzsteuer', Fieldtype.OTHER),
	('Schloßallee', Fieldtype.STREET)
	]
	
	playercolors = [
		"red",
		"yellow",
		"green",
		"blue",
		"black",
		"white",
		"pink",
		"brown"
		]
	fields = []
	players = []
	dice = Dice()

	def __init__(self, numberofplayers = 4):
		if not 3 <= numberofplayers <= 8:
			exit("kann nicht mit weniger als 3 oder mehr als 8 spielern spielen")
		for player in range(numberofplayers):
			self.players.append(Player(self.playercolors[player]))
		for street in self.streets:
			self.fields.append(Field(street))

	def play(self, numberofrounds = 10000):
		for i in range(numberofrounds):
			for player in self.players:
                                turnended = False
                                while not turnended:
                                    turnended = True
                                    doubles = 0
                                    self.dice.roll()
                                    
                                    self.dice.isdouble():
                                        doubles +=1
                                        tuenended = False
                                    if doubles > 2:
                                                    player.isinjail = not player.isinjail
                                                    doubles = 0
                                                    turnended = True
                                    if player.isinjail:
                                            player.currentfield = 9
                                            break

                                    player.currentfield = (player.currentfield+self.dice.getval()) % len(self.fields)

                                    self.fields[player.currentfield].numberoftimesbeenvisited += 1
                                    fieldtype = self.fields[player.currentfield].typeoffield
                                    if fieldtype == Fieldtype.GOTOJAIL:
                                        player.currentfield = 9
                                        player.isinjail = True
                                


	def end(self):
		for field in self.fields:
                    print("field: {}, visited: {}".format(field.name, field.numberoftimesbeenvisited))
		
		
if __name__ == "__main__":
	game = Board()
	game.play()
	game.end()
	
