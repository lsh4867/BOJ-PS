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

# z
