'''
api.py
Kezia Sharnoff
April 21, 2025

NAME: api.py - API and CSV to JSON assignment
SYNOPSIS: python3 api.py localhost [port]
DESCRIPTION: Hosts a webpage where lists of countries flags with certain
attributes (symbols or colors) can be queried and shown. 


Modifed the code of:
- github.com/ondich/cs257-2025-spring/blob/main/flask/flask_sample.py
- github.com/ksharnoff/cs257/blob/main/individual/cli.py
'''

import flask 
import argparse # for the CLI arguments
import csv # to read the csv file
import json # to transform the dictionary into json for the user

app = flask.Flask(__name__)

@app.route('/')
def hello():
    return "The page is up!"


'''
Returns true if the attribute is a symbol or color being tested for
'''
def not_valid_attribute(attribute):
	valid_attributes = ("bars", "stripes", "circles", "crosses", "saltires", 
					 "sunstars", "crescent", "triangle", "inanimateimage", 
					 "animateimage", "red", "green", "blue", "gold", "white",
					 "black", "orange")

	if attribute.lower() in valid_attributes:
		return False

	# if the attribute inputted is not in the csv (or not a symbol/color)
	return True


# all of the columns of the data at the correct indicies
indices = ("name", "landmass", "zone", "area", "population", "language",
		   "religion", "bars", "stripes", "colours", "red", "green", "blue",
		   "gold", "white", "black", "orange", "mainhue", "circles", 
		   "crosses", "saltires", "quarters", "sunstars", "crescent", 
		   "triangle", "inanimateimage", "animateimage", "text", "topleft",
		   "topright")
'''
Inputs the attribute, outputs a list of 2-tuples with the country and the
number of the specified attribute, where the number of that attribute  is
greater than zero. The boolean items (colors, etc.) will all have 1. I am
only returning a 2-tuples because the rest of the data per country will not
be meaningful. 
'''
@app.route('/countries/<attribute>')
def fetch_countries_csv(attribute):
	if (not_valid_attribute(attribute)):
		return json.dumps([])

	index = indices.index(attribute)
	countries = []

	with open('../data/flags.csv') as f:
		reader = csv.reader(f)
		# each row represents a country
		for country_row in reader:
			if country_row[index] != '0':
				countries.append((country_row[0], country_row[index]))

	return json.dumps(countries)

'''
Help documentation page for the API as specified in ./templates/help.html
'''
@app.route('/help')
def help():
     return flask.render_template('help.html')



if __name__ == '__main__':
    parser = argparse.ArgumentParser('Intro to API and Flask assignment')
    parser.add_argument('host', help='the host on which this application is running')
    parser.add_argument('port', type=int, help='the port on which this application is listening')
    arguments = parser.parse_args()
    app.run(host=arguments.host, port=arguments.port, debug=True)