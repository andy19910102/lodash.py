from lodash_instance_provider import _

print(_.pull_all(['a', 'b', 'c', 'a', 'b', 'c'], ['a', 'c']))
# ['b', 'b']