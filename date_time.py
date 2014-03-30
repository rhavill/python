#!/usr/bin/python
from datetime import datetime
 
now = datetime.now()
current_year = now.year
current_month = now.month
current_day = now.day

print '%s:%s:%s' % (now.hour, now.minute, now.second)