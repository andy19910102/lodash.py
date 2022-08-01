from lodash_instance_provider import _

print(_.compact([0, 1, False, 2, '', 3, None]))
print(_.drop([1, 2, 3], 2))
print(_.drop([1, 2, 3], 5))
print(_.drop([1, 2, 3], 0))