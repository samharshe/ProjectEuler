ev_fibs = [0,2,8]
while(ev_fibs[-1]+ev_fibs[-2]<4000000):
    ev_fibs.append(4*ev_fibs[-1]+ev_fibs[-2])

print(sum(ev_fibs))