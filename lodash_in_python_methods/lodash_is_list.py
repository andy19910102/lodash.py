from lodash_instance_provider import _

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