from functools import reduce
from operator import mul
from os import environ


def getSolutionPart1():
	sum = 0
	with open("day01/input.txt", "r") as file:
		for line in file.readlines():
			for character in line:
				if character.isnumeric():
					number_1 = character
					break

			for character in line[::-1]:
				if character.isnumeric():
					number_2 = character
					break

			sum += int(number_1+number_2)

	return sum


def getSolutionPart2():
	sum = 0
	written_numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
	with open("day01/input.txt", "r") as file:
		for line in file.readlines():
			number_1 = None
			number_2 = None
			for index, character in enumerate(line):
				if character.isnumeric():
					number_1 = character
				else:
					for written_number in written_numbers:
						if line[index:index+len(written_number)] == written_number:
							number_1 = str(written_numbers.index(written_number)+1)

				if number_1:
					break

			for index, character in enumerate(line[::-1]):
				if character.isnumeric():
					number_2 = character
				else:
					index = len(line)-index
					for written_number in written_numbers:
						if line[index-len(written_number):index] == written_number:
							number_2 = str(written_numbers.index(written_number)+1)

				if number_2:
					break

			sum += int(number_1+number_2)

	return sum


print('Python')
part = environ.get('part')

if part == 'part2':
    print(getSolutionPart2())
else:
    print(getSolutionPart1())





