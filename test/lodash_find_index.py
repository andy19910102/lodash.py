from lodash_instance_provider import _

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