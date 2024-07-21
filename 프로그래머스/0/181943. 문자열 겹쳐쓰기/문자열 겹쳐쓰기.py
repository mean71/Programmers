import re

def solution(my_string, overwrite_string, s):
    pattern=r'^[0-9A-Za-z]+$'
    if re.match(pattern,my_string)and re.match(pattern,overwrite_string)and 1<=len(overwrite_string)<=len(my_string)<=1000 and 0<=s<=len(my_string)-len(overwrite_string):
        my_string = my_string[:s]+overwrite_string+my_string[s+len(overwrite_string) :]
    return my_string