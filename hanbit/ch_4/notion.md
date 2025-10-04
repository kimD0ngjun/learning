# 데이터 전처리
[유툽 강의](https://www.youtube.com/watch?v=Y0IPajPyqn8&list=PLVsNizTWUw7E2RxZ4aspcR9vNamXccmFE&index=6)
- 지난번에는 **모델의 학습 편향성 개선**
- 이번에는 모듈 잘 활용해보며 학습훈련 세트와 예측테스트 세트로 나눔

### 1. 예상과 다르다면...?
- 도미라고 예상한 게 빙어라고 출력되는 케이스
- 그 원인은 산점도에서 x축(길이)과 y축(무게)의 스케일 범위 표준이 다르기 때문

### 2. 데이터 특성들의 스케일 차이
- 특성들의 최소 최대 범위 정수값의 편차가 크기 때문에 이를 비율로 통일시키는 게 맞음
- 정수 범위로 맞추면 오히려 그래프 가독성이 떨어지므로...
```python
# 좋지 않아요...
plt.scatter(train_input[:,0], train_input[:,1])
plt.scatter(25, 150, marker='^')
plt.scatter(train_input[indexes,0], train_input[indexes,1], marker='D')
plt.xlim((0, 1000)) # x축의 범위를 조정하는 함수...지만 잘못된 선택
plt.xlabel('length')
plt.ylabel('weight')
plt.show()
```
- **단순히 K 최근접 이웃 외에도 로지스틱 회귀, 선형 회귀, 심지어 인공신경망 알고리즘 등에서도 특성의 스케일 표준을 통일하는 것이 매우 중요함**
- 예외적으로 트리 기반 모델은 특성 스케일의 영향을 안 받는단다.. 오 신기해...
- 이 스케일을 맞추는 과정이 곧 오늘 과정의 **데이터 전처리**

### 3. 데이터 전처리 : 스케일 범위 표준 통일
> 계산식 = (특성값 - 평균) / 표준편차
- 평균을 뺀다는 건, 데이터 중심을 0으로 이동
- 표준편차로 나눈다는 건, 데이터 폭(스케일)을 1로 조정
```python
mean = np.mean(train_input, axis=0) # 평균 계산, 열 특성(세로) 방향으로 -> 길이의 평균과 무게의 평균 연산
std = np.std(train_input, axis=0) # 표준편차 계산, 열 특성(세로) 방향으로 -> 길이의 표준편차와 무게의 표준편차 연산

train_scaled = (train_input - mean) / std # numpy의 차원 확장(broadcasting) 덕분에 이런 연산이 가능... 평균과 표준편차를 각 행에 복사해 연산
print(train_scaled)
```
- 이런 연산이 그냥 파이썬에선 안되지만, numpy의 브로드캐스팅 때문에 가능
- 이상한 물고기 데이터도 역시 똑같이 전처리해야 함
```python
"""
다시 모델을 학습 훈련하고 예측 테스트 해보자
"""
kn.fit(train_scaled, train_target) # 새롭게 학습 훈련
test_scaled = (test_input - mean) / std
kn.score(test_scaled, test_target) # 새롭게 예측 테스트, 역시나 100점

distances, indexes = kn.kneighbors([new])
print(train_scaled[indexes]) # 가까운 이웃들
print(distances) # 가까운 이웃들 거리
print(train_target[indexes]) # 가까운 이웃들 정체, 전부 도미네요:)

# 다시 이웃 5개를 찍어보자
plt.scatter(train_scaled[:,0], train_scaled[:,1])
plt.scatter(new[0], new[1], marker='^')
plt.scatter(train_scaled[indexes,0], train_scaled[indexes,1], marker='D')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()
```
### 4. 결론
- **특성 스케일링**은 수많은 데이터 전처리 중 하나
- 그 외에도 결측치 처리, 이상치 처리, 범주형 데이터 인코딩, 적합한 특성 선택, 샘플링 등 다양한 데이터 전처리 과정이 존재