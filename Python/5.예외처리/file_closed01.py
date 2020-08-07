 # 예제. 파일을 열고 있으면 해당 파일을 이동하거나 덮어 씌우거나 하는 것이 불가능 해집니다

# 따라서 프로그램에서 파일을 열었으면 무조건 닫아야 합니다
# 파일을 제대로 닫았는지 파일객체의 closed 속성으로 알수 있습니다.

# 새로운 파일을 생성하는 동시에 쓰기 모드로 연다.
try :
 file = open("info.txt",'w')
 file.write("dasda")
 # 여러가지 처리를 수행 합니다
 # 파일을 닫습니다
 file.close()

except Exception as e :
    print(e)

print("파일이 제대로 닫혔는지 확인하기")
print("file.closed" , file.closed)


try :
    #파일을 쓰기모드로 연다
    file = open("info.txt",'w')
    #여러가지 처리를 수행합니다
    예약.발생해라()
    #파일을 닫습니다
    file.close()
except Exception as e :
    print(e)
finally:
    file.close()

print("파일이 제대로 닫혔는지 확인하기")
print(file.closed)

# 코드를 실행 해보면 closed 속성의 반환값이 false 이므로 파일이 닫히지 않았다는 것을 알 수 있습니다
# 따라서 반드시 finally 구문을 사용하여 파일을 닫게 해야합니다



def test():
    print("test() 함수의 첫 줄입니다")
    try :
        print("try구문이 실행되었습니다")
        return
        print("try 구문의 return 키워드 뒤 입니다ㅓ")
    except :
        print("except구문 실행")
    else :
        print("else 구문 실행")
    finally:
        print("finaly구문입니다")
    print("test()함수의 마지막 줄 입니다.")

test()

# 리턴도 finally는 실행 시킨다!
