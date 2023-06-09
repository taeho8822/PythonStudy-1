'''
패키지
    모듈 상위 개념
    모듈의 집합을 의미한다

패키지 설치
console> pip install package명
pip install numpy

패키지 삭제
console> pip uninstall package명
'''
import numpy as np


# 1차원 배열 생성
arr1 = np.array([1, 2, 3, 4, 5])

# 2차원 배열 생성
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

# 배열의 크기 확인
print(arr1.shape)  # 출력: (5,)
print(arr2.shape)  # 출력: (2, 3)

# 배열 연산
result = arr1 + 10
print(result)  # 출력: [11, 12, 13, 14, 15]