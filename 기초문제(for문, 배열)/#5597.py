# 리스트 초기화: List Comprehension
# [expression for item in iterable]

d = [i for i in range(1, 31)]

for _ in range(28):
  n = int(input())
  d.remove(n)

print(min(d))
print(max(d))
