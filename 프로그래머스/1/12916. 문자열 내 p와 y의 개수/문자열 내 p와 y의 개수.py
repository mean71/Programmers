def solution(s):
    s = s.lower()
    if len(s)<=50 and s.count('p')==s.count('y'):return True
    else:return False