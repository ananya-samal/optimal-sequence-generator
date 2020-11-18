# optimal-sequence-generator
## Problem statement
## Let Cm be a sequence defined by:

  1- 
  ```
  Cm(n+1)  :={ Cm(n)/2
               Cm(n)∗3 + 1
  ```                
  2- Cm(n)/2 for Cm(n) is even
  
  3- cm(n)∗3 + 1 for Cm(n) is uneven/odd
  
  4- Cm(1) :=m and m,n ∈ N
  
 ## Understanding
  
  It is a Mathematical Sequence, We are provided with a number m. Task is to generate a sequence of numbers starting from m and find the number of steps taken by m to reduce to     1,4,2.
  Imagine m = 10 
  and N = index
  
  C10(1) = 10 // as 10 is even Cm(n)/2 --> 10/2
  
  C10(2) = 5  // as 5 is odd Cm(n)∗3 + 1 ---> 5x3+1
  
  C10(3) = 16
  
  C10(4) = 8
  
  C10(5) = 4
  
  C10(6) = 2
  
  C10(7) = 1
  
  C10(8) = 4
  
  C10(9) = 2
  
  for the above example number of steps required to reach 1 is 7
# How to run the file
```
Run for : master
to run the file download to your local system
install the packages mentioned in requirment.txt
to run python file in cmd use command ---> python <file name.py>
```
# Explanation each solution
## Q - A - Implement a program to calculate the number of steps to reach 1 thefirst time for any given m∈N.
  1- Idea of approching this solution was to find a simplest method to generate the mathematical sequence 1,4,2 for any given number given as a input by the user. And print the sequence and no of steps taken to reach 1.
  2- And also allowing user to input only natural number n > 0.

## Q - B - Adapt  the  implementation  to  calculate  the  number  of  steps  for  each m ∈ [1,10000].
  1- Instaed of user giving any number as input, we are genrating the sequence for a range of number starting from 1 to 10000. And no of steps taken to reach 1 for each number.

## Q - C - Try  to  improve  the  implementation  to  calculate  the  steps  as  fast  aspossbile.
  1- For this Idea was to modify the approach taken in Q-B and improving the performance by making use of different methods of iteration in python. And finding an optimal solution which will take least time to achieve 1. I have taken 4 different approaches, each with explaination has been described inside the file.

## Q - D - Print the number of steps for eachm∈[1,10000] as diagram.
  1- Implemented a graph using matplotlib package from python.
 
![Figure_1](https://user-images.githubusercontent.com/34180878/99405183-c35d5a00-28ec-11eb-87aa-2505e300e0a8.png)
