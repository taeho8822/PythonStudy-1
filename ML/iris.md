```python
import sklearn

print(sklearn.__version__)

# !에러발생시 anaconda prompt 에서 
# pip install sklearn

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
```

    1.0.2
    


```python
import pandas as pd
# pip install pandas

# 붓꽃 데이터셋 로딩합니다.
iris = load_iris()

# 붓꽃 데이터셋 csv 파일로 생성!
# df = pd.DataFrame(data=iris['data'], columns = iris['feature_names'])
# df.to_csv('iris.csv', sep = ',', index = False)

# iris.data 채집한 데이터 iris_data
iris_data = iris.data  

# iris.targe은 붓꽃 데이터셋의 결정값.
iris_label = iris.target
print('iris_label 값:', iris_label)
print('target_names 값:', iris.target_names)

# 붓꽃 데이터 셋을 자세히 보기위해 DataFrame으로 변환.
iris_df = pd.DataFrame(data=iris_data, columns=iris.feature_names)
iris_df['label'] = iris.target
iris_df.head(3)
```

    iris_label 값: [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
     0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
     1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2
     2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
     2 2]
    target_names 값: ['setosa' 'versicolor' 'virginica']
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>sepal length (cm)</th>
      <th>sepal width (cm)</th>
      <th>petal length (cm)</th>
      <th>petal width (cm)</th>
      <th>label</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5.1</td>
      <td>3.5</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4.9</td>
      <td>3.0</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.7</td>
      <td>3.2</td>
      <td>1.3</td>
      <td>0.2</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 학습(train) 데이터 테스트(test) 데이터 분류
X_train, X_test, y_train, y_test = train_test_split(iris_data, iris_label, 
                                                    test_size=0.2, random_state=11)
```


```python
# DecisionTreeClassifier 모델 객체생성
dt_clf = DecisionTreeClassifier(random_state=11)

# 학습 수행
dt_clf.fit(X_train, y_train)
```




    DecisionTreeClassifier(random_state=11)




```python
# 테스트 데이터로 예측
pred = dt_clf.predict(X_test)
```


```python
from sklearn.metrics import accuracy_score
print('예측 정확도: {0:.4f}'.format(accuracy_score(y_test, pred)))
```

    예측 정확도: 0.9333
    


```python

```
