### 아나콘다 가상환경 
가상환경을 만들어서 가상환경 별로 독립적인 패키지 버전 관리가 가능하다는 장점

* * *
#### 아나콘다 프롬프트에서 가상환경 만들기
  
아나콘다 프롬프트 실행

- 아나콘다에 존재하는 환경 목록을 보여주는 명령어
```
conda info --envs
```

- 가상환경 추가
```
conda create -n 가상환경명
```

- 가상환경 활성화
```
conda activate 가상환경명
```

- 가상환경 비활성화
```
conda deactivate
```
- 가상환경 삭제
```
conda env remove -n 가상환경명
```

- 패키지 설치
```
conda install -n 가상환경명 패키지명
```

- 패키지 삭제
```
conda uninstall -n 가상환경명 패키지명
```

- 파이썬 버젼리스트
```
conda search python
```
- 파이썬 버젼 변경
```
conda install python=x.x.x
```

