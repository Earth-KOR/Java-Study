# REST

<br>

**`RE`presentational 표현** <br><br>
**`S`tate 상태** <br><br>
**`T`ransfer 전달**

<br>

<hr>

<br>

## 초창기 웹?

<br>

<p align="center"> <img src="https://user-images.githubusercontent.com/62025746/95959070-f79cb100-0e3c-11eb-9654-89188a561dec.png" width="600px"> </p>

<br>

<hr>

<br>

## REST API란 - 1

<br>

<p align="center"> <img src="https://user-images.githubusercontent.com/62025746/95959060-f53a5700-0e3c-11eb-87f6-5d37f022acf3.png" width="600px"> </p>

<br>

<hr>

<br>

## REST API란 - 2

<br>

<p align="center"> <img src="https://user-images.githubusercontent.com/62025746/95959064-f66b8400-0e3c-11eb-9c60-c175fa1ebdc6.png" width="600px"> </p>

<br>

<hr>

<br>

## 다양한 API 명령어들

<br>

<p align="center"> <img src="https://user-images.githubusercontent.com/62025746/95959066-f7041a80-0e3c-11eb-8fc2-b43b09093c6b.png" width="600px"> </p>

<br>

<hr>

<br>

## 왜 REST API를 쓰는가 ?

 * 분산 시스템을 찾기 위해서
  * 모듈, 기능별로 분리하기 쉬워졌다. <br>
  * 어떤 다른 모듈 또는 애플리케이션들이라도 RESTful API 를 통해 상호간에 통신을 할 수 있기 때문
 * WEB 브라우저 외의 클라이언트를 위해서 (멀티 플랫폼)
  * 데이터만 주고받기 때문에 여러 클라이언트가 자유롭고 부담없이 데이터를 이용 할 수있다.

<br>

<hr>

<br>

## RESTful 이란 ?

**REST의 제약조건을 모두 만족하는 구조를 가진 시스템을 Restful 이라고 함**

<br>

<hr>

<br>

## RESTful의 제약조건 ?

<p align="center"> <img src="https://user-images.githubusercontent.com/62025746/95960292-8b22b180-0e3e-11eb-8378-566482f7084d.png" width="600px"> </p>

<br>

<hr>

<br>

## Richardson Maturity Model ?

<p align="center"> <img src="https://user-images.githubusercontent.com/62025746/95960618-e81e6780-0e3e-11eb-9e67-f14579dff511.png" width="600px"> </p>

<br><br>

**레너드 리처드슨(Leonard Richardson)은 REST가 얼마나 성숙했는지 알 수 있는 아주 유용한 모델을 제시했습니다. 이 모델에 따르면 REST의 성숙도는 다음 4단계로 구분됩니다.**
<br>
 * 레벨 0: 클라이언트는 서비스별로 유일한 URL 끝점에 HTTP POST 요청을 하여 서비스를 호출합니다. 요청을 할 때마다 어떤 액션을 수행할지, 그 대상(예: 비즈니스 객체)은 무엇인지 지정합니다. 필요한 매개변수도 함께 전달합니다. <br><br>
 * 레벨 1: 서비스는 리소스 개념을 지원합니다. 클라이언트는 수행할 액션과 매개변수가 지정된 POST 요청을 합니다. <br><br>
 * 레벨 2: 서비스는 HTTP 동사를 이용해서 액션을 수행하고(예: GET은 조회, POST는 생성, PUT은 수정), 요청 쿼리 매개변수 및 본문, 필요 시 매개변수를 지정합니다. 덕분에 서비스는 GET 요청을 캐싱하는 등 웹 인프라를 활용할 수 있습니다.<br><br>
 * 레벨 3: 서비스를 HATEOAS(Hypertext As The Engine Of Application State, 애플리케이션 상태 엔진으로서의 하이퍼미디어) 원칙에 기반하여 설계합니다. HATEOAS는 GET 요청으로 반환된 리소스 표현형에 그 리소스에 대한 액션의 링크도 함께 태워 보내자는 생각입니다. 가령 클라이언트는 GET 요청으로 주문 데이터를 조회하고 이때 반환된 표현형 내부 링크를 이용해서 해당 주문을 취소할 수도 있습니다. HATEOAS를 사용하면 하드 코딩한 URL을 클라이언트 코드에 욱여넣지 않아도 됩니다

<hr>

<br>



# AJAX

<br>

**`A`synchronous 비동기** <br><br> 
**`J`avaScript** <br><br>
**`A`nd** <br><br>
**`X`ml**

<br>

<hr>

<br>

## 초창기 웹?

<br>

<p align="center"> <img src="https://user-images.githubusercontent.com/62025746/95962124-efdf0b80-0e40-11eb-9aa8-be93a96b077b.png" width="600px"> </p>

<br>

<hr>

<br>

## Ajax의 장점 - 1

<br>

<p align="center"> <img src="https://user-images.githubusercontent.com/62025746/95962129-f077a200-0e40-11eb-918c-7f60936d888d.png" width="600px"> </p>

<br>

<hr>

<br>


## Ajax의 장점 - 2

**비동기 방식으로 페이지를 새로고침 하지 않고도 필요한 데이터를 받아와서 내용을 업데이트 하기 때문에 클라이언트의 대기시간을 줄일 수 있다.**

<br>

<p align="center"> <img src="https://user-images.githubusercontent.com/62025746/95962130-f1103880-0e40-11eb-92d4-4293d0195a00.png" width="600px"> </p>

<br><br>
### 동기/비동기 방식의 차이점
<br>

 * 동기(synchronous : 동시에 일어나는)
   * 동기는 말 그대로 동시에 일어난다는 뜻입니다. 요청과 그 결과가 동시에 일어난다는 약속인데요. 바로 요청을 하면 시간이 얼마가 걸리던지 요청한 자리에서 결과가 주어져야 합니다. <br><br>
   * 요청과 결과가 한 자리에서 동시에 일어남 <br><br>
   * A노드와 B노드 사이의 작업 처리 단위(transaction)를 동시에 맞추겠다.
 * 비동기(Asynchronous : 동시에 일어나지 않는)
   * 비동기는 동시에 일어나지 않는다를 의미합니다. 요청과 결과가 동시에 일어나지 않을거라는 약속입니다. <br><br>
   * 요청한 그 자리에서 결과가 주어지지 않음 <br><br>
   * 노드 사이의 작업 처리 단위를 동시에 맞추지 않아도 된다. 
  
  <br><br>
   
### 동기/비동기 방식의 장단점

<br>

 **동기와 비동기는 상황에 따라서 각각의 장단점이 있습니다.**  <br><br>

 **동기방식은 설계가 매우 간단하고 직관적이지만 결과가 주어질 때까지 아무것도 못하고 대기해야 하는 단점이 있고,**  <br><br>

 **비동기방식은 동기보다 복잡하지만 결과가 주어지는데 시간이 걸리더라도 그 시간 동안 다른 작업을 할 수 있으므로 자원을 효율적으로 사용할 수 있는 장점이 있습니다.**



<br>

<hr>

<br>

## 비동기 방식의 종류

 * **$(" ").load( )**
 * **$.get( ),$.post( )**
 * **$.getJSON( )**
 * **$.ajax( )**
 
 <br>
 
 <hr>
 
### 비동기 방식의 종류 - $(" ").load( )

<br>

<p align="center"> <img src="https://user-images.githubusercontent.com/62025746/95962119-ef467500-0e40-11eb-8305-f1fb54d35871.png" width="600px"> </p>

<br>

<hr>

<br>

### 비동기 방식의 종류 - $.get( ),$.post( )

<br>

<p align="center"> <img src="https://user-images.githubusercontent.com/62025746/95962111-ece41b00-0e40-11eb-9905-5fa594ad517a.png" width="600px"> </p>

<br>

<hr>

<br>

### 비동기 방식의 종류 - $.getJSON( )

<br>

<p align="center"> <img src="https://user-images.githubusercontent.com/62025746/95962114-eeadde80-0e40-11eb-9cd2-26a7cc660dd6.png" width="600px"> </p>

<br>

<hr>

<br>

### 비동기 방식의 종류 - $.ajax( )

<br>

<p align="center"> <img src="https://user-images.githubusercontent.com/62025746/95962116-eeadde80-0e40-11eb-9e40-fe92eeee4c07.png" width="600px"> </p>

<br>

<hr>

<br>

