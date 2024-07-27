def solution(ineq, eq, n, m):
    if n==m and eq=='=':return 1
    if n>m and ineq=='>':return 1
    if n<m and ineq=='<':return 1
    else:return 0
    # if ineq=="<" and eq=="=": return int(n<=m)
    # if ineq==">" and eq=="=": return int(n>=m)
    # if ineq=="<" and eq=="!": return int(n<m)
    # if ineq==">" and eq=="!": return int(n>m)