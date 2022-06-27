##############################################################
# Name : Kang Chin Shen
# Section : G3
##############################################################

# Main idea : Divide and Conquer

# Compare the sequence of the two inputs that gives larger outcome
def compare(x, y):
    xy = int(str(x) + str(y))
    yx = int(str(y) + str(x))

    if(xy > yx) :
        return True
    return False


# Sort the array using compare(x, y)
def sort(arr):
    if len(arr) > 1:
  
        # Finding the mid of the array
        mid = len(arr)//2
  
        # Dividing array into two halves
        left = arr[:mid]
        right = arr[mid:]
  
        # Recursively call the first half
        sort(left)
  
        # Recursively call the second half
        sort(right)
  
        # Define three pointers
        i = 0
        j = 0
        k = 0
  
        # Merge
        while i < len(left) and j < len(right):
            if compare(right[j], left[i]):
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
  
        # Checking if any element was left 
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
  
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


# Form the final result
def get_res(arr):
    res = "";
    for i in range(len(arr),0,-1):
        res += str(arr[i-1])
    return int(res)


def largest_number(arr):
    sort(arr)
    return get_res(arr)

