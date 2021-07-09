# O(n) or Linear Time Complexity
import time
small_array = ['sai']
medium_array = ['sai' for i in range(1000)]
large_array = ['sai' for i in range(100000)]


def findName(names):
    t0=time.time()
    for i in range(0,len(names)):    # O(n)
        if names[i] == 'sai':    # O(n)
            print('Required name found')  #  O(n)
    t1 = time.time()
    print('the search taken', {t1-t0} , 'seconds') 


findName(small_array)
findName(medium_array)
findName(large_array)

def funChallenge(input):
    t0 = time.time()
    temp = 10     #  O(1)
    temp = temp + 50     #  O(1)
    for i in range(0,len(input)):   # O(n)
        var = True  # n * O(1)
        a = +1    # n * O(1)
    t1 = time.time()
    print('the serach taken ',{t1-t0},'seconds')
    return a  # O(1)

funChallenge(small_array)
funChallenge(medium_array)
funChallenge(large_array)

"""
Complexity Analysis:
#Total running time of the funchallenge function =
#O(1 + 1 + n + n*1 + n*1 + n*1 + 1) = O(3n +3) = O(3(n+1))
#Any constant in the Big-O representation can be replaced by 1, as it doesn't really matter what constant it is.
#Therefore, O(3(n+1)) becomes O(n+1)
#Similarly, any constant number added or subtracted to n or multiplied or divided by n can also be safely written as just n
#This is because the constant that operates upon n, doesn't depend on n, i.e., the input size
#Therefore, the funchallenge function can be said to be of O(n) or Linear Time Complexity.

"""