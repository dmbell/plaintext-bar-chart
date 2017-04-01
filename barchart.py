import re, string; alphanum = re.compile('[\W_]+', re.UNICODE)
from collections import OrderedDict

def normalize_file(file):
	list = []
	with open(file) as file_input:
		lines = filter(None, (line.rstrip() for line in file_input))
		for line in lines:
			list.append(alphanum.sub('', str(line)).lower())
	return list

def calc_freq(line, freqs):
	for char in line:
		if char in freqs:
			freqs[char] = freqs[char] + 1
		else:
			freqs[char] = 1

lines = normalize_file('ptresume.txt')

freqs = {}

for line in lines:
	calc_freq(line, freqs)

freqs = OrderedDict(sorted(freqs.items()))

print("Number of items in dict: " + str(len(freqs)))

for char, freq in freqs.items():
	print(char + ":" + str(freq))