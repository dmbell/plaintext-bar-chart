import numpy as np
import matplotlib.pyplot as plot
from collections import OrderedDict
import re, string; alphanum = re.compile("[\W_]+", re.UNICODE)

def normalize_file(file):
	list = []
	with open(file) as file_input:
		lines = filter(None, (line.rstrip() for line in file_input))
		for line in lines:
			list.append(alphanum.sub('', str(line)).lower())
	return list

def calc_frequencies(line, freqs):
	for char in line:
		if char in freqs:
			freqs[char] = freqs[char] + 1
		else:
			freqs[char] = 1

def reorder_nums(freqs):
	for i in range(10):
		if str(i) in freqs:
			v = freqs[str(i)]
			del freqs[str(i)]
			freqs[str(i)] = v

def create_dict(lines):
	freqs = {}
	for line in lines:
		calc_frequencies(line, freqs)
	freqs = OrderedDict(sorted(freqs.items()))
	reorder_nums(freqs)
	return freqs

def plot_dict(freqs):
	y_pos = np.arange(len(freqs))
	plot.bar(y_pos, list(freqs.values()), align="center", alpha=0.5)
	plot.xticks(y_pos, list(freqs.keys()))
	plot.ylabel("Frequency")
	plot.xlabel("Character")
	plot.title("Alphanumeric Character Frequency")
	plot.show()

def print_dict(freqs):
	for char, freq in freqs.items():
		print(char + ":" + str(freq))

lines = normalize_file("ptresume.txt")
freqs = create_dict(lines)
plot_dict(freqs)
