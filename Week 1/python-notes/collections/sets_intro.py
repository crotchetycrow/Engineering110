utensils = {"fork", "knife", "spoon", "spatula"}

print(utensils, type(utensils))

utensils.add("garlic press")

print(utensils)

utensils.discard("knife")

print(utensils)

# Unordered, unique collection

rep_list = [1,2,3,3,3,4,5,6,7,8,88,8,9]

unique = set(rep_list)

print(unique)

# Frozen sets

x = frozenset([1,2,4,6])

# Immutable version of a set
