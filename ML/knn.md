```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
import joblib
```


```python
 print("knn")
# 1. 데이터 준비
col_names = ['age', 'sex',
             'job', 'hobby',
             'Class']

# csv 파일에서 DataFrame을 생성
dataset = pd.read_csv('shopknn.csv', encoding='UTF-8', header=None, names=col_names)

# DataFrame 확인
print(dataset.shape)  # (row개수, column개수)
print(dataset.info())  # 데이터 타입, row 개수, column 개수, 컬럼 데이터 타입
print(dataset.describe())  # 요약 통계 정보
print(dataset.iloc[0:5])  # dataset.head()
print(dataset.iloc[-5:])  # dataset.tail()
```

    knn
    (126, 5)
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 126 entries, 0 to 125
    Data columns (total 5 columns):
     #   Column  Non-Null Count  Dtype
    ---  ------  --------------  -----
     0   age     126 non-null    int64
     1   sex     126 non-null    int64
     2   job     126 non-null    int64
     3   hobby   126 non-null    int64
     4   Class   126 non-null    int64
    dtypes: int64(5)
    memory usage: 5.0 KB
    None
                  age         sex         job       hobby       Class
    count  126.000000  126.000000  126.000000  126.000000  126.000000
    mean    35.468254    1.444444    2.357143    2.452381    2.587302
    std     13.310860    0.498888    0.924894    1.142679    1.154261
    min     20.000000    1.000000    1.000000    1.000000    1.000000
    25%     24.000000    1.000000    2.000000    1.000000    1.000000
    50%     28.000000    1.000000    3.000000    3.000000    3.000000
    75%     48.750000    2.000000    3.000000    3.000000    4.000000
    max     60.000000    2.000000    4.000000    4.000000    4.000000
       age  sex  job  hobby  Class
    0   28    2    2      2      3
    1   25    2    2      2      2
    2   22    2    2      2      2
    3   22    2    2      2      2
    4   22    2    2      2      3
         age  sex  job  hobby  Class
    121   55    1    1      3      3
    122   56    1    1      3      4
    123   57    1    1      3      3
    124   58    1    1      3      4
    125   57    1    1      3      1
    


```python
# X = 전체 행, 마지막 열 제외한 모든 열 데이터 -> n차원 공간의 포인트
X = dataset.iloc[:, :-1].to_numpy()  # DataFrame을 np.ndarray로 변환
print(X)

# y = 전체 행, 마지막 열 데이터
y = dataset.iloc[:, 4].to_numpy()
print(y)
```

    [[28  2  2  2]
     [25  2  2  2]
     [22  2  2  2]
     [22  2  2  2]
     [22  2  2  2]
     [22  2  2  4]
     [23  2  2  3]
     [24  2  2  4]
     [25  2  3  3]
     [26  2  3  3]
     [27  1  3  2]
     [28  1  3  4]
     [29  1  3  2]
     [24  1  3  4]
     [25  1  3  2]
     [26  1  3  3]
     [27  1  3  2]
     [24  1  3  4]
     [25  1  3  3]
     [26  1  3  2]
     [27  1  3  3]
     [20  2  3  1]
     [22  2  4  1]
     [32  2  3  4]
     [20  2  3  1]
     [33  2  3  1]
     [49  2  2  1]
     [50  2  2  1]
     [52  2  4  3]
     [52  2  2  4]
     [53  2  2  1]
     [54  2  2  2]
     [55  1  1  4]
     [56  1  3  3]
     [57  1  4  2]
     [58  1  1  4]
     [45  1  1  4]
     [46  1  1  3]
     [47  1  1  3]
     [48  1  1  3]
     [49  1  3  3]
     [44  1  1  3]
     [45  1  4  3]
     [46  2  3  1]
     [47  2  3  1]
     [48  2  3  1]
     [49  2  4  1]
     [23  2  3  1]
     [24  2  3  1]
     [24  1  3  3]
     [25  1  3  2]
     [25  1  3  2]
     [25  1  4  3]
     [26  1  1  2]
     [26  1  1  3]
     [27  1  1  3]
     [27  1  1  4]
     [28  1  1  4]
     [28  1  1  1]
     [29  1  1  1]
     [29  1  1  2]
     [20  1  1  1]
     [20  1  1  3]
     [22  2  3  1]
     [22  2  3  1]
     [22  2  3  1]
     [22  2  3  1]
     [23  2  3  1]
     [23  2  3  1]
     [24  2  3  1]
     [24  1  3  1]
     [25  1  3  1]
     [25  1  3  1]
     [25  1  3  3]
     [26  1  3  1]
     [26  1  3  3]
     [27  1  3  2]
     [27  1  3  3]
     [28  1  3  1]
     [28  1  3  2]
     [29  1  3  4]
     [29  1  3  4]
     [20  1  3  4]
     [20  1  3  4]
     [22  2  2  1]
     [22  2  2  1]
     [22  2  2  1]
     [22  2  2  1]
     [23  2  2  1]
     [23  2  2  1]
     [24  2  2  1]
     [24  2  2  1]
     [25  2  2  1]
     [25  2  2  1]
     [40  2  2  1]
     [42  1  3  3]
     [42  1  3  3]
     [43  1  3  3]
     [44  1  1  3]
     [45  1  3  3]
     [46  1  4  3]
     [47  1  3  3]
     [48  1  1  3]
     [49  1  3  3]
     [50  1  1  3]
     [52  2  2  4]
     [52  2  2  4]
     [53  2  2  4]
     [54  2  2  4]
     [55  2  1  4]
     [56  2  2  4]
     [57  2  1  4]
     [58  2  2  4]
     [59  2  2  4]
     [60  2  2  4]
     [38  2  2  4]
     [39  1  4  3]
     [39  1  4  3]
     [52  1  4  3]
     [53  1  1  3]
     [54  1  1  3]
     [55  1  1  3]
     [56  1  1  3]
     [57  1  1  3]
     [58  1  1  3]
     [57  1  1  3]]
    [3 2 2 2 3 3 3 3 3 1 4 4 4 2 4 4 1 4 3 4 4 1 1 2 1 1 2 2 2 3 3 3 3 3 1 3 3
     4 4 1 4 4 4 2 1 2 2 1 2 3 1 2 4 2 2 3 4 4 4 1 3 3 3 1 1 1 1 1 1 1 3 3 3 3
     4 4 4 3 4 3 4 4 2 1 1 1 1 1 1 1 1 1 1 1 1 3 3 3 3 3 3 4 4 4 4 2 2 2 4 2 1
     2 4 3 4 4 4 3 3 4 3 3 4 3 4 1]
    


```python
# 전체 데이터 세트를 학습 세트(training set)와 검증 세트(test set)로 나눔
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=23)
print(len(X_train), len(X_test))

print(X_train[:3])
print(y_train[:3])
```

    100 26
    [[46  1  4  3]
     [54  2  2  4]
     [49  1  3  3]]
    [3 4 4]
    


```python
# k-NN 분류기를 생성
classifier = KNeighborsClassifier(n_neighbors=5)
# 분류기 학습
classifier.fit(X_train, y_train)

# 예측
y_pred = classifier.predict(X_test)
print(len(X_test))
print(y_pred)
print(len(y_pred))

from sklearn.metrics import accuracy_score
print('예측 정확도: {0:.4f}'.format(accuracy_score(y_test, y_pred)))
```

    26
    [4 1 3 1 3 4 2 2 4 3 1 4 4 2 1 3 3 1 4 2 1 1 2 4 1 1]
    26
    예측 정확도: 0.5769
    


```python
# 모델 저장


joblib.dump(classifier, './shopknn.pkl')
```




    ['./shopknn.pkl']




```python
# 모델 불러오기
loaded_model = joblib.load('./shopknn.pkl')
# 예측
loaded_pred = loaded_model.predict(X_test)
print(loaded_pred)
```

    [4 1 3 1 3 4 2 2 4 3 1 4 4 2 1 3 3 1 4 2 1 1 2 4 1 1]
    


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```
