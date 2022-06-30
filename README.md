# Design and Analysis of Algorithms - Assignment Description

## Assignment 1
[Question_1](https://github.com/cskang0121/design-and-analysis-of-algorithms/tree/main/assignment_1/q1)

[Question_2_and_Question_3](https://github.com/cskang0121/design-and-analysis-of-algorithms/tree/main/assignment_1/q2q3)

> Problem statement for question 1: "In a far away world in another multi-verse, your final score in a course depends on the marks in 𝑛 exams. This world is weird, so you can place the scores from each exam side by side (in any order you want) to make your final score. So, you are very much interested in maximizing this number. How can you do this? "

I implemented an algorithm such that it not only works for single-digit numbers, but for arbitrary positive integers. Constraints on the input: 1 ≤ 𝑛 ≤ 10000 and 1 ≤ 𝑎𝑖 ≤ 1000 for all 1 ≤ 𝑖 ≤ 𝑛.

> Problem statement for question 2 : "Normally, we treat multiplication as one operation (meaning taking O(1) time). This is ok because the number of digits of numbers you multiply has a fixed upper bound (normally). However, for high precision computing you may be asked to multiply numbers with a large number of digits. Now, we consider the number of digits as the input size 𝑛 (I am going to use base 2 numbers here). Let’s see how we can multiply efficiently: split your 𝑛 digit input numbers 𝑥, 𝑦 into two halves. For example, a number 10101110 is same as 24 * 1010 + 1110"

I solved this task using "Divide and Conquer" approach. Before jumping into writing the actual code, I wrote out the recurrence relation with the information given and use master's method to find the complexity of this approach.

> Problem statement for question 3 : "Continuing from the previous problem, try to use three multiplications instead of the four for the recursive multiplication of 𝑥𝑦 from the previous problem."

Following the instructions, I wrote a new recurrence relation and use master’s method to get better complexity for multiplication.

## Assignment 2
[Question_1](https://github.com/cskang0121/design-and-analysis-of-algorithms/blob/main/assignment_2/q1.py)

[Question_1_and_Question_2_Explanation](https://github.com/cskang0121/design-and-analysis-of-algorithms/blob/main/assignment_2/KANG%20CHIN%20SHEN_Assignment%202%20CS202%20q1q2.pdf)

> Problem statement for question 1 : "You are given a string 𝑥 of length 𝑛 with the characters given as 𝑥[1], 𝑥[2], ... , 𝑥[𝑛] (note the index starts at 1). The problem is to find the minimum number of characters to add to the string so that it becomes a palindrome. A palindrome is a sequence of characters which reads the same backward as forward, such as madam or racecar. In order to do this you need to use dynamic programming. For example, abca can become a palindrome abcba and acbca is a smallest such palindrome obtained by adding characters to abca. Other examples include abbc -> acbbca OR cabbac (note may not be unique) and abbca -> acbbca."

The tasks are as following : 
  - Write down the recursive formulation for finding 𝐷[𝑖, 𝑗] as well as the base case.
  - Explain in English why the above recursive formulation is correct.
  - Code up your solution in python producing the optimal solution.

I implemented my solution using iterative dynamic programming approach.

> Problem statement for question 2 : "You have started a business selling rolls of paper. The paper rolls come out of your machine as a single roll of length 𝑛. You have an option of cutting the rolls into smaller ones. Rolls of different length sell for different prices; of course, you want to maximize your revenue. You want to solve this problem using dynamic programming. For example, here is table of Length : 1 2 3 4 5 6 7 8 9 10 and Price(𝑝𝑖) : 1 5 7 9 10 17 17 20 23 30"

The tasks are as following :
  - Write a recursive formulation for the optimal solution of the problem for a roll of length 𝑛 with prices for length 𝑖 given as 𝑝𝑖 . Follow the convention that when you cut the roll the first piece is the left side of the roll and then the rest of roll to the right is further cut up as required. Use the notation 𝑅[𝑛] to denote the optimal revenue from roll of length 𝑛
  - Write an iterative pseudo code implementing the above recursive formulation to calculate 𝑅[𝑛].
  - Now, someone imposes an additional constraints that limits the number of rolls of each size that can be produced. For example, as given below :

Length : 1 2 3 4 5 6 7 8 9 10 

Price  : 1 5 7 9 10 17 17 20 23 30 

Limit  : 2 1 2 2 2 1 1 1 1 1
  
- Explain (in less than 30 words) why the same recursive formulation that you wrote in part (a) does not work anymore. Be precise and write the precise reason.

## Assignment 3
[Question_1](https://github.com/cskang0121/design-and-analysis-of-algorithms/tree/main/assignment_3/q1)

> Problem statement for question 1 : "Consider a Boolean formula φ in CNF form. You can write an ILP so that a solution of the ILP can tell us if there exists a satisfying assignment for the given formula φ. In this question, you need to write code to implement such an ILP for solving satisfiability problem for given CNF logic formulas. You must use the cvxpy and sympy library for this question."

## Final Project

The team explored different algorithms to tackle the Max-Flox problem. After doing some research, our team decided to go for Push-Relabel algorithms for this project and went ahead to implement the actual code.
