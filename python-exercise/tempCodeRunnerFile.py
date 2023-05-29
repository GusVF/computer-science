permissions = {"member", "group"}
permissions.add('affiliate')
permissions.add('user')
permissions.union({user})
print(permissions)
