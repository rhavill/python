#!/usr/bin/python3

''' 
	This script creates a randomized desktop background for Ubuntu.
'''

import sys
from os import path, remove, symlink, system, walk
from random import randrange

if len(sys.argv) > 1:
  source_directory = sys.argv[1]
  files = []
  for (dirpath, dirnames, filenames) in walk(source_directory):
    for filename in filenames:
      name, file_extension = path.splitext(filename)
      if file_extension.lower() == '.jpg':
        files.append(dirpath + '/' + filename)
  if(len(files)):
    random_file = files[randrange(len(files))]
    system("gsettings set org.gnome.desktop.background picture-uri \"file://" + random_file + "\"")
  else:
    print("Error: Could not find any jpg files in directory " + source_directory)
else:
  print("Please specify a source directory.")
  print("Example: python " + sys.argv[0])