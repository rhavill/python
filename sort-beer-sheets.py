#!/usr/bin/python3

''' 
	Sorts a beer sheets CSV file by player value. 
'''

import re
import sys

position_map = {
	'QUARTERBACK': 'QB',
	'TIGHT END': 'TE',
	'RUNNING BACK': 'RB',
	'WIDE RECEIVER': 'WR',
}

if len(sys.argv) > 1:
	read_file = open(sys.argv[1])
	position = ""
	for line in read_file:
		match = re.search(r'^(VALUE)', line)
		if match:
			continue
		match = re.search(r'^([A-Z\s]+),,,,', line)
		if match:
			position = position_map[match.group(1)]
			continue
		match = re.search(r'(\d*),([A-Z]+),([\w\s\'\.]+),(-?[\d\.]+)', line)
		if match:
			value = match.group(1)
			team = match.group(2)
			name  = match.group(3)
			points  = match.group(4)
			# print(value, team, position, name, points)
			print("%s,%s,%s,%s,%s" % (value, team, position, name, points))
		# ignore_line = False
		# for i in range(len(remove_lines_with)):
		# 	match = re.search("^\s*;*\s*" + remove_lines_with[i], line);
		# 	if match:
		# 		ignore_line = True
		# 		break
		# if not ignore_line:
		# 	write_file.write(line)
	read_file.close()
	# write_file.close()
else:
	print("Please specify an input CSV file.")
