#!/usr/local/bin/python3

''' 
	This script resizes image files in a directory and copies them to another
  directory. The original image file names may be from a few photo file name
  formats. The destination file names have a YYYY-MM-DD-NN.jpg format. 
'''

import re
import sys
from os import walk, rename
from PIL import Image, ExifTags
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
    else:
      m = re.match(r'^(\d{2})(\d{2})(\d{2})\d{4}', file_list[i])
      if m is not None:
        month = m.group(1)
        day = m.group(2)
        year = '20' + m.group(3)
      else:
        m = re.match(r'^(\d{4})(\d{2})(\d{2})_', file_list[i])
        if m is not None:
          year = m.group(1)
          month = m.group(2)
          day = m.group(3)
        else:
          print('could not parse date in file ' + file_list[i])
          continue
    date = year + '-' + month + '-' + day
    # print('date ' + date)
    key = year + month + day
    if date_counts.get(key):
      date_counts[key] += 1
    else:
      date_counts[key] = 1
    name = date + '-' + f'{date_counts[key]:02d}' + '.jpg'
    source_file = source_folder + file_list[i]
    dest_file = dest_folder + name
    print(f'source_file is {source_file}')
    fd_img = open(source_file, 'rb')
    img = Image.open(fd_img)
    width, height = img.size

    img = resizeimage.resize_width(img, 1024)

    for orientation in ExifTags.TAGS.keys():
        if ExifTags.TAGS[orientation]=='Orientation':
            break
    exif=dict(img.getexif().items())
    if exif[orientation] == 3:
        image=img.rotate(180, expand=True)
    elif exif[orientation] == 6:
        img=img.rotate(270, expand=True)
    elif exif[orientation] == 8:
        img=image.rotate(90, expand=True)
    img.save(dest_file, img.format)
    img.close()
    print(f'{source_file} ({width}x{height}) -> {dest_file}')
else:
  print("Please specify a source directory containing image files and a destination directory for the new files.")
  print("Example: python " + sys.argv[0] + " source-folder dest-folder")
