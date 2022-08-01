# Lodash.py

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

Implement Lodash methods with Python.

## Usage

```python
from lodash import Lodash

# Create instance of Lodash
_ = Lodash()

print(_.find_index(users, lambda o: o["user"] == "barney"))
# 0
```

### List Methods

#### _.compact

Creates an list with all falsey values removed. The values False, None, 0 and "" are falsey.

```python
print(_.compact([0, 1, False, 2, '', 3, None]))
# [1, 2, 3]
```

#### _.drop

Creates a slice of list with n elements dropped from the beginning.

```python
print(_.drop([1, 2, 3], 2))
# [3]
print(_.drop([1, 2, 3], 5))
# []
print(_.drop([1, 2, 3], 0))
# [1, 2, 3]
```

#### _.drop_right

Creates a slice of list with n elements dropped from the end.

```python
print(_.drop_right([1, 2, 3]))
# [1, 2]
print(_.drop_right([1, 2, 3], 2))
# [1]
print(_.drop_right([1, 2, 3], 5))
# []
print(_.drop_right([1, 2, 3], 0))
# [1, 2, 3]
```

#### _.find_index

Returns the index of the found element, else -1.

```python
users = [
  { 'user': 'Benson',  'active': False },
  { 'user': 'Frank',    'active': False },
  { 'user': 'Erik', 'active': True }
]

print(_.find_index(users, lambda o: o["user"] == "Benson"))
# 0
print(_.find_index(users, { 'user': 'Frank', 'active': False }))
# 1
print(_.find_index(users, ['active', False]))
# 0
print(_.find_index(users, 'active'))
# 2
```

#### _.from_pairs

This method returns an object composed from key-value pairs.

```python
print(_.from_pairs([['a', 1], ['b', 2]]))
# {'a': 1, 'b': 2}
```

#### _.head

Returns the first element of list.

```python
print(_.head([1, 2, 3]))
# 1
print(_.head([])) 
# None
```

#### _.initial

Gets all but the last element of list.

```python
print(_.initial([1,2,3]))
# [1, 2]
```

#### _.join

Returns the joined string.

```python
print(_.join(["a", "b", "c"], "~"))
# 'a~b~c'
print(_.join(["a", "b", "c", "d"], "@"))
# 'a@b@c@d'
```

#### _.last

Returns the last element of list.

```python
print(_.last([1, 2, 3]))
# 3
```

#### _.take

Creates a slice of list with n elements taken from the beginning.

```python
print(_.take([1, 2, 3]))
# [1]
print(_.take([1, 2, 3], 2))
# [1, 2]
print(_.take([1, 2, 3], 5))
# [1, 2, 3]
print(_.take([1, 2, 3], 0))
# [0]
```