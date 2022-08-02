from lodash_instance_provider import _

print(_.join(["a", "b", "c"], "~"))
# 'a~b~c'
print(_.join(["a", "b", "c", "d"], "@"))
# 'a@b@c@d'