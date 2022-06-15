# object는 QuerySet 내부에 있는 객체에 해당한다. QuerySet은 리스트형태의 데이터베이스에서 전달받은 객체의 모음이다.
# DB(SQL)에서는 row에 해당한다.
# Python으로 작성한 코드가 SQL로 mapping되어 QuerySet이라는 자료 형태로 값이 넘어온다.

#DB에는 column과 row에 데이터가 저장된다. Django에서 column에 해당하는 부분은 모델의 각 클래스안에 지정해준 속성들이며, row에 해당하는 부분은 각 속성에 부여되어 있는 값들이다. 즉 dictionary 가 저장되는 것이다.

# 따라서, QuerySet안에 있는 객체에 접근할 때에는 value에 접근하는지, dictionary의 요소에 접근하는지 등에 따라서 접근 방식이 다르다.

# <클래스이름>.objects.values() :
# .values()로 dictionary의 key와 value에 접근이 가능하다.
# QuerySet()은 리스트이고, 객체는 dictionary 이므로 <variable name>[index]['key'] 의 형식으로 value값에 접근이 가능하다

>>> from account.models import Account
>>> a = Account.objects.values()
>>> a

>>> <QuerySet [{'id':8, 'name':'Kim', 'email':'abc@abc.abc'},{'id':8, 'name':'Kim', 'email':'abc@abc.abc'},{'id':8, 'name':'Kim', 'email':'abc@abc.abc'}]
>>> a[0]['email']
'abc@abc.abc'

# get()은 dictionary의 요소 하나를 반환한다.
# 하나의 객체이기에 반환되기 때문에, dot notation으로 접근이 가능하다. <variable name>.name
# 해당 조건의 요소가 존재하지 않을때는 DoesNotExist, 여러개 존재할때는 MultipleObjectsReturned 에러가 발생한다.
>>> c = Account.objects.get(id=1)
>>> c.name
'Kim'

# filter()는 주어진 parameter에 따라 query의 결과를 필터하며, 결과는 리스트로 반환한다.
>>> b = Account.objects.filter(name__startswith="K")
>>> <QuerySet [<Account: Account object (1)>, <Account: Account object (2)>]>

# <variable name>[index]로 접근이 가능하다.
>>> b[0]
<Account: Account object (1)>

# all()은 QuerySet안의 모든 객체를 리스트 형태로 return한다.
>>> c = Account.objects.all()
<QuerySet [<Account: Account object (8)>, <Account: Account object (9)>, <Account: Account object (10)>]>

>>> c[0]
<Account: Account object (8)>

