# while(n:=int(input()))and 1<=n<=1000:print(f'{n} is even')if n%2 ==0 else print(f'{n} is odd');break
print(f'{(n:=int(input()))} is {"odd" if n%2!=0 else "even"}')