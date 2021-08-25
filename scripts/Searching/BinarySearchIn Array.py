""" use binary search only in below conditions:
1. if array is sorted
2. if array is increasing and decreasing
3. sorted array is rotated and then given as i/p
4. Array is given as zigzaw format   """

# Binary Search - Recursion/Recursion approach  : O(logn)
def binarySearch1(arr , key , low , high):
   if(low > high):
       return -1
   mid = (low + high) // 2
   if(key == arr[mid]):
       return mid
   elif(key < arr[mid]):
       return binarySearch1(arr , key , low , mid-1)
   else:
       return binarySearch1(arr , key , mid+1 , high)

if __name__ == "__main__":
    arr = [1,2,4,6,9,13,17]
    key = 11
    firstIndex, lastIndex = (0, len(arr) - 1)
result = binarySearch1(arr , key , firstIndex , lastIndex)

if(result != -1):
    print({key} , 'found in ',str(arr) ,'at index : ', str(result))
else:
    print({key} ,'not found in ' , str(arr) )

