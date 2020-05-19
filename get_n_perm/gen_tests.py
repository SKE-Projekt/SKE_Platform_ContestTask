import os
import sys
import random


test_p = f'test{sys.argv[1]}'
test_s = int(sys.argv[2])

os.makedirs(test_p, exist_ok=True)

silnia = [1]
for i in range(1, 13):
    silnia.append(silnia[i - 1] * i);

with open(os.path.join(test_p, 'input.in'), 'w+', encoding='utf-8') as f:
    # t = random.randint(1 + int((float(test_s) / 10 * 50)), test_s * 250)
    t = random.randint(1, 4)
    f.write(str(t))
    f.write('\n')
    for i in range(t):
        leng = random.randint(1, 12)
        pos = random.randint(0, silnia[leng])
        f.write(f'{leng} {pos}\n')
print("DONE")
