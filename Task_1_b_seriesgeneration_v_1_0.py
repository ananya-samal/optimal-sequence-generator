'''
@AUTHOR: Ananya Samal

@NAME: Task_1_b_seriesgeneration_v_1_0.py 
Task a :- 
a) Implement a program to calculate the number of steps to reach 1 thefirst time for any given m€N.

Description:
  1- Generate a math sequence which ends with 1,4,2 for each number in the range 1 to 10000.
  2- Find the number of steps required to reach 1.
  
'''
def optimal_sequence(n):
    sequence = []        # an empty list where each element of the series will be appended
    sequence.append(n)   # Cm(1)= m first element is always the no for which the series has to be generated (m)
    evaluate = True
    while(evaluate == True):                        # Run the loop till the end sequence 1,4,2 is not encountered
        if sequence[-1] % 2 == 0:                   # To check number is even or not
            new_elem_sequence = (sequence[-1])//2   # When number is even as per the rule Cm(n)/2
        else:
            new_elem_sequence = (sequence[-1] * 3) + 1 # When number is odd as per the rule Cm(n)x 3 + 1
        sequence.append(new_elem_sequence)             # appending new element to tge list
        if(len(sequence)>2):                           # Not checking when the list is less than size 3
            if(sequence[-1] == 2 and sequence[-2] == 4 and sequence[-3] == 1):  # Validating the sequence 1,4,2     
                evaluate = False
    return sequence

for n in range(1,10000,1):               # Added a loop so that each element from 1-10000 can be provided as a input to the function
    sequence = list(optimal_sequence(n)) # calling the function for sequence generation
    print(sequence)
    print(len(sequence) - 3)             # It will print from reverse the third position which is 1
