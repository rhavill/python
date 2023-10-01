#!/usr/bin/python3

import re

input_file = open("../files-changed.html")

for line in input_file:
  match = re.search(r'<a[^\>]+class="Link--primary Truncate-text"[^\>]+\>([^\<]+)\<', line)
  if match:
    file = match.group(1)
    print(file)

input_file.close()
