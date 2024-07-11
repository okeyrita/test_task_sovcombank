from random import randint

len_shares = 2000000

with open('share_building_big_input.txt', 'w+') as f:
    f.write(str(len_shares) + '\n')
    for x in range(0, len_shares):
        f.write(str(randint(1,100)) + '\n')
