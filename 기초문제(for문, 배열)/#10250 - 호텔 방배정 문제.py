# 내코드
n = int(input())
for _ in range(n):
  a, b, c = map(int, input().split())
  if c%a == 0:
    floor = a
    num = '{:02}'.format(c//a)
  else:
    floor = c%a
    num = '{:02}'.format(c//a+1)
  print(f'{floor}{num}')

# GPT ver
n = int(input())
for _ in range(n):
    a, b, c = map(int, input().split())
    floor = c % a if c % a != 0 else a
    num = (c-1)//a + 1 # c-1 : 0 기반 인덱스로 조정(마지막 +1로 실제 값 도출)
    print(f'{floor}{num:02}') # 두 자리 맞추기 method (format 함수보다 단순함!!)
