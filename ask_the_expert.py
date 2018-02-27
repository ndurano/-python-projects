import Tkinter
from Tkinter import Tk
import tkSimpleDialog
import tkMessageBox

def read_from_file():
	with open('capital_cities.txt') as file:
		for line in file:
			line = line.rstrip('\n')
			country, city = line.split('/')
			the_world[country] = city


def write_to_file(country_name, city_name):
	with open('capital_cities.txt', 'a') as file:
		file.write('\n' + country_name + '/' + city_name)


print('Ask the expert = Capital Cities of the World')

root = Tk()
root.withdraw()
the_world = {}

read_from_file()

while True:
	query_country = tkSimpleDialog.askstring('Country', 'Type the name of the country :')


	if query_country in the_world:
		result = the_world[query_country]
		tkMessageBox.showinfo('Answer', 'The capital city of ' + query_country + 'is' + result )

	else:
		new_city = tkSimpleDialog.askstring('Teach me', 'I don\'t know!' + 'What is the capital city of ' + query_country + '?')
		the_world[query_country] = new_city
		write_to_file(query_country, new_city)


root.mainloop()
