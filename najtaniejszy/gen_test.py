import os
import sys
import random


test_p = f'test{sys.argv[1]}'
test_s = int(sys.argv[2])

os.makedirs(test_p, exist_ok=True)
with open(os.path.join(test_p, 'input.in'), 'w+', encoding='utf-8') as f:
    n = random.randint(3, 300)
    m = random.randint(n + 2, min(500, n*4))

    f.write(f"{n} {m}\n")
    for i in range(n - 1):
        a = i + 1
        b = i + 2
        c = random.randint(1, test_s * 20)

        f.write(f"{a} {b} {c}\n")
    
    for i in range(m - n + 1):
        a = random.randint(1, n)
        b = random.randint(1, n)
        c = random.randint(1, test_s * 40)

        f.write(f"{a} {b} {c}\n")