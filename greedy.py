import time

# Example 1
## give change to a customer
## input  : 1260
## output : 6

start_time = time.time()

n = 1260
count = 0

# coins
array = [500, 100, 50, 10]

for coin in array:
    count += n // coin
    n %= coin

end_time = time.time()
print(f'result : {count}, {end_time - start_time:.5f}')

# Problem 1
## until the number becomes 1
## input  : 25 3
## output : 6

### My Answer
n, k = map(int, input().split())

start_time = time.time()
count = 0

while True:
    if n % k == 0:
        n //= k
        count += 1
    else:
        n -= 1
        count += 1
    
    if n == 1:
        break

end_time = time.time()
print(f'result : {count}, {end_time - start_time:.5f}')

### Solution
n, k = map(int, input().split())

start_time = time.time()
result = 0

while True:
    
    target = (n // k) * k
    result += (n-target)
    n = target
    
    if n < k:
        break
    
    result += 1
    n //= k
    
result += (n - 1)

end_time = time.time()
print(f'result : {result}, {end_time - start_time:.5f}')

# Problem 2
## add or multiple
## input  : 02984
## output : 576

### My Answer

array = list(map(int, input()))
start_time = time.time()

result = array[0]
for n in array[1:]:
    if (result in [0, 1]) or (n in [0, 1]):
        result += n
    else:
        result *= n
        
end_time = time.time()
print(f'result : {result}, {end_time - start_time:.5f}')

### Solution

data = input()
start_time = time.time()

result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num
    
end_time = time.time()
print(f'result : {result}, {end_time - start_time:.5f}')

# Problem 3
## maximize the group
## input  : 5
##          2 3 1 2 2
## output : 2

### My Answer

n = int(input())
data = list(map(int, input().split()))
start_time = time.time()

data.sort()

result = 0
tmp = []
for d in data:
    tmp.append(d)
    
    if max(tmp) == len(tmp):
        result += 1
        tmp = []
        
end_time = time.time()
print(f'result : {result}, {end_time - start_time:.5f}')

### Solution

n = int(input())
data = list(map(int, input().split()))
start_time = time.time()

data.sort()

result = 0
count = 0

for i in data:
    count += 1
    if count >= i:
        result += 1
        count = 0
    
end_time = time.time()
print(f'result : {result}, {end_time - start_time:.5f}')