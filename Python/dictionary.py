# Dictionary containing student marks
d = {"Ram": 95, "Shyam": 90, "Hari": 85}

print("Original Dictionary:")
print(d)

# 1. keys()
print("\n1. Keys:")
print(d.keys())

# 2. values()
print("\n2. Values:")
print(d.values())

# 3. items()
print("\n3. Items:")
print(d.items())

# 4. get()
print("\n4. Get value of 'Ram':")
print(d.get("Ram"))

print("Get value of 'Sita' (default):")
print(d.get("Sita", "Not Found"))

# 5. update()
print("\n5. Update Dictionary:")
d.update({"Sita": 88})
print(d)

# 6. setdefault()
print("\n6. Set Default:")
d.setdefault("Gita", 80)
print(d)

# 7. pop()
print("\n7. Pop 'Hari':")
removed = d.pop("Hari")
print("Removed Value:", removed)
print(d)

# 8. popitem()
print("\n8. Popitem:")
last = d.popitem()
print("Removed Pair:", last)
print(d)

# 9. copy()
print("\n9. Copy Dictionary:")
copy_d = d.copy()
print(copy_d)

# 10. fromkeys()
print("\n10. Fromkeys:")
keys = ["A", "B", "C"]
new_d = dict.fromkeys(keys, 0)
print(new_d)

# 11. len()
print("\n11. Length:")
print(len(d))

# 12. in
print("\n12. Check Key using 'in':")
if "Ram" in d:
    print("Ram Found")

# 13. not in
print("\n13. Check Key using 'not in':")
if "Hari" not in d:
    print("Hari Not Found")

# 14. del
print("\n14. Delete 'Shyam':")
del d["Shyam"]
print(d)

# 15. clear()
print("\n15. Clear Dictionary:")
d.clear()
print(d)