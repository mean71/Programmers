def solution(s):
    s = s.lower()
    if s[0].isalpha(): s = s[0].upper() + s[1:]
    for i in range(len(s)-1):
        if s[i] == ' ':
            if s[i+1] != None and s[i+1] != ' ':
                s = s[:i+1] + s[i+1].upper() + s[i+2:]
    return s