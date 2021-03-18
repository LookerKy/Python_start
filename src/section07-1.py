# section07
# 클래스
# 구조화, 결합을 느슨하게 만들기 유지보수 및 생산성을 늘리기 위해서

# 선언
class UserInfo:
    # 속성, 메소드로 이루어져 잇음
    def __init__(self, name):
        self.name = name

    def user_info_p(self):
        print("Name", self.name)


# 클래스, 인스턴스 차이중요
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 사용 가능, 객체보다 먼저 생성(static), 객체간 변수 공유
# 인스턴스 변수 : 객체마다 별도로 존재, 인스턴스 생성 후 사용
# 클래스의 인스턴스화
user1 = UserInfo("Lee")
user1.user_info_p()
user2 = UserInfo("Park")
user2.user_info_p()

print(id(user1))
print(id(user2))

# 네임스페이스 확인
print(user1.__dict__)
print(user2.__dict__)


# 예제2 self의 이해
class SelfTest:

    # 클래스메소드
    @classmethod
    def function1(cls):
        print('function1 called')

    # 인스턴스 메소드
    def function2(self):
        print(">>>", id(self))
        print("function2 called")


# 인스턴스 변수에 할당 self_test는 인스턴스로써 생성이되고 self가 자동으로 파라미터로 넘어가게됨
self_test = SelfTest()
SelfTest.function1()
self_test.function2()

print(id(self_test))
SelfTest.function2(self_test)


# 예제 3
# 클래스 변수, 인스턴스 변수

class WareHouse:
    # 클래스 변수
    stock_num = 0

    def __init__(self, name):
        self.name = name
        WareHouse.stock_num += 1

    def __del__(self):
        WareHouse.stock_num -= 1


user1 = WareHouse("Kim")
user2 = WareHouse("Park")
user3 = WareHouse("Lee")

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)
print(WareHouse.__dict__)

print(user1.name)
print(user2.name)
print(user3.name)

print(user1.stock_num)
print(user2.stock_num)
print(user3.stock_num)

del user1

print(user2.stock_num)
print(user3.stock_num)


