##############################################################
# Name : Kang Chin Shen
# Section : G3
##############################################################

def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False


def shortest_palindrome(s):

    # Return s if the s is already a palindrome 
    if(is_palindrome(s)):
        return s

    # Otherwise form shortest palindrome 
    n = len(s)

    # Creation of matrix of size n*n to store minimum number of insertions
    matrix = [[0 for i in range(n)] for i in range(n)]

	# Fill the matrix
    for gap in range(1, n):
        l = 0
        for h in range(gap, n):
            if s[l] == s[h]:
                matrix[l][h] = matrix[l + 1][h - 1]
            else:
                matrix[l][h] = (min(matrix[l][h - 1],matrix[l + 1][h]) + 1)
            l += 1

    # Trace the matrix to form the shortest palindrome
    i = 0
    j = n-1 
    trace = ""

    # Loop through the matrix from top right corner
    # Stop when the cell is holding zero value
    while(matrix[i][j] > 0):

        # If s[i] and s[j] are same, move in diagonal direction
        if(s[i] == s[j]):
            trace += s[i]
            i+=1
            j-=1

        # If they are different
        else:
            
            if(matrix[i+1][j] <= matrix[i][j-1]): 
                #append the character to trace and increment i 
                trace += s[i]
                i+=1 

            else:
                #append the character to trace and decrement j 
                trace += s[j]
                j-=1
    
    # Extract the remaining portion
    middle = s[i:j+1]

    # Form the final result
    res = trace + middle + trace[::-1]
 
    return res
