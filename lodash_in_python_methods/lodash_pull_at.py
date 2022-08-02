from lodash_instance_provider import _

list_example = ['a', 'b', 'c', 'd']
pulled = _.pull_at(list_example, [1, 3]);

print(list_example)
# ['a', 'c']
print(pulled)
# ['b', 'd']

