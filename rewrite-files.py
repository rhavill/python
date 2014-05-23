#!/usr/bin/python

''' 
	This script rewrites all of the files in a directory. 
	If a line in a file contains text that matches the list of strings in the "match" array,
	that line is removed from the file.
'''

import sys
from os import walk

remove_lines_with = [
	'GROUP',
	'HALF'
];

if len(sys.argv) > 2:
	source_folder = sys.argv[1]
	dest_folder = sys.argv[2]
	if source_folder[len(source_folder)-1] != '/':
		source_folder = source_folder + '/'
	if dest_folder[len(dest_folder)-1] != '/':
		dest_folder = dest_folder + '/'
	file_list = []
	for (dirpath, dirnames, filenames) in walk(source_folder):
	    file_list.extend(filenames)
	    break
	for i in range(len(file_list)):
		write_file = open(dest_folder+'/'+file_list[i], "w")
		with open(source_folder+'/'+file_list[i], "r") as read_file:
			for line in read_file:
				ignore_line = False
				for i in range(len(remove_lines_with)):
					if remove_lines_with[i] in line:
						ignore_line = True
						break
				if not ignore_line:
					write_file.write(line)
		read_file.close()
		write_file.close()
else:
	print "Please specify a source directory containing TPL files and a destination directory for the new TPL files."
	print "Example: python rewrite-files.py source-folder dest-folder"
