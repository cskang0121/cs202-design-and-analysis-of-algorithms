##############################################################
# this is a tester file, you are not required to submit this
# file in the final solution, please ensure your submitted q1 file
# can run without any issues with this tester file to avoid any penalty
##############################################################

from time import time

# Import the parse_expr from sympy.parsing.sympy_parser
from sympy.parsing.sympy_parser import parse_expr

# Import ilp from q1
from q1 import ilp

# Test cases
test_cases = [
    "(x4 | ~x3) & (x1 | x2 | x4) & (x3 | ~x1 | ~x2) & (x0 | x2 | x3 | ~x1 | ~x4) & (x1 | x3 | x4 | ~x0 | ~x2)",
    "x0 & ~x0",
    "(x3 | ~x1) & (x0 | x3 | x4 | ~x1 | ~x2)",
    "x0 & ~x0 & (x1 | x2) & (x0 | ~x2) & (x1 | ~x0) & (x1 | ~x2) & (x2 | ~x0) & (~x0 | ~x1)",
    "x2 & ~x0",
]

# Convert each string expression into 
test_cases = [parse_expr(s) for s in test_cases]

# Expected result
expected_result = [True, False, True, False, True]

num_test_cases = len(test_cases)

test_cases_mismatched_index = []

for i in range(num_test_cases):
    try:
        start_time = time()
        result = ilp(test_cases[i])
        time_taken = time() - start_time
        print("Test Case " + str(i+1))
        print("Execution Time : " + str(round(time_taken,2)) + " seconds")
        print("Expected Result: " + str(expected_result[i]))
        print("         Result: " + str(result))
        if (result == expected_result[i]):
            print ("Passed")
        else:
            print ("Failed")
            test_cases_mismatched_index.append(str(i+1))
         
        print('--------------------------------------------------------------------------')

    except Exception as e:
            print('Result  : Failed - Exception ' + str(e))
            test_cases_mismatched_index.append(str(i+1))

print ("Number of test cases : " + str(num_test_cases))
print ("Number of test cases with matched outcome : " + \
    str(num_test_cases-len(test_cases_mismatched_index)))
print ("Index of failed cases (if any): {}".format(", ".join(test_cases_mismatched_index))) 
print('--------------------------------------------------------------------------')

