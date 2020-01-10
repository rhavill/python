#!/usr/bin/python3

''' 
	This script recursively deletes unwanted OS X files/folders in a specific 
  directory. It is assumed that the backup files have file names that begin with 
  "._" or ".DS_Store"
'''

from os import walk, remove

for (dirpath, dirnames, filenames) in walk('.', topdown=True):
  for filename in filenames:
    if filename.startswith('.DS_Store') or filename.startswith('._'):
      filepath = dirpath + '/' + filename
      print("Deleting " + filepath)
      remove(filepath)
      