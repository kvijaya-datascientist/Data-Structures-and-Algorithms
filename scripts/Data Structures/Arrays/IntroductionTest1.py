"""
Arrays are one of the most commonly used Data Structure.
The elements of an Array are stored in contiguous memory location.
Arrays are of two types : Static and Dynamic.
Static arrays have fixed, pre-defined amount of memory that they can use, whereas in Dynamic array this is flexible.
In Python, we only have dynamic arrays.
Some basic operations and their complexities are given below:
Look up/Access  ---> O(1)
append/pop  ---> O(1)
Insert ---> O(n)
Delete ---> O(n)

"""
array = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
array1 = [1, 2, 7,  3, 4, 5, 6, 7, 8,7]

"""  Look-up/Access:
Any element of an array can be accessed by its index.
We just need to ask for the particular index of the element we are interested in and we will get the element in constant time. """
print('first_element :',array[0])   #This will return the first element of the array, in this case, a, in O(1) time
print('sixth_element :',array[5])   #sixth-element = g Again, in O(1) time

"""  append/pop:
append corresponds to pushing or adding an element at the end of the array.
Similarly, pop corresponds to removing the element at the end of the array.
Since the index of the end of the array is known, finding it and appending or popping an element will only require O(1) time """
array.append('h')   #Adds 'h' at the end of the array in O(1) time
print(array)

""" In some special cases, the append operation may take greater time. This is because as mentioned earlier, Python has dynamic arrays
So when an element is to appended and the array is filled, the entire array has to be copied to a new location
With more space allocated(generally double the space) this time so that more items can be appended.
Therefore, some individual operations may reuire O(n) time or greater, but when averaged over a large number of operations,
The complexity can be safely considered to be O(1)  """

array.pop()   #removed last element 'h' from the array
print(array)

"""  Insert:
Insert operation inserts an element at the beginning of the array, or at any location specified.
This is O(n) operation since after inserting the element at the desired location,
the elements to the right of the array have to be updated with the correct index as they all have shifted by one place.
This requires looping through the array. Hence, O(n) time. """
array.insert(0,'vijaya') #Inserts 'vijaya' at the beginning of the array and shifts all other elements one place towards right. O(n)
print(array)
array.insert(4,'sai') #inserts 'sai' at index '4', thus shifting all elements starting from index 4 one place towards right. O(n)
print(array)

"""  Delete:
Similar to insert, it deletes an element from the specified location in O(n) time
The elements to the right of the deleted element have to shifted one space left, which requires looping over the entire array
Hence, O(n) time complexity  """
array.remove('a')  #remove the given element 'a' from the array
print(array)
array1.pop(0)  #This pops the first element of the array, shifting the remaining elements of the array one place left. O(n)
print(array1)
array1.remove(7) #This command removes the first occurence of the element 7 in the array, for which it needs to traverse the entire array, which requires O(n) time
print(array1)
del array[2:4] #This command deletes elements from position 2 to position 4, again, in O(n) time
print(array)

