'''
@AUTHOR: Ananya Samal

@NAME: Task_1_a_seriesgeneration_userinput_v_1_0.py 
Task a :- 
a) Implement a program to calculate the number of steps to reach 1 thefirst time for any given m€N.

Description:
  1- Generate a math sequence which ends with 1,4,2 for any given number taken as a input from user.
  2- Find the number of steps required to reach 1.  
'''

def optimal_sequence(user_input):
    sequence = [] # an empty list where each element of the series will be appended
    
    sequence.append(user_input) # Cm(1)= m first element is always the no for which the series has to be generated (m)
    
    evaluate = True
    
    while(evaluate == True): # run the loop till the end sequence 1,4,2 is not encountered 
        if sequence[-1] % 2 == 0: # to check number is even or not
            new_elem_sequence = (sequence[-1])//2 #when number is even as per the rule Cm(n)/2
        else:
            new_elem_sequence = (sequence[-1] * 3) + 1 #when number is odd as per the rule Cm(n)x 3 + 1
        sequence.append(new_elem_sequence)
        if(len(sequence)>2): #Not checking when the list is less than size 3
            if(sequence[-1] == 2 and sequence[-2] == 4 and sequence[-3] == 1):       
                evaluate = False
    return sequence

input_new = input('Enter a number to generate series :') #Taking input from user
user_input = int(input_new)
sequence = list(optimal_sequence(user_input))# calling the function for sequence generation
print('Expected Sequence is :', sequence)
print('The Number of steps required to Reach 1 is : ', len(sequence) - 3)
       
