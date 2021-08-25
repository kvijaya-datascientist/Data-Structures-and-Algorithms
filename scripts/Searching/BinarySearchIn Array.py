""" use binary search only in below conditions:
1. if array is sorted
2. if array is increasing and decreasing
3. sorted array is rotated and then given as i/p
4. Array is given as zigzaw format
Implementation :
Step 1 - Read the search element from the user.
Step 2 - Find the middle element in the sorted list.
Step 3 - Compare the search element with the middle element in the sorted list.
Step 4 - If both are matched, then display "Given element is found!!!" and terminate the function.
Step 5 - If both are not matched, then check whether the search element is smaller or larger than the middle element.
Step 6 - If the search element is smaller than middle element, repeat steps 2, 3, 4 and 5 for the left sublist of the middle element.
Step 7 - If the search element is larger than middle element, repeat steps 2, 3, 4 and 5 for the right sublist of the middle element.
Step 8 - Repeat the same process until we find the search element in the list or until sublist contains only one element.
Step 9 - If that element also doesn't match with the search element, then display "Element is not found in the list!!!" and terminate the function."""

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

