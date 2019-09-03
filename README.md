# Interactive Rest interface

## Usage
A simple python script to simulate a json rest interface using the flask framework (https://github.com/pallets/flask).

To start, simply type `python interface.py`. If you want to start it on a custom port, use the first argument for that (e.g. `python interface.py 6920`). Now you can change the value for the field "value" by typing any float value in the terminal. The value "counter" will be incremented every time the rest interface is requested.

## Adjustment
You can simply change the structure of the json object by changing the data dictionary in the code. You can also change the behaviour of the program, by changing the method `home()` (which is called every time a http request is received) or by changing the method `userInput()` (which is called everytime the user enters a string in the terminal).

