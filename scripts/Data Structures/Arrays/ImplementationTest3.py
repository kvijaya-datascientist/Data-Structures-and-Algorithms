"""  Although arrays are pre-defined in Python in the form of lists, we can implement our own arrays.
Here, we will implement our own array with some common methods such as access, push, pop, insert, delete    """
class MyArray:

    def __init__(self):
        self.length = 0  #We initialize the array's length to be zero
        self.data = {}   #We initialize the data of the array using an empty dictionary. The keys will correspond to the index and the values to the data

    """  The attributes of the array class are stored in a dictionary by default.
     When the __dict__ method is called on an instance of the class it returns the attributes of the class along with their values in a dictionary format
     Now, when the instance of the class is printed, it returns a class object with its location in memory.
     But we know when we print the array we get the elements of the array as output
     When we print the instance of the class, the built-in __str__ method is called. So we can modify the __str__ method inside the class
     To suit our needs.  """
    def __str__(self):
        return str(self.__dict__)  #This will print the attributes of the array class(length and dsata) in string format when print(array_instance) is executed

    def push(self,item):
        self.length += 1
        self.data[self.length-1] = item  #Adds the item provided to the end of the array

    def get(self,index):
        return self.data[index] #This method takes in the index of the element as a parameter and returns the corresponding element in O(1) time.

    def pop(self):
        del self.data[self.length - 1]
        self.length -= 1

    def insert(self,index,item):
        self.length += 1
        for i in range(self.length-1 , index , -1):
            self.data[i] = self.data[i-1]  #Shifts every element from the index to the end by one plsce towards right. Thus making space at the specified index
        self.data[index] = item   #Adds the element at the given index. O(n) operation

    def delete(self,index):
        for i in range(index , self.length-1):
            self.data[i] = self.data[i+1]
        del self.data[self.length-1]
        self.length -= 1

if __name__ == "__main__":
    array1 = MyArray()
    print(array1.__str__())  # print(array1.__dict__)
    array1.push('vijaya')
    array1.push('sai')
    array1.push('hemaja')
    print(array1.__str__())
    print(array1.get(0))
    array1.pop()
    print(array1.__str__())
    array1.insert(0,'sita')
    print(array1.__str__())
    array1.delete(2)
    print(array1.__str__())