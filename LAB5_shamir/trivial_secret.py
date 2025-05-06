import random

n=10
t=10

k = 100001
s = random.randint(0,100000)
print("s:",s)

#podział na udziały
nums = []
for i in range(n-1):
    nums.append(random.randint(0,100001))
print(f'nums:', nums)
sn = s
for i in range(n-1):
    sn = (sn - nums[i])
    
sn = sn % k
nums.append(sn)
print(f'udzialy {nums}')


#odtwarzanie sekretu

secret_recovered = 0
for i in range(n):
    secret_recovered += nums[i]
secret_recovered = secret_recovered % k
print(f'sekret odtworzony {secret_recovered}')


