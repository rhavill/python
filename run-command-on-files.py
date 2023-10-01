#!/usr/bin/python3

import re
import subprocess

args = [
  "docker-compose",
  "exec",
  "frontend",
  "./node_modules/eslint/bin/eslint.js",
  "-c",
  "player/.eslintrc.js",
]
input_file = open("../files-changed.txt")

for line in input_file:
  file = line.rstrip()
  args.append(file)

subprocess.run(args)
input_file.close()
