파일명 sqlScript.md

**0. User & Database 생성**

- mysql 접속
```
mysql -u root 
```
- 외부 접속 권한 주기
```
- grant all privileges on *.* to root@"%" identified by 'qwe123' with grant option;
```
- Database 생성
```
CREATE DATABASE hr;
```
- 원격접속용 MySql 계정
```
# CREATE USER 'name'@'ip' IDENTIFIED BY 'password';
CREATE USER 'scott'@'%' IDENTIFIED BY 'tiger';
```
- 해당 계정에 필요한 권한을 준다.
``` 
GRANT ALL PRIVILEGES ON *.* TO 'scott'@'%' WITH GRANT OPTION;

FLUSH PRIVILEGES;
```


