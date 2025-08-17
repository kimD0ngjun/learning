"""
https://wikidocs.net/217157
데이터를 차트, 플롯으로 시각화하는 패키지
"""
import matplotlib.pyplot as plt

plt.title('test') # 제목
"""
(1,2) -> (2,4) -> (3,8) -> (4,6)
"""
plt.plot([1,2,3,4],[2,4,8,6]) # 라인 플롯(선그래프) 드로잉
plt.plot([1.5,2.5,3.5,4.5],[3,5,8,10]) # 라인 새로 추가
plt.xlabel('hours') # x축 레이블
plt.ylabel('score') # y축 레이블
plt.legend(['A student', 'B student']) # 범례 삽입(플롯 메소드 순서대로)
plt.show() # 운영 환경마다 자동으로 보여주기도 함(난 있어야 되더라고...)