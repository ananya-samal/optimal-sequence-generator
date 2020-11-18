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

#First solution using floor division and list comprehension
def optimal_sequence_desc_with_div_list_comp(n):    
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
'''
for n in range(1,10001,1):                     #for loop to iterate in number 1 to 10000
    step_cnt = optimal_sequence_desc_with_div(n) #passing the optimal_sequence_desc_with_div func to the for loop over 10000 times
    optimal_steps_array.append(step_cnt)         #appending step_cnt to optimal_steps_array list
'''
optimal_steps_array = [optimal_sequence_desc_with_div_list_comp(x) for x in range(1,10001)]   #list comprehension
end_total_time = timeit.default_timer();        #end time after execution
total_execution_time = (end_total_time - start_total_time) #time needed for entire calculation
print("optimal_sequence_desc_with_div_list_comp::The execution time to reach 1 in all sequences is "+str(total_execution_time)) 
#print(optimal_steps_array)  #commented out for readbility uncomment to see the list of step count required for each no

'''
In second approach little time improvement is acheieved when loop is moved inside the function
'''
def optimal_sequence_internal_looped_map_list():
    
    def optimal_sequence_desc_with_div_int(n): #to implemet map iteration,defined this function
        evaluate = True
        step_cnt = 0                        #initialising the setup count to 0
        new_elem_sequence = n               #after each while loop unless 1 is encountered it will keep appending generated numbers from the sequence
        while(evaluate == True):
            new_elem_sequence = (new_elem_sequence * 3) + 1 if new_elem_sequence % 2 != 0 else new_elem_sequence // 2  #nested if-else
            step_cnt = step_cnt + 1         #icrement of step count with 1
            if(new_elem_sequence == 1):     #condition to check when 1 will encounter and will break the loop
                evaluate = False
        return step_cnt                
    
    optimal_steps_array1 = list(map(optimal_sequence_desc_with_div_int, list(range(1,10001,1)) )) #converting the list to map for easy retrieval
    print(type(optimal_steps_array1)) #type is list
    #print(optimal_steps_array1)    #commented out for readbility uncomment to see the list of step count required for each no
    return optimal_steps_array1     #return type is a list

#Q(c)
##Optimization 2 - Move for loop inside function
start_total_time = timeit.default_timer();  #the start time at execution
optimal_steps_array_looped = optimal_sequence_internal_looped_map_list() # optimal_steps_array_looped storing the function output
#print(type(optimal_steps_array_looped))
end_total_time = timeit.default_timer();  #end time after execution
total_execution_time = (end_total_time - start_total_time)    #time needed for entire calculation
print("optimal_sequence_internal_looped_map_list::The execution time to reach 1 in all sequences is "+str(total_execution_time))

'''
3rd approach. my thought here was using a map i could save sometime in the previous approach.
but converting list was consuming. So i turned towrds generator, which saves time significantly compared to last stage.
but I can not use the output of yield directly for ploting graph or anytging for current case graph as it gives 
generator object and i need to covert it to list which results in same time.
So I will stick to the list(map) which is my 2nd approach to generate graph.
'''

def optimal_sequence_gen_obj_internal_looped_map_list(): 
    
    def optimal_sequence_desc_with_div_yield_int(n): #to implemet map iteration,defined this function
        evaluate = True                              #initialising the setup count to 0
        step_cnt = 0
        new_elem_sequence = n                        #after each while loop unless 1 is encountered it will keep appending generated numbers from the sequence
        while(evaluate == True):
            new_elem_sequence = (new_elem_sequence * 3) + 1 if new_elem_sequence % 2 != 0 else new_elem_sequence // 2  #nested if-else
            step_cnt = step_cnt + 1                  #icrement of step count with 1
            if(new_elem_sequence == 1):              #condition to check when 1 will encounter and will break the loop
                evaluate = False
        yield step_cnt          #yield makes it a generator
        #print(step_cnt)

    #defining map for iteration and converting map to list for easy retrieval
    optimal_steps_array = list(map(optimal_sequence_desc_with_div_yield_int, list(range(1,10001,1)) )) 
    print(type(optimal_steps_array)) #type is list
    return optimal_steps_array

##Optimization 3 - Using Yeild
optimal_steps_array3 = []                           #declared a empty list where step_cnt will be stored
start_total_time = timeit.default_timer();          #the start time at execution
optimal_steps_array3 = optimal_sequence_gen_obj_internal_looped_map_list() #optimal_steps_array3 storing function output
#print(type(optimal_steps_array3)) #type is list
end_total_time = timeit.default_timer();                      #end time after execution
total_execution_time = (end_total_time - start_total_time)    #time needed for entire calculation
print("optimal_sequence_gen_obj_internal_looped_map_list::The execution time to reach 1 in all sequences is "+str(total_execution_time))

'''
4th approach
For my undestanding and trying several approches I believe map is the fastest method to perform calculation and store data,
but as it returns map object so retrieving data in list or tuple is time consuming.
so only if time is considered for performace based on calculation and 
storing data then this approach gives significant time reduction comapred to all the other approches i have taken in this file.
For plotting I am just coverting the map object to list as matplotlib takes list as argument.
''' 
def optimal_sequence_only_map_object():
    
    def optimal_sequence_map_int(n):  #to implemet map iteration,defined this function
        evaluate = True               #initialising the setup count to 0
        step_cnt = 0
        new_elem_sequence = n         #after each while loop unless 1 is encountered it will keep appending generated numbers from the sequence
        while(evaluate == True):
            new_elem_sequence = (new_elem_sequence * 3) + 1 if new_elem_sequence % 2 != 0 else new_elem_sequence // 2   #nested if-else
            step_cnt = step_cnt + 1        #icrement of step count with 1
            if(new_elem_sequence == 1):    #condition to check when 1 will encounter and will break the loop
                evaluate = False
        return step_cnt
        #print(step_cnt)        
    
    optimal_steps_array = map(optimal_sequence_map_int, list(range(1,10001,1)) ) 
    #defining map for iteration - as lambda is to simple for this implementation we have to use a function for calculating the steps 
    print(type(optimal_steps_array)) #type is map object
    #print(optimal_steps_array)
    #print(list(optimal_steps_array))
    return optimal_steps_array

##Optimization 4 - Using System provided Map Iteration
start_total_time = timeit.default_timer();           #the start time at execution
optimal_steps_array_np = optimal_sequence_only_map_object() #optimal_steps_array_np storing function output
end_total_time = timeit.default_timer();              #end time after execution
total_execution_time = (end_total_time - start_total_time) #time needed for entire calculation
print("optimal_sequence_only_map_object::The execution time to reach 1 in all sequences is "+str(total_execution_time)) 
#print(list(optimal_steps_array))   #can always convert to list post performing operation to use the data
#Alternatively we could use next function to interate trough a map object 

#for map_iter in range(10000):#
#    print(next(optimal_steps_array_np))
    
