'''
barchart.py
Purpose: Simple bar chart plot of alphanumeric characters in a text file using matplotlib
Version. 0.1
Author: Douglas Bell
'''

import numpy as np
import matplotlib.pyplot as plot
from collections import OrderedDict
import re, string; alphanum = re.compile("[\W_]+", re.UNICODE)

def normalize_file(file):
	'''
	Return a list of all lines in a file with blank spaces and non-alphanumeric characters removed in lowercase

	Args:
		file: Name of file to normalize
	Returns:
		list: List of normalized strings
	'''

	list = []
	with open(file) as file_input:
		lines = filter(None, (line.rstrip() for line in file_input))
		for line in lines:
			list.append(alphanum.sub('', str(line)).lower())
	return list

def calc_frequencies(line, freqs):
	'''
	Calculate the frequency of a character in a line with the given dictionary

	Args:
		line: Line of characters to count
		freqs: Dictionary where count of individual characters is being tracked
	'''
	for char in line:
		if char in freqs:
			freqs[char] = freqs[char] + 1
		else:
			freqs[char] = 1

def reorder_nums(freqs):
	'''
	Move 0-9, if present, in a pre-sorted given OrderedDict to the end of the dictionary

	Args:
		freqs: Pre-sorted (0-9, a-z) OrderedDictionary
	'''

	for i in range(10):
		if str(i) in freqs:
			v = freqs[str(i)]
			del freqs[str(i)]
			freqs[str(i)] = v

def create_dict(lines):
	'''
	Create a dictionary of <character, frequency> pairs from given list of strings

	Args:
		lines: List of strings of which to calculate frequency of characters

	Returns:
		freqs: OrderedDict of <char, freq> pairs
	'''

	freqs = {}
	for line in lines:
		calc_frequencies(line, freqs)
	freqs = OrderedDict(sorted(freqs.items()))
	reorder_nums(freqs)
	return freqs

def plot_dict(freqs):
	'''
	Plot a basic bar chart using matplotlib of given dictionary's <k, v> pairs

	Args:
		freqs: Dictionary to plot
	'''

	y_pos = np.arange(len(freqs))
	plot.bar(y_pos, list(freqs.values()), align="center", alpha=0.5)
	plot.xticks(y_pos, list(freqs.keys()))
	plot.ylabel("Frequency")
	plot.xlabel("Character")
	plot.title("Alphanumeric Character Frequency")
	plot.show()

def print_dict(freqs):
	'''
	Print dictionary <k, v> pairs for testing purposes
	'''
	
	for char, freq in freqs.items():
		print(char + ":" + str(freq))

lines = normalize_file("ptresume.txt")
freqs = create_dict(lines)
plot_dict(freqs)
