# 딕셔너리란?
#리스트와 튜플등에서는 정수인 인덱스를 가지고 순차적으로 각 요소에 접근 할 수 있었다면,
#딕셔너리는 단어 그대로 사전과 같이 별도로 정의 키(key)를 통해 각 요소에 접근 할 수 있도록 만들어진 데이터타입이다.

#딕셔너리 선언하기 문법
#딕셔너리명 = { 요소1, 요소2, 요소3... }
#요소 = 키(key)  : 값 (value)

#설명 : 딕셔너리는 중괄호 {}로 감싸서 선언하며, 딕셔너리의 각 요소들은 쉼표,를 사용하여 구분 합니다.
#       이러한 딕셔너리의 요소는 또 다시 key와 value의 한쌍으로 구성되며 이들은 콜론 : 으로 연결 됩니다.

#딕셔너리 만들기 예제
dic = {'name' : 'pay' , 'phone' : '010' , 'birth' : '1118'}

#딕셔너리 데이터를 쌍으로 추가하는 예제
a = {1:'a'}

a[2] = 'b' # {2:'b'} 쌍 추가
print(a)

a['name'] = 'pay' # 딕셔너리에 'name' : 'pay'라는 쌍을 추가 시킴
print(a)

a[3] = [1,2,3] # 딕셔너리 key는 3 value [1,2,3]을 가지는 한 쌍을 추가 시킴
print(a)



# 딕셔너리 요소 삭제하기 예제
#del 함수를 사용해서 del a[key]처럼 입력하면 지정한 key에 해당하는 {key:value}쌍이 삭제 된다

#key가 1인 key:value를 쌍으로 삭제

del a[1]
print(a)

#딕셔너리에서 key를 사용해 value 얻기
#예제
grade = {'pay' : 10 , 'julliet':99}
#key가 'pay'의 딕셔너리의 value 10을 되돌려 받자
print(grade['pay'])
print(grade['julliet'])

#딕셔너리 관련 함수
#딕셔너리를 자유자재로 사용하기 위해 딕셔너리가 자체적으로 가지고 있는 관련 함수를 사용 해보자

#1. key들을 요소로 갖는 리스트 만들기
#예제
a = {'name' : 'pay' , 'phone':'011', 'birth' : '1110'}
d = a.keys() # 딕셔너리 a의 key 값들만 모아서 dict_keys 객체에 저장한 후 반환
print(d) # dict_keys(['name' , 'phone','birth']) 객체가 출력됨!

#참고 dict_keys 객체를 리스트로 변환하려면 ?
list = list(a.keys())
print(list) # ['name','phone','birth'] 리스트 객체 출력됨

#2. value들을 요소로 갖는 리스트 만들기
#key를 얻는것과 마찬가지 방법으로 value만 얻고 싶다면 value 함수를 사용하면 된다.
a = {'name' : 'pay', 'phone' : '011' , 'birth':'1110'}
d = a.values()
print(d)

#3. ket, value 쌍으로 얻기 (item함수사용)
# item 함수는 key와 value의 쌍을 튜플로 묶은 값을 dict_items 객체로 돌려준다.
#예제
a = {'name' : 'pay', 'phone' : '011' , 'birth':'1110'}
b=a.items()
print(b) # dict_items([('name', 'pay'), ('phone', '011'), ('birth', '1110')])

#4. key:value쌍 모두 지우기
# clear 함수는 딕셔너리 안의 모든 요소를 삭제 한다
# 빈 리스트를 [], 빈튜플을 () 로 표현하는 것과 마찬가지로 빈 딕셔너리로 {}로 표현한다.
#예제
a = {'name' : 'pay', 'phone' : '011' , 'birth':'1110'}
a.clear()
print(a) # {}

#5. key로 value 얻기
#   get(x)함수는 x라는 key에 대응되는 value를 돌려 준다.
#예제
a = {'name' : 'pay' , 'phone':'011'}
b = a.get('name') # 'name'  in a를 호출하면 참(True)을 돌려준다
print(b)

