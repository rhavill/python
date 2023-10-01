#!/usr/bin/python3

import re

print("Position\tTeam\tName\tPoints")
input_file = open("../draft-sheet.html")

for line in input_file:
  match = re.search(r'player-pos="([^"]+)"', line)
  if match:
    position = match.group(1).upper()
  match = re.search(r'<td class="team">(\w+)</td', line)
  if match:
    team = match.group(1)
  match = re.search(r'<td class="player-name">(.+)</td>', line)
  if match:
    name = match.group(1)
  match = re.search(r'>([\+-][\.\d]+)</td>', line)
  if match:
    points = match.group(1)
    print(position + "\t" + team + "\t" + name + "\t" + points)

input_file.close()
