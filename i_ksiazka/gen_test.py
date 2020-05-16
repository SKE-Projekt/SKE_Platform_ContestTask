import os
import sys
import random
import string


ordid = int(sys.argv[2])
s = int(sys.argv[1])
def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

n = random.randint(max(0, s - (s // 10)), s + (s // 10))
strings = []
for i in range(n):
    if random.randint(0, 10) > 6:
        if random.randint(1, 20) > 17:
            strings.append(randomString(random.randint(0, 10)) + "$NAME$" + randomString(random.randint(0, 15)))
        else:
            strings.append("$NAME$")
    else:
        strings.append(randomString(random.randint(10, 50)))
strings.append("$NAME$")
strings.append("$END$")

strings = ' '.join(strings)
os.makedirs(f'test{ordid}', exist_ok=True)

with open(f'test{ordid}/input.in', 'w+', encoding='utf-8') as f:
    f.write(strings)
print("DONE")