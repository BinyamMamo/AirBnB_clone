#!/usr/bin/python3

from datetime import datetime as dt

dstr = "2017-09-28T21:05:54.119427"

print(type(dstr))
print("-----------")
ndate = dt.strptime(dstr, "%Y-%m-%dT%H:%M:%S.%f")
print(type(ndate))