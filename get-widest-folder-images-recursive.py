from os import walk
import os.path
import Image

def get_recursive_file_paths(dir):
	files = []
	folders = []
	file_paths = []
	for (dirpath, dirnames, filenames) in walk(dir):
	    folders.append(dirpath)
	    files.append(filenames)
	for i in range(0, len(folders)):
		for j in range(0, len(files[i])):
			file_paths.append(folders[i]+'/'+files[i][j])
	return file_paths

def get_recursive_image_files(dir):
	image_files = []
	files = get_recursive_file_paths(dir)
	for file in files:
		file_extension = os.path.splitext(file)[1]
		# file_extension = file_info[1]
		if file_extension == '.jpg' or file_extension == '.jpeg':
			try:
				Image.open(file)
				image_files.append(file)
			except IOError:
				x = 0
	return image_files

def get_image_widths(dir):
	image_widths = []
	files = get_recursive_image_files(dir)
	for i in range(0, len(files)):
		image = Image.open(files[i])
		image_widths.append([image.size[0], files[i]])
	return image_widths

def get_widest_images(dir, count):
	files = get_image_widths(dir)
	image_widths = sorted(files, key=lambda files: files[0], reverse=True)
	widest = []
	for i in range(count):
		if i < len(image_widths):
			widest.append(image_widths[i])
		else:
			break
	return widest

root = '/tmp'
files = get_widest_images(root,10)
print files
