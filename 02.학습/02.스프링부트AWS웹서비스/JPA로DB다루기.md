# [스프링 부트와 AWS로 혼자 구현하는 웹 서비스] 스프링 부트에서 JPA로 데이터베이스 다루기
## 데이터베이스 다루기

### SQL Mapper
- ex) iBatis, MyBatis
- 쿼리를 매핑
- SQL작성 시간이 많이 소요됨
- 테이블 모델링에 집중하게 됨
=> 객체지향 프로그래밍과 패러다임이 맞지 않음

### 자가 표준 ORM기술인 JPA
- 객체를 매핑
=> 관계형 데이터베이스를 이용하는 프로젝트에서 객체지향 프로그래밍 가능


## JPA 소개
### 기존의 문제점
#### 1. SQL 코드 증가
- 관계형 데이터베이스는 SQL만 인식할 수 있다.
- 각 테이블마다 CRUD SQL을 매번 생성하다보면 SQL의 비중이 높아진다.
- 그에 따라 유지보수의 어려움이 있다.
#### 2. 패러다임 불일치
왜 필요한가?
- 현대 웹 애플리케이션에서 Oracle, MySQL, MSSQL 등의 RDB를 쓰지 않은 경우가 드물다.


- 따라서, 객체를 관계형 데이터베이스에서 관리하는 것이 중요하다.
