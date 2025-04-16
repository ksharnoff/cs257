'''
cli.py, Implementing a Simple CLI Assignment
Kezia Sharnoff
April 18 2025


NAME: cli.py - command-line interface exercise
SYNOPSIS: python3 cli.py attribute
DESCRIPTION: Shows a list of the countries that have the specified attribute, a
symbol or a color (stripes, bars, sunstars...red, blue, green...). 

Sources used, more information is at specific functions: 
- https://github.com/ondich/cs257-2025-spring/blob/main/arguments/argparse-sample.py 
- https://github.com/ondich/cs257-2025-spring/blob/main/data-wrangling/csv-wrangler.py
- https://realpython.com/if-name-main-python/

flags.csv is formatted like:
	name, landmass, zone, area, population, language, religion, bars, stripes, colours, 
	red, green, blue, gold, white, black, orange, mainhue, circles, crosses, saltires, 
	quarters, sunstars, crescent, triangle, icon, animate, text, topleft, topright

In this CLI I have renamed animate and icon to be unanimateImage and 
animateImage to be more clear to the user. 
'''

import argparse # for the CLI arguments
import csv # to read the csv file
import sys # for sys.exit(1)


'''
Uses argparse to get the category (symbol or color) and then the specified 
attribute
I used https://github.com/ondich/cs257-2025-spring/blob/main/arguments/argparse-sample.py 
and copied some of the code in the get_parsed_arguments function.
'''
def get_parsed_args():
	parser = argparse.ArgumentParser(description = 'Prints list of 1986 sovereign state flags that have that symbol or color')
	parser.add_argument('attribute', help = 'the specific symbol or color searching for: stripes, bars, circles, crosses, saltires, sunstars, crescent, triangle, inanimateImage, animateImage, red, orange, gold, green, blue, white, black. Write gold for yellow and orange for brown.')
	return parser.parse_args()


'''
Returns true if the cetegory (symbol or color) is correct and if the attribute
is within the category chosen. 
'''
def not_valid_prased_args(arguments):
	valid_attributes = ("bars", "stripes", "circles", "crosses", "saltires", 
					 "sunstars", "crescent", "triangle", "inanimateImage", 
					 "animateImage", "red", "green", "blue", "gold", "white",
					 "black", "orange")

	if arguments.attribute in valid_attributes:
		return False

	# if the attribute inputted is not one of the ones that we have in the csv
	return True


# all of the columns at their correct indicies
indices = ("name", "landmass", "zone", "area", "population", "language",
		   "religion", "bars", "stripes", "colours", "red", "green", "blue",
		   "gold", "white", "black", "orange", "mainhue", "circles", 
		   "crosses", "saltires", "quarters", "sunstars", "crescent", 
		   "triangle", "inanimateImage", "animateImage", "text", "topleft",
		   "topright")


'''
Inputs the prased CLI arguments, outputs a list of 2-tuples with the country 
and the number of attributes, where the number of that attribute is greater 
than zero. 
Copied the starting code about reading from the csv from:
https://github.com/ondich/cs257-2025-spring/blob/main/data-wrangling/csv-wrangler.py
'''
def fetch_countries_csv(arguments):
	index = indices.index(arguments.attribute)
	countries = []

	with open('../data/flags.csv') as f:
		reader = csv.reader(f)
		# each row represents a country
		for country_row in reader:
			if country_row[index] != '0':
				# appends a 2-tuple with country name and attribute count
				countries.append((country_row[0], country_row[index]))

	return countries


# the attributes that are in a boolean form (and therefore should not print a 
# count)
booleans = ("red", "greenblue", "gold", "white", "black", "orange", "crescent",
		   "triangle", "inanimateImage", "animateImage")

'''
Prints out the countries that have the attribute asked for from the CLI. 
'''
def main():
	arguments = get_parsed_args()

	if not_valid_prased_args(arguments):
		sys.exit("Usage: cli.py attribute\n\tPrints flags with the" +
				 " inputted symbol or color")

	countries = fetch_countries_csv(arguments)
	attribute = arguments.attribute

	boolean = attribute in booleans

	for country in countries:
		if boolean:
			print(f'{country[0]} has {attribute}')
		else: # if it's a count:  
			print(f'{country[0]} has {country[1]} {attribute}')


'''
I read the following article and therefore maybe think that this would be a 
better way to call main() than to just write main(), in this case. I copied
the code to here. 
https://realpython.com/if-name-main-python/
'''
if __name__ == "__main__":
	main()