import numpy as np

"""
numpy 모듈의 array 함수가 그냥 배열이 아닌, 벡터 생성에 최적화된 모듈
"""

print("=== 벡터 덧셈과 뺄셈 ===")

# 벡터 정의
v1 = np.array([3, 2])
v2 = np.array([1, 4])
print(f"벡터 v1: {v1}")
print(f"벡터 v2: {v2}")

# 벡터 덧셈
v_sum = v1 + v2
print(f"v1 + v2 = {v_sum}")

# 벡터 뺄셈
v_diff = v1 - v2
print(f"v1 - v2 = {v_diff}")

print("\n=== 3차원 벡터 연산 ===")

# 3차원 벡터
a = np.array([100, 50, 20])
b = np.array([-10, 30, -5])
print(f"벡터 a: {a}")
print(f"벡터 b: {b}")

# 3차원 벡터 덧셈
result = a + b
print(f"a + b = {result}")

print("\n=== 스칼라 곱 ===")

# 기본 벡터
v = np.array([2, 3])
print(f"원래 벡터 v: {v}")

# 다양한 스칼라 곱
print(f"2배 확대: 2 * v = {2 * v}")
print(f"절반 축소: 0.5 * v = {0.5 * v}")
print(f"반대 방향: -v = {-v}")
print(f"3배 반대: -3 * v = {-3 * v}")

print("\n=== 복합 연산 ===")

# 복합 벡터 연산
u = np.array([1, 2, 3])
v = np.array([4, 5, 6])
w = np.array([7, 8, 9])

# (2u + 3v) - w 계산
result = 2*u + 3*v - w
print(f"u = {u}")
print(f"v = {v}")
print(f"w = {w}")
print(f"2u + 3v - w = {result}")

print("\n=== 벡터 연산 성질 확인 ===")

# 교환법칙 확인
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(f"a + b = {a + b}")
print(f"b + a = {b + a}")
print(f"교환법칙 성립: {np.array_equal(a + b, b + a)}")

# 결합법칙 확인
c = np.array([7, 8, 9])
left = (a + b) + c
right = a + (b + c)
print(f"(a + b) + c = {left}")
print(f"a + (b + c) = {right}")
print(f"결합법칙 성립: {np.array_equal(left, right)}")

# 분배법칙 확인
k = 3
left_dist = k * (a + b)
right_dist = k * a + k * b
print(f"3 * (a + b) = {left_dist}")
print(f"3 * a + 3 * b = {right_dist}")
print(f"분배법칙 성립: {np.array_equal(left_dist, right_dist)}")
