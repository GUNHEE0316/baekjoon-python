#1-11
# A,B,C= map(int,input().split())
# print(A+B+C)

#1-12
# print("\    /\\")
# print(" )  ( ')")
# print("(  /  )")
# print(" \(__)|")

#1-13

# print("|\\_/|")
# print("|q p|   /}")
# print('( 0 )"""\\')
# print('|"^"`    |')
# print("||_/=\\\\__|")

#2-1
# A가 B보다 큰 경우에는 '>'를 출력한다.
# A가 B보다 작은 경우에는 '<'를 출력한다.
# A와 B가 같은 경우에는 '=='를 출력한다.
# A,B=map(int, input().split())

# if A>B: {
#     print(">")
    
# }

# elif A<B:{
    
#     print("<")
# }

# elif A==B:{
#     print("==")
# }

#2-2
# 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.

# A = int(input())

# if 100 >= A >=90 :{
#     print("A")
# }

# elif 89 >= A >=80:{
#     print("B")
# }

# elif 79 >= A >=70:{
#     print("C")
# }

# elif 69 >= A >=60:{
#     print("D")
# }

# else:{
#     print("F")
# }

#2-3
# year = int(input())
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(1) 
# else:
#     print(0) 

#2-4

# X=int(input())
# Y=int(input())

# if X>0 and Y > 0:{
#     print("1")
# }

# elif X < 0 and Y > 0:{
#     print("2")
# }

# elif X < 0 and Y < 0:{
#     print("3")
# }

# elif X > 0 and Y <0:{
#     print("4")
# }

#2-5

# # H(시)와 M(분)을 입력받습니다.
# H, M = map(int, input().split())

# # M이 45분보다 작을 경우, 시간(H)에서 1을 빌려옵니다.
# if M < 45:
#     # 시간(H)이 0시일 경우, 전날인 23시로 변경합니다.
#     if H == 0:
#         H = 23
#     # 0시가 아닐 경우, 단순히 1시간을 뺍니다.
#     else:
#         H = H - 1
#     # 분(M)은 60분을 빌려와 45분을 뺀 값을 계산합니다. (M + 60 - 45)
#     M = M + 15
# # M이 45분보다 크거나 같을 경우, 분(M)에서 45를 빼기만 합니다.
# else:
#     M = M - 45

# # 45분 앞당겨진 최종 시간을 출력합니다.
# print(H, M)

#2-6

# # 현재 시각 A(시)와 B(분)를 입력받습니다.
# A, B = map(int, input().split())
# # 요리하는 데 필요한 시간 C(분)를 입력받습니다.
# C = int(input())

# # 현재 시각을 모두 분으로 변환한 뒤, 요리 시간을 더합니다.
# total_minute = A * 60 + B + C

# # 총 분을 60으로 나눈 몫이 최종 '시'가 됩니다.
# # 24시를 넘는 경우를 대비해 24로 나눈 나머지를 구합니다.
# end_hour = (total_minute // 60) % 24

# # 총 분을 60으로 나눈 나머지가 최종 '분'이 됩니다.
# end_minute = total_minute % 60

# # 계산된 종료 시각을 출력합니다.
# print(end_hour, end_minute)

#2-7

A, B, C=map(int, input().split())

if A==B and A==C:{
    print(10000+A*1000)
} 

elif A==B or A==C:{
    print(1000+A*100)
}

elif B==C:{
    print(1000+B*100)
}

else:{
    print(max(A,B,C)*100)
}
