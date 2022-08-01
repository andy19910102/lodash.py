from lodash_instance_provider import _

print(_.drop_right([1, 2, 3]))
# [1, 2]
print(_.drop_right([1, 2, 3], 2))
# [1]
print(_.drop_right([1, 2, 3], 5))
# []
print(_.drop_right([1, 2, 3], 0))
# [1, 2, 3]