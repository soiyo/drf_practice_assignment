'''
과제
 1. args, kwargs를 사용하는 예제 코드 짜보기
 2. mutable과 immutable은 어떤 특성이 있고, 어떤 자료형이 어디에 해당하는지 서술하기
 3. DB Field에서 사용되는 Key 종류와 특징 서술하기
 4. django에서 queryset과 object는 어떻게 다른지 서술하기
'''
# immutable 은 상태가 변경되지 않는 객체입니다. 종류로는 int, float, tuple, str, bool이 있습니다.
# 하나의 immutable 값에 여러 개의 참조가 붙습니다. 하나의 주소를 갖습니다.
# mutable 은 상태가 변경되는 객체입니다. 쓰기가 가능한 컨테이너로 이해할 수 있습니다. 종류로는 list, set, dictionary, ndarray(numpy의 배열)가 있습니다.
# 하나의 mutable 값은 하나의 주소를 갖습니다.

print("immutable 객체")
PIE = 3.14
immutable_number = 3.14
number = 3.14

print(hex(id(PIE)))
print(hex(id(PIE)))
print(hex(id(PIE)))

print("mutable 객체")
radius_1 = [3, 5, 7]
radius_2 = [3, 5, 7]
radius_3 = [3, 5, 7]
radius_4 = [3, 5, 7]

print(hex(id(radius_1)))
print(hex(id(radius_2)))
print(hex(id(radius_3)))
print(hex(id(radius_4)))

# 🍺 output
# immutable 객체
# 0x100b1bc70
# 0x100b1bc70
# 0x100b1bc70
# mutable 객체
# 0x100d4da80
# 0x100d4d9c0
# 0x100d526c0
# 0x100d51240