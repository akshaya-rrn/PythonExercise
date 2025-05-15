grocery = ['apple', 'orange']

print(len(grocery))

for item in grocery:
    print( " ***************** ", item ," **********************")

grocery.append("banana")
grocery.sort()

del grocery[0]

for item in grocery:
    print( " after deleting item ", item ," **********************")


##################### Set
bri = set(['brazil', 'russia', 'india'])



