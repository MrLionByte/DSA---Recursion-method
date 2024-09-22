# 1. Find Fibonacci number of 10 using Recursion
# 2. Find sum of this array arr = [2,4,6,3,1,44,32] using Recursion
# 3. Find a number is prime using Recursion
# 4. Binary search using Recursion 
# 5. Binary search using Recursion reverse
# 

# 5 :
def reverse_binary_serch(arr, start, end):
    if start >= end:
        return arr
    arr[start],arr[end] = arr[end], arr[start]
    return reverse_binary_serch(arr, start+1 , end-1)
        
p = [1,2,3,4,5,6]
print(reverse_binary_serch(p, 0, len(p)-1))

# 1:
def fibonacci_finder(val):
    if val == 2 or val == 1:
        return 1
    elif val == 0:
        return 0
    elif val < 0:
        return 'Can not find'
    else:
        return fibonacci_finder(val-1)+fibonacci_finder(val-2)
    
print(fibonacci_finder(10))

#2:
def sum_arr(arr):
    if not arr:
        return 0
    return arr[0]+sum_arr(arr[1:])


arr = [2,4,6,3,1,44,32]
print(sum_arr(arr))

#3 :
def prime_finder(prime, divisor=None):
    if divisor is None:
        divisor = int(prime**0.5)
    if prime <= 1:
        return False
    if divisor == 1:
        return True
    if prime%divisor == 0:
        return False
    else:
        return prime_finder(prime, divisor-1)

prime = 9
print(prime_finder(prime))

#4 :
def recursion_binary(arr, target, lower, upper):
    if lower > upper:
        return 'Not Found'
    mid = (lower+upper)//2

    if arr[mid] == target:
        return f'{arr[mid]} ON index {mid} '
    elif arr[mid] < target:
        return recursion_binary(arr, target, mid+1, upper)
    else:
        return recursion_binary(arr, target, lower, mid - 1)

def binary_search(arr, target):
    arr = sorted(arr)
    print(arr,'Sorted')
    return recursion_binary(arr, target, 0, len(arr)-1)

arr = [1,4,3,6,7,8,4,2]
target = 2
print(binary_search(arr, target))

 
