#4-1
#import sys
# N = int(sys.stdin.readline())
# b_list= list(map(int,sys.stdin.readline().split()))
# v =int(sys.stdin.readline())
# print(b_list.count(v))

#4-2
# import sys

# N,X=map(int,sys.stdin.readline().split())

# my_list=list(map(int,sys.stdin.readline().split()))

# for i in range(N):
#     if X > my_list[i]:
#         print(my_list[i],end=" ")

#4-3

# import sys
# N = int(sys.stdin.readline())
# my_list = list(map(int,sys.stdin.readline().split()))
# print(min(my_list), max(my_list))

#4-4
# import sys
# my_list = []
# for i in range(9):
#     N= int(sys.stdin.readline())
#     my_list.append(N)
    
# print(max(my_list))
# print(my_list.index(max(my_list))+1)

#4-5

# import sys

# N, M = map(int, sys.stdin.readline().split())

# baskets = [0] * N

# for _ in range(M):

#     i, j, k = map(int, sys.stdin.readline().split()) 

#     for idx in range(i - 1, j):
#         baskets[idx] = k 

# print(*baskets)