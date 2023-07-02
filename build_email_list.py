#!/usr/bin/python3

from os import walk
import re
import sys

all_emails = []
emails_by_file = {}
folder = sys.argv[1]

for (dirpath, dirnames, filenames) in walk(folder):
  for filename in filenames:
    emails_by_file[filename] = []
    input_file = open(folder + '/' + filename)
    for line in input_file:
      # assumption: every line in every file contains only an email address or
      # it may contain some other text if it has an email address inside angle
      # brackes "<>"
      if "<" in line:
        match = re.search(r'\<(.+)\>', line)
        email = match.group(1)
      else:
        email = line.strip()
      emails_by_file[filename].append(email.lower())
    input_file.close()

for key in emails_by_file:
  print(key, len(emails_by_file[key]))
  for email in emails_by_file[key]:
    if email not in all_emails:
      all_emails.append(email)


all_emails.sort()

# print email addresses that were excluded from one or more files
# print(" ")
# for email in all_emails:
#   for key in emails_by_file:
#     if email not in emails_by_file[key]:
#       print(email, "not in", key)

print("\nTotal:", len(all_emails))
#102
print("\n" + ",".join(all_emails))
