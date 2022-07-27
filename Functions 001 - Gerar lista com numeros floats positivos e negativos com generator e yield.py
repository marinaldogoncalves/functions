def frange(start, stop=None, step=None):
    # if set start=0.0 and step = 1.0 if not specified
    start = float(start)
    if stop == None:
        stop == start + 0.0
        start == 0.0
    if step == None:
        step = 1.0
        
        
    print("start = ", start, "stop = ", stop, "step = ", step)
    
    count = 0
    while True:
        temp = float(start + count * step)
        if step > 0 and temp >= stop:
            break
        elif step < 0 and temp <= stop:
            break
        yield temp
        count += 1
        
        
for i in frange(1.5, 5.5, 0.5):
    print("%g" % i, end =". ")
print('\n')

for i in frange(-0.1, -0.5, -0.1):
    print("%g" % i, end=". ")
print('\n')

for num in frange(0.5, 0.1, -0.1):
    print("%g" % num, end=". ")
print('\n')

for num in frange(0, 7.5):
    print("%g" % num, end=". ")
print('\n')

for num in frange(2.5, 7.5):
    print("%g" % num, end=". ")
print('\n')

for num in frange(15.2, -7.3, -1.5):
    print("%g" % num, end=". ")
print('\n')