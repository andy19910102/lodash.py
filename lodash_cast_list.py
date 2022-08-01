from lodash_instance_provider import _

print(_.cast_list(1))
# [1]
print(_.cast_list({ 'a': 1 }))
# [{'a': 1}]
print(_.cast_list('abc'))
# ['abc']
print(_.cast_list())
# []