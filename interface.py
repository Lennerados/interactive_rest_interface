#!/bin/python

from flask import Flask
from threading import Thread
import sys

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
	port = 5000
	if len(sys.argv) > 1:
		try:
			port = int(sys.argv[1])
			if port < 1 or port > 65535:
				print("Port must be between 1 and 65535. Using default port 5000")
				port = 5000
		except:
			print("Wrong port argument. Using default port 5000")
	app.run(debug=True, port=port)

