nums = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}

def f(l):
    out = ""
    for i in range(len(l)):
        if l[i].isnumeric():
            out += l[i]
            continue
        for k,v in nums.items():
            if l[i::-1][:len(k)] == k[::-1]:
                out += str(v) 
    return out
    
print(sum([int((v := [c for c in l if c.isnumeric()])[0] + v[-1]) for l in d]))
print(sum([int((v := [c for c in f(l) if c.isnumeric()])[0] + v[-1]) for l in d]
