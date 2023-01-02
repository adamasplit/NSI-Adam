while i<num:
    s = n +m
    n=m
    m=s
    i+=1

def suite_fibo_rec(n):
    if n<2:
        return 1
    return suite_fibo_rec(n+1)+suite_fibo_rec(n+2)

def suite_fibo_dyn(val,n):
    if n in val.keys:
        return val[n]
