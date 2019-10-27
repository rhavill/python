#!/usr/bin/python3

''' 
	This script renames image files in a directory and copies them to another
  directory. The original image file names may be from a few photo file name
  formats. The destination file names have a YYYY-MM-DD-NN.jpg format. 
'''

import re
import sys
from os import walk, rename

if len(sys.argv) > 2:
  source_folder = sys.argv[1]
  dest_folder = sys.argv[2]
  if source_folder[len(source_folder)-1] != '/':
    source_folder = source_folder + '/'
  if dest_folder[len(dest_folder)-1] != '/':
    dest_folder = dest_folder + '/'
  file_list = []
  renamed_file_list = []
  date_counts = {}
  for (dirpath, dirnames, filenames) in walk(source_folder):
      file_list.extend(filenames)
      break
  file_list.sort()
  for i in range(len(file_list)):
    m = re.match(r'^\w+_(\d{4})(\d{2})(\d{2})_', file_list[i])
    if m is not None:
      year = m.group(1)
      month = m.group(2)
      day = m.group(3)
      date = year + '-' + month + '-' + day
      key = year + month + day
      if date_counts.get(key):
        date_counts[key] += 1
      else:
        date_counts[key] = 1
      name = date + '-' + f'{date_counts[key]:02d}' + '.jpg'
      source_file = source_folder + file_list[i]
      dest_file = dest_folder + name
      rename(source_file, dest_file)
      print(source_file + ' -> ' + dest_file)
    else:
      print('could not parse date in file ' + file_list[i])
else:
  print("Please specify a source directory containing image files and a destination directory for the new files.")
  print("Example: python " + sys.argv[0] + " source-folder dest-folder")
