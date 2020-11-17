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
  
 ## a)  Implement a program to calculate the number of steps to reach 1 the first time for any given m∈N.
  for the above example number of steps required to reach 1 is 7
```
Run for : master
to run the file download to local system
to run python file in cmd use command python <file name.py>
```



## Q - D - GRAPH
![Figure_1](https://user-images.githubusercontent.com/34180878/99405183-c35d5a00-28ec-11eb-87aa-2505e300e0a8.png)
