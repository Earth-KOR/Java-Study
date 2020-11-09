# REST

<br>

**`RE`presentational 표현**   <br>
**`S`tate 상태** <br><br>
**`T`ransfer 전달**


<br>

<hr>

<br>

## 초창기 웹?

<br>

<p align="center"> <img src="https://user-images.githubusercontent.com/62025746/95959070-f79cb100-0e3c-11eb-9654-89188a561dec.png" width="600px"> </p>

<br>

**초창기의 웹은 하나의 request를 보내면 그 request에 맞는 html/css 코드 전체를 주었다. <br>
이러한 방식은 웹 페이지의 규모가 작을 떄에는 큰 상관이 없었지만 현재같이 대용량의 홈페이지나 <br>
수 많은 데이터가 이동하는 현대시대에는 성능 문제에 큰 결함이 발생하였다.**

<hr>

<br>

## REST API란 - 1

<br>

<p align="center"> <img src="https://user-images.githubusercontent.com/62025746/95959060-f53a5700-0e3c-11eb-87f6-5d37f022acf3.png" width="600px"> </p>

<br>

**이러한 문제점을 개선하기 위해서 나온게 REST인데 서버에 보내는 URL에 특정 명령과 파라미터 값을 넣음으로써 <br> http protocol을 더 유연하게 사용 할 수 있었고, 서버도 전체 html/css를 주는것이 아닌 사용자가 요청한 데이터를 JSON/XML 형태로 줌으로써 형태를 바꾸었다.**

<hr>

<br>

## REST API란 - 2

<br>

<p align="center"> <img src="https://user-images.githubusercontent.com/62025746/95959064-f66b8400-0e3c-11eb-9c60-c175fa1ebdc6.png" width="600px"> </p>

<br>

**해당 사진은 GET방식으로 원하는 정보를 요청 했을 떄의 예시인데, Server가 해당 url의 주소를 받고 싶다는 명령을 받고, <br> DataCenter에서 특정 데이터를 받은 뒤, 사용자에게 JSON/XML 형태로 돌려주고 있다**

<hr>

<br>

## 다양한 API 명령어들

<br>

<p align="center"> <img src="https://user-images.githubusercontent.com/62025746/95959066-f7041a80-0e3c-11eb-8fc2-b43b09093c6b.png" width="600px"> </p>

<br>

<hr>

**REST에는 GET 뿐만 아니라 다양한 명령어가 존재하고, REST Client 라는 구글앱을 사용하여 보다 편리하게 REST를 Request 할 수 있다!**

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

**초창기의 웹은 전체 부분 중 일부분의 정보가 바뀌었을 떄, 전체 소스를 reload하여 클라이언트에게 전달 해 주었다 <br> 이러한 방법은 소규모의 페이지에서는 상관이 없지만 대규모의 홈페이지에는 큰 성능저하를 불러 일으켰고 <br> 새로고침 버튼을 눌러야 정보가 업로드되는 불편함이 존재하였다.**

<hr>

<br>

## Ajax의 장점 - 1

<br>

<p align="center"> <img src="https://user-images.githubusercontent.com/62025746/95962129-f077a200-0e40-11eb-918c-7f60936d888d.png" width="600px"> </p>

<br>

**Ajax의 첫 번째 장점은 중간에 Ajax Engine이 생김으로써 사용자는 일부분의 javascript만 요청하게 되고 그 요청을 받은 engine은 Server에서 이벤트의 발생을 요청합니다. <br> 해당 이벤트를 받은 server는 xml 데이터 형식으로 돌려주고 engine은 이 데이터를 html/css 형식으로 변환하게 사용자에게 돌려줍니다** 

<hr>

<br>


## Ajax의 장점 - 2

<br>

<p align="center"> <img src="https://user-images.githubusercontent.com/62025746/95962130-f1103880-0e40-11eb-92d4-4293d0195a00.png" width="600px"> </p>

<br>

**Ajax의 두 번째 장점은, 비동기 방식으로 페이지를 새로고침 하지 않고도 필요한 데이터를 받아와서 내용을 업데이트 하기 때문에 클라이언트의 대기시간을 줄일 수 있다.**


<br>
<br>

### 동기/비동기 방식의 차이점

<br>

 * 동기 (synchronous : 동시에 일어나는) <br><br>
   * 동기는 말 그대로 동시에 일어난다는 뜻입니다. 요청과 그 결과가 동시에 일어난다는 약속인데요. 바로 요청을 하면 시간이 얼마가 걸리던지 요청한 자리에서 결과가 주어져야 합니다. <br><br>
   * 요청과 결과가 한 자리에서 동시에 일어남 <br><br>
   * A노드와 B노드 사이의 작업 처리 단위(transaction)를 동시에 맞추겠다. <br><br>
 * 비동기 (Asynchronous : 동시에 일어나지 않는) <br><br>
   * 비동기는 동시에 일어나지 않는다를 의미합니다. 요청과 결과가 동시에 일어나지 않을거라는 약속입니다. <br><br>
   * 요청한 그 자리에서 결과가 주어지지 않음 <br><br>
   * 노드 사이의 작업 처리 단위를 동시에 맞추지 않아도 된다. 
  
  <br><br>
   
### 동기/비동기 방식의 장단점

<br>

 동기와 비동기는 상황에 따라서 각각의 장단점이 있습니다.  <br><br>

 동기방식은 설계가 매우 간단하고 직관적이지만 결과가 주어질 때까지 아무것도 못하고 대기해야 하는 단점이 있고 <br><br>

 비동기방식은 동기보다 복잡하지만 결과가 주어지는데 시간이 걸리더라도 그 시간 동안 다른 작업을 할 수 있으므로 자원을 효율적으로 사용할 수 있는 장점이 있습니다.



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

# 의존성 주입 (DI)

<br><br>

## Dependency Injection 이란?

**객체 자체가 아니라 Framework에 의해 객체의 의존성이 주입되는 설계 패턴**

<br>

<p align="center"> <img src="https://user-images.githubusercontent.com/62025746/95982681-5bce6d80-0e5b-11eb-8aaa-1c304af96423.png" width="600px"> </p>

<br><br>

## 의존성 주입 방법

 * Contructor Injection
   * 생성자를 통한 전달
   * `<constructor-arg ref="cat"></constructor-arg>`
 * Method(Setter) Injection
   * setter()을 통한 전달
   * `<property name="myName" value="poodle"></property>`
 * Field Injection
   * 멤버 변수를 통한 전달
   
<br><br>

## 의존성 주입의 장점

* 재사용성을 높여줍니다. <br> 
* 테스트에 용이합니다. <br>
* 코드도 단순화 시켜줍니다. <br>
* 종속적이던 코드의 수도 줄여줍니다. <br>
* 왜 사용하는 지 파악하기가 수월합니다. 코드를 읽기 쉬워지는 점이 있습니다. <br> 
* 종속성이 감소합니다. 구성 요소의 종속성이 감소하면, 변경에 민감하지 않습니다. <br>
* 결합도(coupling)는 낮추면서 유연성과 확장성은 향상시킬 수 있습니다. <br> 
* 객체간의 의존관계를 설정할 수 있습니다. <br>
* 객체간의 의존관계를 없애거나 줄일 수 있습니다. <br>

<br><br>

## 예시

<br>

<p align="center"> <img src="https://user-images.githubusercontent.com/62025746/95982506-26c21b00-0e5b-11eb-894f-b5a31d5db2b4.png" width="600px"> </p>

<br>

1. AnimalType에 대한 구체적인 Class를 생성한다. <br>
  - Dog Class, Cat Class <br><br>
2. PetOwner 객체에 AnimalType 객체를 전달한다. <br>
  - Contructor Injection <br><br>
3. 생성자를 통한 전달 <br>
  - `<constructor-arg ref="cat"></constructor-arg>` <br><br>
4. Method(Setter) Injection <br>
  - setter()을 통한 전달 <br>
  - `<property name="myName" value="poodle"></property> `<br><br>
5. Field Injection <br>
  - 멤버 변수를 통한 전달 <br>

개발자가 할 일은 주입할 것에 대한 Class를 작성(Dog, Cat 등)하는 것 ! <br>

출처 : https://gmlwjd9405.github.io/2018/11/09/dependency-injection.html


# 공공데이터 값 가져오기

## 태그 안의 태그 및 태그 내부의 값 가져오기

<br>

<p align="center"> <img src="https://user-images.githubusercontent.com/62025746/96097411-deaf0100-0f0b-11eb-9ac5-b9f710c463b7.png" width="600px"> </p>

<br>

**다음과 같은 tag안의 tag 값을 가져오는 방법과 tag 내부에 있는 값을 가져오는걸 배워보겠습니다!**
<br>
<hr>

<p align="center"> <img src="https://user-images.githubusercontent.com/62025746/96097413-df479780-0f0b-11eb-87ea-8386354c8c7f.png" width="600px"> </p>

<br>

**DocumentURL 변수에 데이터를 가져올 주소를 넣어주고 태그에 접근하기 위한 xpath를 생성하고 특정 태그의 값을 담을 변수를 선언해줍니다!**

<br>
<hr>

<p align="center"> <img src="https://user-images.githubusercontent.com/62025746/96097398-dc4ca700-0f0b-11eb-8fc0-7d7f80f12888.png" width="600px"> </p>

<br>

**URL 변수에 원하는 데이터만 가져오기 위해 파라미터를 추가한 URL 값을 넣습니다** <br><br>

**그 후 앞서 사용한 Document 변수안에 현재 페이지의 데이터를 담습니다.** <br><br>

**evaluate 매서드에 원하는 태그까지 접근함으로써 원하는 데이터를 nodeList안에 리스트 형태로 저장합니다**

<br>
<hr>

<br>

<p align="center"> <img src="https://user-images.githubusercontent.com/62025746/96097402-dd7dd400-0f0b-11eb-8c35-c5556446e8f9.png" width="600px"> </p>

<br>

**가져온 데이터 중에서 SECTION 태그의 갯수를 파악하여 그 수만큼 반복문을 돌리고 가져온 값은 result 변수에 추가시킵니다.**

<br>

<hr>
<br>

<p align="center"> <img src="https://user-images.githubusercontent.com/62025746/96097405-dd7dd400-0f0b-11eb-9743-9ed850c3ab77.png" width="600px"> </p>

<br>

**가져온 데이터 중에서 ARTICLE 태그의 갯수를 파악하여 그 수만큼 반복문을 돌리고 가져온 값은 result 변수에 추가시킵니다.**

<hr>
<br>

<p align="center"> <img src="https://user-images.githubusercontent.com/62025746/96097408-de166a80-0f0b-11eb-9c5b-22780425fed7.png" width="600px"> </p>

<br>

**가져온 데이터 중에서 PARAGRAPH 태그의 갯수를 파악하여 그 수만큼 반복문을 돌리고 가져온 값은 result 변수에 추가시킵니다.**


<hr>
<br>

<p align="center"> <img src="https://user-images.githubusercontent.com/62025746/96097409-deaf0100-0f0b-11eb-9008-3a32920d6576.png" width="600px"> </p>

<br>

**모든 데이터를 가지고있는 result값을 DB에 저장하여 데이터를 사용합니다!**





## 태그 안 Value 값 가져오기

<br>

<p align="center"> <img src="https://user-images.githubusercontent.com/62025746/96095045-0fda0200-0f09-11eb-9912-2c9dc29a6f37.png" width="600px"> </p>

<br>

**다음과 같은 tag안의 데이터들 중에서 가지고오고 싶은 데이터만 파싱하는 방법을 알아보겠습니다.**
<br>
<hr>

<p align="center"> <img src="https://user-images.githubusercontent.com/62025746/96095046-0fda0200-0f09-11eb-8fab-e67a9ff173f8.png" width="600px"> </p>

<br>

**url 변수에 데이터를 가져올 주소와 파라미터 값을 넣어주고 DocumentBuilderFactory , DocumentBuilder, Document 를 이용하여 전체 페이지를 파싱한 데이터를 담는다.**

<br>
<hr>

<p align="center"> <img src="https://user-images.githubusercontent.com/62025746/96095049-10729880-0f09-11eb-9387-f552486d3434.png" width="600px"> </p>

<br>

**root 태그로 접근한 다음, 파싱을 시작 할 시작태그의 변수를 넣어 가져올 데이터의 범위를 좁혀준다!** <br><br>

**좁혀진 데이터들을 Nodelist 변수에 list 형태로 담은 후, Nodelist가 가지고 있는 모든 데이터를 for 반복문과 item 메서드를 이용하여 list 안의 각각의 데이터를 Node 변수에 모두 담아준다.** <br><br>

**getNodeType() 메서드에 가지고 오고 싶은 태그이름을 매개변수에 넣음으로써 해당 태그안의 데이터를 가지고 올 수 있음!**

<br>
<br>

<p align="center"> <img src="(https://user-images.githubusercontent.com/62025746/96095042-0ea8d500-0f09-11eb-8ffa-2b806c2085bd.png" width="600px"> </p>

<br>
<hr>

<br>
<br>

<p align="center"> <img src="https://user-images.githubusercontent.com/62025746/96095054-110b2f00-0f09-11eb-9a66-dd7877e58155.png" width="600px"> </p>

<br>

**getNodeType으로 가져온 데이터를 List 변수에 저장함.**

<br>

<hr>

<br>
<br>

<p align="center"> <img src="https://user-images.githubusercontent.com/62025746/96095057-110b2f00-0f09-11eb-90c6-42998052f599.png" width="600px"> </p>

<br>

**List안에 들어있는 데이터를 DB안에 저장해서 사용함 !**

<br><br><hr>


# JavaScript로 그래프 그리기

<br><br>

## Chart.js 란?

**JavaScript를 이용하여 그래프를 그릴 수 있게 도와주는 플러그인 (Chart.js는 canvas로 그리는 형식)**

<br>
<hr>

## Chart.js 사용방법

<br>
<br>

<p align="center"> <img src="https://user-images.githubusercontent.com/62025746/96148830-9f040b80-0f43-11eb-96a0-6f11fc3384e1.png" width="600px"> </p>

<br>

**위와 같이 body 태그 영역안에 chart를 선언 해줌으로써 그래프를 나타나게 한다!**

<br><br>

<p align="center"> <img src="https://user-images.githubusercontent.com/62025746/96148835-a0353880-0f43-11eb-91f1-28e5f4ac2ae7.png" width="600px"> </p>

<br>

**chart.js의 기본 옵션으로 만드려고 하는 그래프의 여러 설정값을 지정 할 수 있음** <br>

**type에서 line 형의 그래프 말고도 수 많은 다른 형태의 그래프를 그릴 수 있음!**

<br>
<hr>

<br><br>

<p align="center"> <img src="https://user-images.githubusercontent.com/62025746/96148833-a0353880-0f43-11eb-965f-2b69b362c91c.png" width="600px"> </p>

<br>

**한번에 그려지는 그래프가 아닌, 시간에 따라 변화하는 그래프를 그리고 싶다면 setTimeOut 메서드를 이용해서 시간을 조절 할 수가 있음**
