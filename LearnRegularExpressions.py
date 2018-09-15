#!/usr/bin/env python
import fileinput
import re
import sys
compiled_regex = re.compile(sys.argv[1]); 
my_file = sys.argv[2] 
for each_line_of_text in fileinput.input(my_file):
    matches = compiled_regex.findall(each_line_of_text)
    if len(matches) > 0
       print matches
