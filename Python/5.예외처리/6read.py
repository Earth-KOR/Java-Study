# 파일객체에 read 함수는 파일의 내용 전체를 읽어 문자열로 올려준다.

file = open("C:/doit/새파일.txt",'r')

data = file.read()

print(data)

file.close()