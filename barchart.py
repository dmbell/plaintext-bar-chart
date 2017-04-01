import re, string; alphanum = re.compile('[\W_]+', re.UNICODE)


def normalize_file(file):
	list = []
	with open(file) as file_input:
		lines = filter(None, (line.rstrip() for line in file_input))
		for line in lines:
			list.append(alphanum.sub('', str(line)).lower())
	return list

lines = normalize_file('ptresume.txt')

for line in lines:
	print(line)