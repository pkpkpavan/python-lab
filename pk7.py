print("using lists")
values = [3,1,5,9]
print(F'"enter the list number in {values}"')
print(1)
print("enter the values in sorted form")
values.sort()
print(values)
print("add the value to a values")
values.insert(2,4)
print(values)
print("remove 3 from the values")
values.remove(3)
print(values)
values.append(7)
print("add 7 at last in values")
print(values)
values.pop()
print(values)
print(len(values))

print("using tuples")
tuple1 = (1,3,"pavan")
tuple2 = (2,4,"kalyan")
print(f'tuple1 = {tuple1}')
print(f'tuple2 = {tuple2}')
print("add tuple1 tuple2")
tuple3 = tuple1 + tuple2
print(tuple3)
print(tuple1.count(3))
print(tuple1.index("pavan"))

print("using dictionaries")
dict = {'fruit': 'apple','color': 'red','cost': 50}
print(dict)
print("accesing valuesin dict")
print("fruit:",dict['fruit'])
print("updating dict ")
dict['fruit'] = 'banana'
print(dict)
print("removing all elements in dict")
dict.clear()
print(dict)

print("using sets")
set1={"pavan","kalyan","harsha"}
print("set1=",set1)
print("add a name to set1")
set1.add("abid")
print(set1)
print("update set1 with different names")
set1.update(["pk","hy","ah"])
print(set1)
print("length of set1")
print(len(set1))
print("remove a name in set1")
set1.remove("pavan")
print(set1)