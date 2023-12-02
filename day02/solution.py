



from functools import reduce
from operator import mul
from os import environ


def getSolutionPart1():
	match = {"red": 12, "green": 13, "blue": 14}
	sum = 0

	with open("day02/input.txt", "r") as file:
		for line in file.readlines():
			impossible = False

			game_id, games = line.split(": ")
			for game in games.split("; "):
				for draw in game.split(", "):
					number, color = draw.split(" ")

					if int(number) > match[color.replace("\n", "")]:
						impossible = True
			
			if not impossible:
				sum += int(game_id.split(" ")[1])

	return sum


def getSolutionPart2():
	sum = 0

	with open("day02/input.txt", "r") as file:
		for line in file.readlines():
			colors = {"red": 0, "green": 0, "blue": 0}

			game_id, games = line.split(": ")
			for game in games.split("; "):
				for draw in game.split(", "):
					number, color = draw.split(" ")
					number = int(number)
					color = color.replace("\n", "")

					if colors[color] < number:
						colors[color] = number
					
			sum += colors["red"] * colors["green"] * colors["blue"]

	return sum


print('Python')
part = environ.get('part')

if part == 'part2':
    print(getSolutionPart2())
else:
    print(getSolutionPart1())





