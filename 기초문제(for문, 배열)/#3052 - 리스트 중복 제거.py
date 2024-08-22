# method 1 : list -> set -> list
a = [int(input()) for _ in range(10)]
d = []
for i in range(10):
  d.append(int(a[i])%42)
print(len(list(set(d))))

# method 2 : list comprehension (중요!!)
a = [int(input()) for _ in range(10)]
d = []
[d.append(i%42) for i in a if i%42 not in d] #list comprehension ㅈㄴ예슐이노
print(len(d))

# method 3 : 반복문 이용 (list comprehension의 기본개념)
# method 4 : dict.fromkeys() - 사전자료형 key는 중복X
