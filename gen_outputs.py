import os
import sys
from timeit import default_timer as timer

dirs = [x for x in os.listdir('.') if os.path.isdir(x)]
def run_output(d):
    run_command = f'../../../SKE_LINUX/Edlang/bin/edlang source.ed < {os.path.join(d, "input.in")} > {os.path.join(d, "output.out")}'
    
    start = timer()
    os.system(run_command)
    end = timer()
    return end - start

max_time = 0
for d in dirs:
    print(d)
    max_time = max(max_time, run_output(d))

print(max_time)