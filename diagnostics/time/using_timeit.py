# this uses timeit to time your function, but use timeit over a timing decorator as timeit "also disables garbage collection for the duration of the test".

func_list = [locals()[key] for key in locals().keys()
           if callable(locals()[key]) and key.startswith('time')]

alist=range(1000000)
times=[]
for f in func_list:
    n = 10
    times.append( min(  t for t,_,_ in (f(alist,31) for i in range(n))))

for (time,func_name) in zip(times, func_list):
    print '%s took %0.3fms.' % (func_name, time*1000.)

# taken from: http://stackoverflow.com/questions/1622943/timeit-versus-timing-decorator
