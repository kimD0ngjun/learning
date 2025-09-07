import numpy as np # 벡터 생성 + 노름 연산용 numpy 모듈

print("=== 벡터의 크기 계산 ===")

# 2차원 벡터
v2d = np.array([3, 4])
print(f"벡터 v = {v2d}")

# L2 노름(유클리드 크기)
l2_norm = np.linalg.norm(v2d)
l2_norm = np.linalg.norm(v2d, ord=2) # ord 파라미터는 디폴트가 2임
print(f"L2 노름: {l2_norm}")

# 직접 유클리드 계산
manual_l2 = np.sqrt(np.sum(v2d ** 2))
print(f"수동 계산 L2 노름: {manual_l2}")

# L1 노름 (맨하탄 거리)
l1_norm = np.linalg.norm(v2d, ord=1)
print(f"L1 노름: {l1_norm}")

# L∞ 노름 (최대 노름)
linf_norm = np.linalg.norm(v2d, ord=np.inf)
print(f"L∞ 노름: {linf_norm}")


print("\n=== 3차원 벡터의 크기 ===")

# 3차원 벡터
v3d = np.array([2, 3, 6])
print(f"3차원 벡터: {v3d}")
print(f"크기: {np.linalg.norm(v3d):.2f}")

print("\n=== 벡터 정규화 ===")

# 정규화 전
original = np.array([300, 400])
print(f"원래 벡터: {original}")
print(f"원래 크기: {np.linalg.norm(original)}")

# 정규화
normalized = original / np.linalg.norm(original)
print(f"정규화된 벡터: {normalized}")
print(f"정규화된 벡터의 크기: {np.linalg.norm(normalized):.10f}")

# NumPy의 정규화 함수 사용
normalized_v2 = original / np.linalg.norm(original)
print(f"검증: {np.allclose(normalized, normalized_v2)}")

print("\n=== 벡터 간 거리 계산 ===")

# 두 점 사이의 거리
point_a = np.array([1, 2])
point_b = np.array([4, 6])
print(f"점 A: {point_a}")
print(f"점 B: {point_b}")

# 유클리드 거리
euclidean_dist = np.linalg.norm(point_a - point_b)
print(f"유클리드 거리: {euclidean_dist}")

# 맨하탄 거리
manhattan_dist = np.linalg.norm(point_a - point_b, ord=1)
print(f"맨하탄 거리: {manhattan_dist}")