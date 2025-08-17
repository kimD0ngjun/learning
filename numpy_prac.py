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

# 0부터 9까지
range_vec = np.arange(10)
print(range_vec)

n = 2
range_n_step_vec = np.arange(1, 10, n) # 파이썬 슬라이싱 문법 그대로 적용
print(range_n_step_vec)

# 30까지 어레인징하고 5행 6열의 배열로 리셰이핑
reshape_mat = np.array(np.arange(30)).reshape((5,6))
print(reshape_mat)

"""
행렬의 슬라이싱, 인덱싱
"""
# numpy는 파이썬 슬라이싱 그대로 통용 가능
# [행에 대한 슬라이싱, 열에 대한 슬라이싱]
mat = np.array([[1, 2, 3], [4, 5, 6]])
print(mat)

# 첫번째 행 출력
slicing_mat = mat[0, :]
print(slicing_mat)

# 두번째 행 두번째 요소부터 2칸씩
slicing_mat = mat[1, 1::2]
print(slicing_mat)

# 두번째 열 출력
slicing_mat = mat[:, 1]
print(slicing_mat)

# 특정 위치의 원소만을 갖고오거나 그런 원소들 간의 조합으로는
# 인덱싱을 써야 함. [행의 인덱스, 열의 인덱스]
mat = np.array([[1, 2], [4, 5], [7, 8]])
print(mat)

# 1행 0열의 원소
# => 0부터 카운트하므로 두번째 행 첫번째 열의 원소.
print(mat[1, 0])

# mat[[2행, 1행],[0열, 1열]]
# 각 행과 열의 쌍을 매칭하면 2행 0열, 1행 1열의 두 개의 원소.
indexing_mat = mat[[2, 1],[0, 1]]
print(indexing_mat)

"""
행렬 사칙연산
* 벡터곱과 다르다 그냥 요소간 위치 맞춰서 사칙연산할 뿐
* 행렬 구조가 서로 다르면 에러가 발생
"""
x = np.array([1,2,3])
y = np.array([4,5,6])

# result = np.add(x, y)와 동일.
result = x + y
print(result)

# result = np.subtract(x, y)와 동일.
result = x - y
print(result)

# result = np.multiply(result, x)와 동일.
result = result * x
print(result)

# result = np.divide(result, x)와 동일.
result = result / x
print(result)

# 행렬 간 곱을 하려면 np.dot(행렬1, 행렬2) 메소드를 호출한다
mat1 = np.array([[1,2],[3,4]])
mat2 = np.array([[5,6],[7,8]])
mat3 = np.dot(mat1, mat2)
print(mat3)