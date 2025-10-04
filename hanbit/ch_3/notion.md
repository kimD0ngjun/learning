# 훈련 세트와 테스트 세트
[유툽 강의](https://www.youtube.com/watch?v=SUpUPXXhE6g&list=PLVsNizTWUw7E2RxZ4aspcR9vNamXccmFE&index=5)
- 일전의 도미와 빙어 분류에서 어차피 정답 데이터를 주고 분류시킨 거니까 100프로 나온 게 의미 없지 않을까
- 시험으로 빗대자면, 공부를 정답지로 한 셈이 아닐까?
```python

from sklearn.neighbors import KNeighborsClassifier

kn = KNeighborsClassifier()
kn.fit(fish_data, fish_target)
kn.score(fish_data, fish_target) # 즉, 이 부분이 좀 위화감이 느껴짐...
```

### 1. 들어가기 전에... 머신러닝 종류부터 정리
- **지도 학습 : 타깃값을 줌. 정답을 미리 알려주고 학습하는 알고리즘**
- **비지도 학습 : 타깃값 없이 데이터만 주고 유용한 결과를 뽑아냄**
- **강화 학습 : 환경에 적응하면서, 그 환경에서 얻은 보상을 최대한 활용하는 분야(알파고 같은...)**
- K-NN 알고리즘은 지도 학습에 속함

### 2. 이전 챕터에서 K-NN 알고리즘 모델의 문제점
- 정답지가 곧 시험 문제였음
- 그래서 **테스트 세트**와 **훈련 세트**를 나눠서 해야 함
- 근데 또 이걸 잘못 나누면 **샘플링 편향 문제**가 생겨요...
```python
from sklearn.neighbors import KNeighborsClassifier

# 학습(훈련)용 : 전부 도미
train_input = fish_data[:35]
train_target = fish_target[:35]

# 예측(평가)용 : 전부 빙어
test_input = fish_data[35:]
test_target = fish_target[35:]

kn = KNeighborsClassifier()
kn.fit(train_input, train_target) # 학습(훈련)
kn.score(test_input, test_target) # 예측(평가)
# 0점 출력, 왜냐면 학습 데이터는 도미고, 평가 데이터는 빙어로만 했으니..(샘플링 편향 이슈)
```
- 결론 : **테스트 세트와 훈련 세트로 나누되, 잘 섞어야 한다**
### 3. 잘 섞기 위한 numpy 모듈
- numpy 모듈은 행렬(다차원 배열)에 특화(참고로 파이썬 배열 요소 타입 전부 동일해야 할 것)
- 사이킷런은 보통 2차원 배열을 기대하고 사용하는 편
```python
import numpy as np

"""
파이썬 리스트의 배열(정확히는 행렬) 처리
"""
input_arr = np.array(fish_data)
target_arr = np.array(fish_target)

"""
데이터를 섞는 방법은 뭐 직접 섞는 것도 방법이지만...
배열 길이가 너무 길면 데이터 섞는 게 비효율적이고 시간도 오래 걸림
그래서 할 수 있는 가장 좋은 방법은 인덱스를 섞는 것임. 어차피 특정 인덱스는 원본 데이터를 참조할 테니까
"""
np.random.seed(42) # 난수 시드를 고정해서, 실행할 때마다 같은 섞임 결과가 나오게 함. 재현성(reproducibility)을 보장
index = np.arange(len(input_arr)) # 인덱스 배열(0부터 48까지)
np.random.shuffle(index) # 섞기

"""
입력(학습) 데이터와 타깃(예측) 데이터는 서로 섞여서는 안 된다
그래서 슬라이싱으로 분별 중
"""
train_input = input_arr[index[:35]] # 파이썬과 다르게 넘파이는 리스트(배열)도 인덱싱에 사용이 가능함
train_target = target_arr[index[:35]]

test_input = input_arr[index[35:]]
test_target = target_arr[index[35:]]
```
