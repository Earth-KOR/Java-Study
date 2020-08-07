# readLines함수를 이용하여 특정 파일의 모든 줄을 읽어서 각각의 요소로 갖는 리스트로 돌려주는 예제

f = open("C:\doit\새파일.txt",'r')

lines = f.readlines() # ["1번째 줄입니다", "2번째 줄입니다","3번째 줄입니다",...]
                        # 읽어 들인 값을 리스트에 저장하여 반환


for line in lines :
    print(line, end="")

f.close()

