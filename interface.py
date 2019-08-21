#!/bin/python

from flask import Flask
import threading
import time

app = Flask(__name__, template_folder='templates')

data = { 'counter': 1, 'value': 0 }

@app.route('/')
def home():
	global data
	data['counter'] += 1
	return data

def run():
	global data
	while True:
		inp = input("Please enter value: ")
		data['value'] = int(inp)

if __name__ == '__main__':
	threading.Thread(target = run).start()
	app.run(debug=True)
