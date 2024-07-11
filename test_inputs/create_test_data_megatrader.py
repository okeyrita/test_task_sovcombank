import random
import string

n = 10
m = 4
s = 100000


with open('megatrader_big_input.txt', 'w+') as f:

    f.write(f'{n} {m} {s}\n')
    for day in range(n):
        for day_lot_count in range(m):
            name = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
            count = str(random.randint(950,1100)/10)
            lot_count = str(random.randint(1,5))
            f.write(f'{str(day)} {name} {count} {lot_count}\n')
    f.write('\n')
