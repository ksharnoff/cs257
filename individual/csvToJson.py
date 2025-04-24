'''
csvToJson.py
Kezia Sharnoff
April 24 2025

Simple program for converting all of the data we're interested to JSON 
and printing it out. Used for making the examples in the API Design
Assignment. 

Base of the code copied from my cli.py assignment: 
https://github.com/ksharnoff/cs257/blob/main/individual/cli.py
'''
import csv 
import json


# all of the columns at their correct indicies (0 to 29)
columns = ("name", "landmass", "zone", "area", "population", "language",
		   "religion", "bars", "stripes", "colours", "red", "green", "blue",
		   "gold", "white", "black", "orange", "mainhue", "circles", 
		   "crosses", "saltires", "quarters", "sunstars", "crescent", 
		   "triangle", "inanimateImage", "animateImage", "text", "topleft",
		   "topright")

'''
Creates the list of dictionaries for all the countries with the data
explicitly labeled. 
Used the following source for how to get the index and value while
looping: 
https://www.geeksforgeeks.org/python-accessing-index-and-value-in-list/
'''
def fetch_countries():
	countries = []

	# hard coded where to find the data: 
	with open('../data/flags.csv') as f:
		reader = csv.reader(f)
		# each row represents a country
		for country_row in reader:
			new_dict = {}
			new_dict["name"] = country_row[0]
			for index, col in enumerate(columns): 
				# not interested in first six or last two
				if index < 7 or index > 27: 
					continue
				new_dict[col] = country_row[index]
			countries.append(new_dict)

	# index = 2 sets it to pretty print! 
	return json.dumps(countries, indent = 2)

'''
Prints out all the countries with the relevant attributes. 
'''
def main():
	print(fetch_countries())


if __name__ == "__main__":
	main()