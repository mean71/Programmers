def solution(x1, y1, x2, y2):
    a = x1*y2 + x2*y1
    b = y1*y2
    while b:
        a,b = b,a%b
    return [(x1*y2 + x2*y1)//a, y1*y2//a]
