def frange_positve(start, stop =None, step=None):
    if stop == None:
        stop = start + 0.0
        start = 0.0
    if step == None:
        step = 1.0
    print("start = ", start, "stop = ", stop, "step = ", step)
    
    count = 0
    while True:
        temp = float(start + count * step)
        if temp >= stop:
            break
        yield temp
        count += 1
    

for i in frange_positve(1.5, 10.5, 0.5):
    print("%g" % i, end=". ")