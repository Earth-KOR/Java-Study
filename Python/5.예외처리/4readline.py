# 특정 파일의 첫번째 줄을 읽어오는 예제
f = open("C:/doit/새파일.txt",'r')
line = f.readline()
print(line)

# 특정 파일의 모든 줄을 읽어오는 예제
f = open("C:\doit\새파일.txt",'r') #파일을 읽기모드로 연다

while True :  # 무한 반복 하면서
    line = f.readline() # 한줄을 읽어 와 line 변수에 저장
    if not line : # 만약 더이상 읽을 줄이 없으면?
        break # 반복문을 빠져 나감
    print(line) # 한줄 단줄로 읽어 들인 내용을 출력

f.close() # File객체 자원 해체