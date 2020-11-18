'''
Memory profiling of how operations is used.
This was not in requirement but adding it for understanding my thought process. 

1- List comprehension takes less amount of memory but as you would have seen in task-C file it takes more time for processing.

2- List conversion of map takes little more memory than list comprehension but it is less time consuming also plottable, so a solution as per my understdning for coveing all the secanarios.

3- map is definietly the most memory consuming compared to other two as it doing the operation in one go but that is where we are saving the time. So this approach is best for cases where data need to be calculated and stored. But for retreiving this will be same as the second method. 


For this setup i have used memory_profiler
to run this file follow the command
  
                                mprof run <python file name>

if you wish to plot it then post the previous command

                                mprof plot 
'''
import numpy as np
from memory_profiler import profile

def optimal_sequence_desc_with_div(n):
    evaluate = True
    step_cnt = 0
    new_elem_sequence = n
    while(evaluate == True):
        new_elem_sequence = (new_elem_sequence * 3) + 1 if new_elem_sequence % 2 != 0 else new_elem_sequence // 2
        step_cnt = step_cnt + 1
        if(new_elem_sequence == 1):
            evaluate = False
    return step_cnt

@profile(precision=5)
def list_comp_run(n):
    store_map = [optimal_sequence_desc_with_div(x) for x in range(1,n)]

@profile(precision=5)
def list_map_run(n):
    store_map = list(map(optimal_sequence_desc_with_div,list(range(1,n))))

@profile(precision=5)
def map_run(n):
    store_map = map(optimal_sequence_desc_with_div,list(range(1,n)))

num = 20000
list_comp_run(num)
list_map_run(num)
map_run(num)
