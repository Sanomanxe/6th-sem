# Original Set
s = {10, 20, 30, 40, 50}

print("Original Set:")
print(s)

# 1. add()
print("\n1. Add:")
s.add(60)
print(s)

# 2. update()
print("\n2. Update:")
s.update([70, 80])
print(s)

# 3. remove()
print("\n3. Remove:")
s.remove(40)
print(s)

# 4. discard()
print("\n4. Discard:")
s.discard(100)      # No error if element is not present
print(s)

# 5. pop()
print("\n5. Pop:")
x = s.pop()         # Removes a random element
print("Removed:", x)
print(s)

# 6. copy()
print("\n6. Copy:")
new_set = s.copy()
print(new_set)

# 7. union()
print("\n7. Union:")
s2 = {50, 60, 90}
print(s.union(s2))

# 8. intersection()
print("\n8. Intersection:")
print(s.intersection(s2))

# 9. difference()
print("\n9. Difference:")
print(s.difference(s2))

# 10. symmetric_difference()
print("\n10. Symmetric Difference:")
print(s.symmetric_difference(s2))

# 11. issubset()
print("\n11. Is Subset:")
a = {10, 20}
print(a.issubset(s))

# 12. issuperset()
print("\n12. Is Superset:")
print(s.issuperset(a))

# 13. len()
print("\n13. Length:")
print(len(s))

# 14. in
print("\n14. Check using 'in':")
if 20 in s:
    print("20 Found")

# 15. not in
print("\n15. Check using 'not in':")
if 100 not in s:
    print("100 Not Found")

# 16. clear()
print("\n16. Clear Set:")
s.clear()
print(s)