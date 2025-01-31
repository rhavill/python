#!/usr/bin/python3

''' 
	This script resizes image files in a directory and copies them to another
  directory. The original image file names may be from a few photo file name
  formats. The destination file names have a YYYY-MM-DD-NN.jpg format. 

  To set up dependencies, run:

  sudo apt install python3-pip
  sudo pip3 install python-resize-image
'''

import re
import sys
from os import walk, rename
from PIL import ImageOps, Image#, ExifTags
from resizeimage import resizeimage

if len(sys.argv) > 2:
  source_folder = sys.argv[1]
  dest_folder = sys.argv[2]
  if source_folder[len(source_folder)-1] != '/':
    source_folder = source_folder + '/'
  if dest_folder[len(dest_folder)-1] != '/':
    dest_folder = dest_folder + '/'
  file_list = []
  renamed_file_list = []
  for (dirpath, dirnames, filenames) in walk(source_folder):
      file_list.extend(filenames)
      break
  file_list.sort()
  for i in range(len(file_list)):
    source_file = source_folder + file_list[i]
    dest_file = dest_folder + file_list[i]
    fd_img = open(source_file, 'rb')
    img = Image.open(fd_img)
    width, height = img.size
    is_landscape = width > height
    if is_landscape:
      img = resizeimage.resize_width(img, 1024)
    else:
      img = resizeimage.resize_height(img, 1024)
    img = ImageOps.exif_transpose(img)
    img.save(dest_file, img.format)
    print(source_file, dest_file)
    img.close()
else:
  print("Please specify a source directory containing image files and a destination directory for the new files.")
  print("Example: python " + sys.argv[0] + " source-folder dest-folder")
