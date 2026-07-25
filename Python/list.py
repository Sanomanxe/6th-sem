l=["apple","ball","cat","dog"]
l.append("elephant")

l.insert(1,"bat")

# l.extend([4,5])

l.remove("bat") #remove(x)

l.pop() #pop(i)

# l.clear()

print(l.index("ball")) #index(x)

print(l.count("cat")) #count(x)

l.sort() #sort()
print(l)

l.reverse() #reverse()
print(l)

a=l.copy() #new=list.copy()
print(a)