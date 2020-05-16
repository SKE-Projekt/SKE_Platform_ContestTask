import sys
import os
import random


def make_input(d):
    try:
        raw_p = os.path.join(d, 'input_raw.in')
        _p = os.path.join(d, 'input.in')

        with open(raw_p, 'r+', encoding='utf-8') as f:
            raw = f.readlines()
        
        _ = []
        for r in raw:
            bad_ones = random.randint(5, max(10000 - (len(raw)) - len(_), 5))
            for b in range(bad_ones):
                if random.randint(1, 3) == 2:
                    y = -random.randint(10, 1000000)
                else:
                    y = random.randint(10, 1000000)
                if random.randint(1, 3) == 2:
                    x = -random.randint(10, 1000000)
                else:
                    x = random.randint(10, 1000000)
                _.append(f"{y} {x}")
            _.append(r)
        
        _ = '\n'.join(_)
        with open(_p, 'w+', encoding='utf-8') as f:
            f.write(_)
    except:
        print("BRAK PLIKU RAW")

ds = [x for x in os.listdir('.') if os.path.isdir(x)]

for d in ds:
    print(d)
    make_input(d)