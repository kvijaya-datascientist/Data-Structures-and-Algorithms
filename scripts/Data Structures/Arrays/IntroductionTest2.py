# Some of basic operations on Array

names = ['sai' , 'gopi' , 'hema' , 'ram']
# Lets consider , we have taken 32-bit system, then 4 elements are there in 'names' array. so, total its 16-bytes (4 * 4).

names.append('siva')  # O(1) - Push
print(names)

names.pop()  # O(1)
print(names)

print(names[3])  # O(1)

names.insert(3 , 'vij')  # O(n/3)
print(names)

names.remove('vij')  # O(n)
print(names)


