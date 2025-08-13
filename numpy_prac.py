# https://wikidocs.net/217157
import numpy as np

"""
numpy 모듈과 math 모듈의 차이
math: 단일 숫자 스칼라에 대한 연산, int와 float 위주, 삼각함수 로그 등등...
numpy: 수치연산 및 배열 중심, 다차원 배열 기반 행렬 벡터 통계 등등...
"""

vec = np.array([1, 2, 3, 4, 5])
print(vec) # 1차원 벡터

mat = np.array([[10, 20, 30], [60, 70, 80]])
print(mat) # 2차원 벡터

print('vec의 타입 :',type(vec))
print('mat의 타입 :',type(mat))

"""
ndarray에서 축(axis, ndim): 데이터 쌓인 갯수 == 차원
ndarray에서 크기(shape): 각 축마다의 원소 갯수
"""

print(vec.ndim) # 1
print(vec.shape) # (5, ) -> 1개니까 차원이 1차원 + 요소 5개
print(mat.ndim) # 2
print(mat.shape) # (2, 3) -> 2차원(즉 2행)의 요소 3개

zero_mat = np.zeros((2, 3)) # 모든 원소가 0으로 채워진 2행 3열 배열(수치는 부동소수점 float64이므로 소숫점이 붙음)
print(zero_mat)
one_mat = np.ones((3, 2)) # 모든 원소가 1로 채워진 3행 2열 배열
print(one_mat)

same_value_mat = np.full((2, 3), True) # 모든 원소가 True로 채운 2행 3열 배열
print(same_value_mat)

eye_mat = np.eye(3) # 대각선값이 1이고 나머지가 0인 단위행렬 생성
print(eye_mat)

random_mat = np.random.random((2,2)) # 임의의 값으로 채워진 배열 생성
print(random_mat)