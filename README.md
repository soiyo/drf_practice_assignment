[폴더구조보기](#folder)

**1주차 과제_week_1**
 1. args, kwargs를 사용하는 예제 코드 짜보기

```python
def comments(*args):
    print('comments : ', args)

comments('Hi, Tommy!','Tommy, there is you?')

def users(**kwargs):
    print(kwargs)

users(name='Tommy', age='16', gender='man')
```
- *args 는 함수에서 n개의 인자를 받아 튜플 형태로 전달한다. **kwargs 는 함수에서 n개를 key-value형태로 받아 딕셔너리 형태로 전달한다. 
---
 **2. mutable과 immutable은 어떤 특성이 있고, 어떤 자료형이 어디에 해당하는지 서술하기**
 
 - immutable : 상태가 변경되지 않는 객체 
     - 종류 : int, float, tuple, str, bool

 - mutable : 상태가 변경되는 객체 (쓰기가 가능한 컨테이너)
    - 종류 : list, set, dictionary, ndarray(numpy의 배열)가 있다. 
---
 **3. DB Field에서 사용되는 Key 종류와 특징 서술하기**
- CK, PK, UK, AK, FK, SK 등이 있다. 
    - PK (Primary Key) : 기본키 (중복불가, 유일성, 최소성, NULL(X))
    - CK (Check) : 특정 Column에 값을 입력할 수 있는 범위나 조건을 지정 (제약 조건)
    - UK (Unique Key) : (중복허용, 유일성, UNIQUE INDEX 만들어 처리, 테이블 내 UK는 여러번 지정가능)
    - AK (Alternate Key) : 후보키 중 기본키로 선정되지 않은 키
    - FK (Foreign Key) : 외래키 (릴레이션 간 관계 표현시 사용, 릴레이션의 기본키를 참조하는 속성)
    - SK (Super Key) : 고유하게 식별하는 모든 조합
---
**4. django에서 queryset과 object는 어떻게 다른지 서술하기**
 - object는 QuerySet 내부에 있는 객체에 해당한다. QuerySet은 리스트형태의 데이터베이스에서 전달받은 객체의 모음이다.
---
# folder
#### **폴더 구조**
```bash
├── README.md
├── week_1_2
│   ├── args_kwargs.py
│   ├── db_field_key.py
│   ├── django_queryset_object.py
│   └── mutable_immutable.py
└── week_3
    ├── blog
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── __init__.cpython-38.pyc
    │   │   ├── admin.cpython-38.pyc
    │   │   ├── apps.cpython-38.pyc
    │   │   └── models.cpython-38.pyc
    │   ├── admin.py
    │   ├── apps.py
    │   ├── migrations
    │   │   ├── 0001_initial.py
    │   │   ├── __init__.py
    │   │   └── __pycache__
    │   │       ├── 0001_initial.cpython-38.pyc
    │   │       └── __init__.cpython-38.pyc
    │   ├── models.py
    │   ├── tests.py
    │   └── views.py
    ├── db.sqlite3
    ├── manage.py
    ├── user
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── __init__.cpython-38.pyc
    │   │   ├── admin.cpython-38.pyc
    │   │   ├── apps.cpython-38.pyc
    │   │   └── models.cpython-38.pyc
    │   ├── admin.py
    │   ├── apps.py
    │   ├── migrations
    │   │   ├── 0001_initial.py
    │   │   ├── __init__.py
    │   │   └── __pycache__
    │   │       ├── 0001_initial.cpython-38.pyc
    │   │       ├── 0002_userprofile_is_active_userprofile_is_admin.cpython-38.pyc
    │   │       ├── 0003_rename_userprofile_user.cpython-38.pyc
    │   │       └── __init__.cpython-38.pyc
    │   ├── models.py
    │   ├── tests.py
    │   └── views.py
    └── week_3
        ├── __init__.py
        ├── __pycache__
        │   ├── __init__.cpython-38.pyc
        │   ├── settings.cpython-38.pyc
        │   ├── urls.cpython-38.pyc
        │   └── wsgi.cpython-38.pyc
        ├── asgi.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py
```
---