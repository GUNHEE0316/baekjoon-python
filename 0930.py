#4-6

# import sys

# N,M = map(int,sys.stdin.readline().split())

# baskets = list(range(1,N+1))

# for _ in range(M):
#     i,j = map(int,sys.stdin.readline().split())
#     baskets[i-1], baskets[j-1] = baskets[j-1], baskets[i-1]

# print(*baskets)

# #4-7
# import sys

# student = list(range(1,31))

# for _ in range(28):
#     N=int(sys.stdin.readline())
#     student.remove(N)
    
# student.sort()
# print(student[0])
# print(student[1])

#4-8

# import sys
# num = set()
# for _ in range(10):
#     A=int(sys.stdin.readline())
#     num.add(A%42)
    
# print(len(num))
    
#4-9

# import sys


# N, M = map(int, sys.stdin.readline().split())
# baskets = list(range(1, N + 1))


# for _ in range(M):
  
#     i, j = map(int, sys.stdin.readline().split())
#     target_slice = baskets[i-1:j]  
#     reversed_slice = target_slice[::-1]  
#     baskets[i-1:j] = reversed_slice


# print(*baskets)

#4-10

# import sys

# N = int(sys.stdin.readline())
# score=list(map(int,sys.stdin.readline().split()))
# max_score = max(score)
# for i in range(N):

#     score[i] = score[i]/max_score*100
       

# result = sum(score)/N

# print(result)     

#5-1
# import sys
# S =sys.stdin.readline().rstrip()
# N =int(sys.stdin.readline())

# print(S[N-1])

#5-2

# import sys

# S=sys.stdin.readline().rstrip()
# print(len(S))

#5-3
import sys

import sys


T = int(sys.stdin.readline())


for _ in range(T):
 
    word = sys.stdin.readline().rstrip()
    first_char = word[0]
    last_char = word[-1]
    
    print(first_char + last_char)