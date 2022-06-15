'''
과제
 1. args, kwargs를 사용하는 예제 코드 짜보기
 2. mutable과 immutable은 어떤 특성이 있고, 어떤 자료형이 어디에 해당하는지 서술하기
 3. DB Field에서 사용되는 Key 종류와 특징 서술하기
 4. django에서 queryset과 object는 어떻게 다른지 서술하기
'''
# *args 는 함수에서 n개의 인자를 받아 튜플 형태로 전달한다.
def comments(*args):
    print('comments : ', args)

comments('Hi, Tommy!','Tommy, there is you?')

# **kwargs 는 함수에서 n개를 key-value형태로 받아 딕셔너리 형태로 전달한다.
def users(**kwargs):
    print(kwargs)

users(name='Tommy', age='16', gender='man')

# 🍺 output
# comments :  ('Hi, Tommy!', 'Tommy, there is you?')
# {'name': 'Tommy', 'age': '16', 'gender': 'man'}