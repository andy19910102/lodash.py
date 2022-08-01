from lodash_instance_provider import _

dict_example = { 'a': 1, 'b': 2 };

print(_.conforms_to(dict_example, { "b":lambda n : n > 1}))
# True
print(_.conforms_to(dict_example, { "b":lambda n : n > 2}))
# False