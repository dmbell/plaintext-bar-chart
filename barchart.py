from collections import OrderedDict
import re, string; alphanum = re.compile('[\W_]+', re.UNICODE)

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

def reorder_nums(freqs):
	for i in range(10):
		if str(i) in freqs:
			v = freqs[str(i)]
			del freqs[str(i)]
			freqs[str(i)] = v

lines = normalize_file('ptresume.txt')

freqs = {}

for line in lines:
	calc_freq(line, freqs)

freqs = OrderedDict(sorted(freqs.items()))

reorder_nums(freqs)

for char, freq in freqs.items():
	print(char + ":" + str(freq))