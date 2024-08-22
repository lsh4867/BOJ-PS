# 내코드

a, b = map(int, input().split())

list_1 = [[0] * (b+1) for _ in range(a+1)]
list_2 = [[0] * (b+1) for _ in range(a+1)]

for i in range(1, a+1):
  d1 = list(map(int, input().split()))
  for j in range(1, b+1):
    list_1[i][j] = d1[j - 1]

for i in range(1, a+1):
  d2 = list(map(int, input().split()))
  for j in range(1, b+1):
    list_2[i][j] = d2[j - 1]

for i in range(1, a+1):
  for j in range(1, b+1):
    print(list_1[i][j] + list_2[i][j], end=' ')
  print()


# 내코드 -> GPT 디벨롭 (List Comprehension 기가 막히네,,)
a, b = map(int, input().split())

list_1 = [list(map(int, input().split())) for _ in range(a)]
list_2 = [list(map(int, input().split())) for _ in range(a)]

for i in range(a):
  for j in range(b):
    print(list_1[i][j] + list_2[i][j], end=' ')
  print()


# 인터넷 버전

N, M =map(int, input().split())

A, B=[], []

for _ in range(N):
    row=list(map(int, input().split()))
    A.append(row)

for _ in range(N):
    row=list(map(int, input().split()))
    B.append(row)

for i in range(N):
    for j in range(M):
        print(A[i][j]+B[i][j], end=' ')
    print()
