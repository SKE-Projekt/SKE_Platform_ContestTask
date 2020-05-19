import os

for filename in os.listdir('real_tests'):
    with open('real_tests/' + filename, 'r+', encoding='utf-8') as f:
        in_d = f.read()
    idr, ext = os.path.splitext(filename)
    
    os.makedirs('test' + idr, exist_ok=True)
    if ext == '.in':
        with open('test' + idr + '/input.in', 'w+', encoding='utf-8') as f:
            f.write(in_d)
    else:
        with open('test' + idr + '/output.out', 'w+', encoding='utf-8') as f:
            f.write(in_d)