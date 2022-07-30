import json
a = {'id': 12345, 
'token':56789}
s = json.dumps(a)

with open('test.json', 'wt') as f:
    f.write(s)
with open('test.json', 'rt') as f:
    ys = json.load(f)
print(ys, type(ys))