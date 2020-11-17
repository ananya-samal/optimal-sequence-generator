'''
@AUTHOR: Ananya Samal

@NAME: Task-1-C-optimize-seriesgeneration.py 
Task c :- 
c)  Try  to  improve  the  implementation  to  calculate  the  steps  as  fast  aspossbile.

Description:
  1- Find the number of steps required to reach 1 from the sequence 1,4,2 in the range 1 to 10000.
  2- Find the fastest time required to reach 1.
  
Remark:
 Adding more than one approach to understand the time efficiency on each approach
'''
import timeit                             #using timeit module for time benchmarking

#First solution using division 
def optimal_sequence_desc_with_div(n):    
    evaluate = True
    step_cnt = 0                          #initialising the setup count to 0 
    new_elem_sequence = n                 #after each while loop unless 1 is encountered it will keep appending generated numbers from the sequence
    while(evaluate == True):
        new_elem_sequence = (new_elem_sequence * 3) + 1 if new_elem_sequence % 2 != 0 else new_elem_sequence // 2  #nested if-else
        step_cnt = step_cnt + 1           #icrement of step count with 1
        if(new_elem_sequence == 1):       #condition to check when 1 will encounter and will break the loop
            evaluate = False
    return step_cnt
	
#Q(c)
##Optimisation 1 - store only the step count 
optimal_steps_array = []                       #declared a empty list where step_cnt will be stored 
start_total_time = timeit.default_timer();     #the start time at execution
for n in range(1,10000,1):                     #for loop to iterate in number 1 to 10000
    step_cnt = optimal_sequence_desc_with_div(n) #passing the optimal_sequence_desc_with_div func to the for loop over 10000 times
    optimal_steps_array.append(step_cnt)         #appending step_cnt to optimal_steps_array list
end_total_time = timeit.default_timer();        #end time after execution
total_execution_time = (end_total_time - start_total_time) #time needed for entire calculation
print("optimal_sequence_desc_with_div::The execution time to reach 1 in all sequences is "+str(total_execution_time)) 
#print(optimal_steps_array)  #commented out for readbility uncomment to see the list of step count required for each no

##second approach little time improvement is acheieved when loop is moved inside the function
def optimal_sequence_desc_with_div_looped():
    
    def optimal_sequence_desc_with_div_int(n): #to implemet map iteration defined this function
        evaluate = True
        step_cnt = 0
        new_elem_sequence = n
        while(evaluate == True):
            new_elem_sequence = (new_elem_sequence * 3) + 1 if new_elem_sequence % 2 != 0 else new_elem_sequence // 2
            step_cnt = step_cnt + 1
            if(new_elem_sequence == 1):
                evaluate = False
        return step_cnt                
    
    optimal_steps_array1 = []
    optimal_steps_array1 = list(map(optimal_sequence_desc_with_div_int, list(range(1,10000,1)) )) #converting the list to map for easy retrieval
    print(type(optimal_steps_array1)) #type is list
    #print(optimal_steps_array1)    #commented out for readbility uncomment to see the list of step count required for each no
    return optimal_steps_array1     #return type is a list

#Q(c)
##Optimization 2 - Move for loop inside function
start_total_time = timeit.default_timer();
optimal_steps_array_looped = optimal_sequence_desc_with_div_looped()
print(type(optimal_steps_array_looped))
end_total_time = timeit.default_timer();
total_execution_time = (end_total_time - start_total_time)
print("optimal_sequence_desc_with_div_looped::The execution time to reach 1 in all sequences is "+str(total_execution_time))
