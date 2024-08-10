def solution(A,B):
    A.sort();B.sort(reverse = True)
    AB = 0
    for i in range(len(A)):
        AB += A[i]*B[i]
    return AB