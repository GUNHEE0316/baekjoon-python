## 3-6
# import sys
# # 테스트 케이스의 개수 T를 입력받음
# T = int(sys.stdin.readline())

# # T번 반복
# for _ in range(T):
#     # A와 B를 한 줄에서 입력받아 정수로 변환
#     A, B = map(int, sys.stdin.readline().split())
    
#     # A와 B의 합을 출력
#     print(A + B)

#3-7
# import sys
# T = int(sys.stdin.readline())

# for i in range(T):
#     A,B=map(int,sys.stdin.readline().split())
#     print(f"Case #{i+1}: {A+B}") 

#3-8

# import sys
# T = int(sys.stdin.readline())

# for i in range(T):
#     A,B=map(int,sys.stdin.readline().split())
#     print(f"Case #{i+1}: {A} + {B} = {A+B}") 


#3-9

# import sys

# T = int(sys.stdin.readline())

# for i in range(T):
#     for j in range(i+1):
#         print("*",end ='')
#     print()

#3-10

# import sys

# T = int(sys.stdin.readline())

# for i in range(1, T + 1):
#     # i개의 별을 만든다
#     stars = "*" * i
    
#     # T칸을 기준으로, 만든 별(stars)을 오른쪽으로 정렬하여 출력한다
#     print(f"{stars:>{T}}")
    
    
#3-11

# import sys

# while True:
#     A,B=map(int,sys.stdin.readline().split())
#     if A==0 and B == 0:
#         break  
#     print(A + B)

# 3- 12

import sys

# 무한 루프 시작
while True:
    # try: 일단 입력받아서 A+B를 출력하는 것을 시도한다.
    try:
        A, B = map(int, sys.stdin.readline().split())
        print(A + B)
        
    # except: 더 이상 입력받을 내용이 없어서 에러가 나면,
    except:
        break # 루프를 탈출하고 프로그램을 종료한다.