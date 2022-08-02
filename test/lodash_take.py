from lodash_instance_provider import _

print(_.take([1, 2, 3]))
# [1]
print(_.take([1, 2, 3], 2))
# [1, 2]
print(_.take([1, 2, 3], 5))
# [1, 2, 3]
print(_.take([1, 2, 3], 0))
# [0]