from lodash_instance_provider import _

users = [
  { 'user': 'barney',  'active': False },
  { 'user': 'fred',    'active': False },
  { 'user': 'pebbles', 'active': True }
]

print(_.find_index(users, lambda o: o["user"] == "barney"))
print(_.find_index(users, { 'user': 'fred', 'active': False }))
print(_.find_index(users, ['active', False]))
print(_.find_index(users, 'active'))