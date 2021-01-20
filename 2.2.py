fibs = [0,1,1]
while(fibs[-1]+fibs[-2]<4000000):
    fibs.append(fibs[-1]+fibs[-2])

sum=0
for i in range(0,len(fibs),3):
    sum+=fibs[i] 

print(sum)