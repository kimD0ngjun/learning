# https://wikidocs.net/217157
import pandas as pd

"""
시리즈: 1차원 배열의 값에서 각 값에 대응되는 인덱스를 부여할 수 있는 구조
"""

sr = pd.Series([17000, 18000, 1000, 5000],
               index=["피자", "치킨", "콜라", "맥주"])

print('시리즈 출력 :')
print('-'*15)
print(sr) # 1차원 데이터 요소에 대해 각각 인덱스를 부여(당연히 내가 커스텀한 인덱스지 리스트 인덱스 x)

print(f"시리즈 값: {sr.values}")
print(f"시리즈 인덱스: {sr.index}")
# 인덱스가 필요한 이유는 데이터의 식별을 용이하게 하기 위함