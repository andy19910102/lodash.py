from lodash_instance_provider import _

print(_.drop([1, 2, 3], 2))
# [3]
print(_.drop([1, 2, 3], 5))
# []
print(_.drop([1, 2, 3], 0))
# [1, 2, 3]