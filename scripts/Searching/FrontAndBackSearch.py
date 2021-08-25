"""
To search any element in an unordered array:
1. Linear Search(checking element by element from beginning to the end) Time Complexity - O(n)
2. But Front and Back algorithm(search for element from Front and Back parallely) takes half of linear search time (i.e) -  O(n/2)
"""
def frontAndBack(arr , key):
    firstIndex , lastIndex = (0 , len(arr)-1)
    while firstIndex <= lastIndex :
        if(key == arr[firstIndex] or key == arr[lastIndex]):
            return True
        firstIndex += 1
        lastIndex -= 1
    return False

if __name__ == "__main__":
    arr = [2,1,4,5,22,67,89,25,75,34,88]
    key = 91
result = frontAndBack(arr , key)
if(result != -1):
    print({key} , 'found in' , str(arr))
else:
    print({key} , 'not found in ' , str(arr))

# Linear Search : O(n)
"""arr1 = [2,3,5,7,11,1,13,56,6]
key = 56
for i in arr1:
    if(arr1[i] == key):
      print({key} , 'found in ',str(arr1) , 'at index',i ) """


