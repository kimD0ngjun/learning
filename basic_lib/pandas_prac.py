# https://wikidocs.net/217157
import pandas as pd

"""
시리즈: 1차원 배열의 값에서 각 값에 대응되는 인덱스를 부여할 수 있는 구조

인덱스, 값으로 구성
"""

sr = pd.Series([17000, 18000, 1000, 5000],
               index=["피자", "치킨", "콜라", "맥주"])

print('시리즈 출력 :')
print(sr) # 1차원 데이터 요소에 대해 각각 인덱스를 부여(당연히 내가 커스텀한 인덱스지 리스트 인덱스 x)

print(f"시리즈 값: {sr.values}")
print(f"시리즈 인덱스: {sr.index}")
# 인덱스가 필요한 이유는 데이터의 식별을 용이하게 하기
# 해시와 비슷해보이지만, 해시값이 아닌, 사람이 이해하기 쉬운 레이

"""
데이터프레임: 2차원 리스트를 매개변수로 전달
2차원이므로 행방향 인덱스(index)와 열방향 인덱스(column)가 존재 -> 행렬의 응용 확장 버전
행렬은 숫자만 다루지만 데이터프레임은 다양한 데이터 타입을 다룸

열, 인덱스, 값으로 구성
"""

values = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
index = ['one', 'two', 'three']
columns = ['A', 'B', 'C']

df = pd.DataFrame(values, index=index, columns=columns)

print('데이터프레임 출력 : ')
print(df)

print(f"데이터프레임 열: {df.columns}")
print(f"데이터프레임 인덱스: {df.index}")
print(f"데이터프레임 값: {df.values}")
# 시리즈에선 단순히 인덱스가 값에 매핑됐다면
# 데이터프레임에서는 인덱스가 값에 매핑되는 것 + 값들이 또 각각 열에 의해서도 매핑되는 셈 -> 흡사 엑셀 스프레드시트 같은

"""
csv 파일, sql.. 기타 등등도 읽기 가능
"""
df_csv = pd.read_csv("/Users/kimdongjun/Desktop/example.csv")
print(df_csv) # csv 내의 id 말고 데이터프레임 자체 인덱스 부여 가

print(df_csv.index)