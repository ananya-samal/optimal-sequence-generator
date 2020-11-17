'''
@AUTHOR: Ananya Samal

@NAME: Task-1-d-diagram.py 
Task d :- 
d)  Print the number of steps for each m € [1,10000] as diagram.

Description:
  1- Find the number of steps required to reach 1 from the sequence 1,4,2 in the range 1 to 10000.
  2- Find the fastest time required to reach 1.
  3- plotting to graph
Remark:
 converting map to list to use it to form the graph 
'''
import timeit
import matplotlib.pyplot as plt #using matplotlib module to plat the graph

#Below stated code is taken from Task-1-C-optimize-seriesgeneration.py file enhancement 2 method. using matplotlib.pyplot as a extra method here to print the output in graph.

def optimal_sequence_desc_with_div_looped():
    
    def optimal_sequence_desc_with_div_int(n):
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
    optimal_steps_array1 = list(map(optimal_sequence_desc_with_div_int, list(range(1,10000,1)) ))
    print(type(optimal_steps_array1))
    #print(optimal_steps_array1)
    return optimal_steps_array1

##Optimization 2 - Move for loop inside function
start_total_time = timeit.default_timer();
optimal_steps_array_looped = optimal_sequence_desc_with_div_looped()
end_total_time = timeit.default_timer();
total_execution_time = (end_total_time - start_total_time)
print("optimal_sequence_desc_with_div_looped::The execution time to reach 1 in all sequences is "+str(total_execution_time))

#Q(d)
plt.figure(figsize =(10, 5),dpi = 250) #adding height width and dpi resolution to have better visibility
plt.plot(list(range(1,10000,1)),optimal_steps_array_looped,color = 'black', linewidth = '0.08') 
plt.title('Optimal Sequence')
plt.ylabel('Plotting No of steps to Input Number')          #y-axis naming
plt.xlabel('Input Number')                                  #x-axis naming
plt.show()
