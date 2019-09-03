#!/bin/python

from flask import Flask
from threading import Thread

app = Flask(__name__, template_folder='templates')

data = { 'counter': 1, 'value': 0.0, 'teststring': 'Hallo' }

@app.route('/')
def home():
	global data
	data['counter'] += 1
	data['teststring'] = 'Hallo' + str(data['counter'])
	return data

def run():
	global data
	while True:
		try:
			inp = input("Please enter value: ")
			data['value'] = float(inp)
		except:
			print("An error occured")

if __name__ == '__main__':
	Thread(target = run).start()
	app.run(debug=True)

