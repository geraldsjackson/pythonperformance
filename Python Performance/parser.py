#!/usr/bin/python

from functions import parseString
from enum import Enum


Directions = Enum()
input_string = raw_input('?>')

print input_string

parseString(input_string)



