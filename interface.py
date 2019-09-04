#!/bin/python

from flask import Flask
from threading import Thread
import sys

app = Flask(__name__, template_folder='templates')

data = { 'counter': 1, 'value': 0.0, 'teststring': 'Hello' }

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
			userInput(input("Please enter value: "))
		except:
			print("An error occured")

def userInput(inp):
	global data
	data['value'] = float(inp)

if __name__ == '__main__':
	Thread(target = run).start()
	port = 5000
	if len(sys.argv) > 1:
		try:
			port = int(sys.argv[1])
			if port < 1 or port > 65535:
				print("Port must be between 1 and 65535. Using default port 5000")
				port = 5000
		except:
			print("Wrong port argument. Using default port 5000")
	app.run(debug=False, port=port)

