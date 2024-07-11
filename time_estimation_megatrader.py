import os
import time 

start = time.time()
os.system('python3 solution/megatrader.py < test_inputs/megatrader_big_input.txt') 
end = time.time()
print(f'work time {end - start}')