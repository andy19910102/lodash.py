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

#### _.pull

Removes all given values from list.

```python
print(_.pull(['a', 'b', 'c', 'a', 'b', 'c'], 'a', 'c'))
# ['b', 'b']
```

#### _.pull_all

This method is like _.pull except that it accepts a list of values to remove.

```python
print(_.pull_all(['a', 'b', 'c', 'a', 'b', 'c'], ['a', 'c']))
# ['b', 'b']
```

#### _.pull_at

Removes elements from list corresponding to indexes and returns a list of removed elements.

```python
list_example = ['a', 'b', 'c', 'd']
pulled = _.pull_at(list_example, [1, 3]);

print(list_example)
# ['a', 'c']
print(pulled)
# ['b', 'd']
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

#### _.tail

Gets all but the first element of list.

```python
print(_.tail([1, 2, 3, 4]))
# [2, 3, 4]
```

#### _.uniq

Creates a duplicate-free version of an list.

```python
print(_.uniq([2, 1, 2]))
# [1, 2]
print(_.uniq([3, 3, 4, 4, 5, 6, 6, 7]))
# [3, 4, 5, 6, 7]
```

#### _.xor

Creates an list of unique values that is the symmetric difference of the given list. 
The order of result values is determined by the order they occur in the list.

```python
print(_.xor([2, 1], [2, 3]))
# [1, 3]
```

### Lang Methods

#### _.cast_list

Casts value as an list

```python
print(_.cast_list(1))
# [1]
print(_.cast_list({ 'a': 1 }))
# [{'a': 1}]
print(_.cast_list('abc'))
# ['abc']
print(_.cast_list())
# []
```

#### _.comforms_to

Checks if dict_input conforms to source by invoking the predicate properties of source with the corresponding property values of dict_input.

```python
dict_example = { 'a': 1, 'b': 2 };

print(_.conforms_to(dict_example, { "b":lambda n : n > 1}))
# True
print(_.conforms_to(dict_example, { "b":lambda n : n > 2}))
# False
```

#### _.gt

Returns true if value is greater than other, else false.

```python
print(_.gt(3, 1))
# True
print(_.gt(3, 3))
# False
print(_.gt(1, 3))
# False
```

#### _.gte

Returns true if value is greater than or equal to other, else false.

```python
print(_.gte(3, 1))
# True
print(_.gte(3, 3))
# True
print(_.gte(1, 3))
# False
```

#### _.is_list

Checks if value is classified as a List.

```python
print(_.is_list([1, 2, 3]))
# True
print(_.is_list("abc"))
# False
print(_.is_list(None))
# False
print(_.is_list(12))
# False
print(_.is_list({"a": 12}))
# False
```

### Math Methods

#### _.add

Adds two numbers.

```python
print(_.add(6, 4))
# 10
```

#### _.divide

Divide two numbers.

```python
print(_.divide(6, 4))
# 1.5
```

#### _.max

Computes the maximum value of list.

```python
print(_.max([4, 2, 8, 6]))
# 8
```

#### _.min

Computes the minimum value of list.

```python
print(_.min([4, 2, 8, 6]))
# 2
```