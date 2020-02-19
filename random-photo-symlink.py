#!/usr/bin/python3

''' 
	This script creates a symlink to a random file in a directory or one if its subdirectories.
  It may be run as a cron job and is used to randomize the desktop background.
'''

import sys
from os import path, remove, symlink, walk
from random import randrange

if len(sys.argv) > 2:
  destination = sys.argv[2]
  files = []
  for (dirpath, dirnames, filenames) in walk(sys.argv[1]):
    for filename in filenames:
      name, file_extension = path.splitext(filename)
      if file_extension.lower() == '.jpg':
        files.append(dirpath + '/' + filename)
  if(len(files)):
    random_file = files[randrange(len(files))]
    if path.exists(destination):
      remove(destination)
    symlink(random_file, destination)
  else:
    print("Error: Could not find any jpg files in directory " + sys.argv[1])
else:
  print("Please specify a source directory and destination symlink.")
  print("Example: python " + sys.argv[0] + " source-folder destination")