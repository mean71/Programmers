def solution(x):
    frequency = {}
    key_counts = 0
    mode = 0
    
    for i in x:
        if i in frequency: frequency[i] += 1
        else: frequency[i] = 1

    for key,count in frequency.items():
        if key_counts == 0: key_counts, mode = count, key
        elif key_counts < count: key_counts, mode = count ,key
        elif key_counts == count: mode = -1
    return mode