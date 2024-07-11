import os
import time 

start = time.time()
os.system('python3 solution/share_building.py < test_inputs/share_building_big_input.txt') 
end = time.time()
print(f'work time {end - start}')