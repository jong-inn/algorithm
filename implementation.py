import time

# Problem 1
## move on N x N matrix
## input  : 5
##        : R R R U D D
## output : 3 4

### My Answer

n = int(input())
d_list = input().split()
start_time = time.time()

d_dict = {
      'R': [0, 1]
    , 'L': [-1, 0]
    , 'U': [-1, 0]
    , 'D': [1, 0]
}

result = [1, 1]
for d in d_list:
    dx, dy = d_dict[d]
    if (1 <= (result[0] + dx) <= n) and (1 <= result[1] + dy <= n):
        result[0] += dx
        result[1] += dy
    
end_time = time.time()
print(f"result : {result}, {end_time - start_time:.5f}")

### Solution

n = int(input())
x, y = 1, 1
plans = input().split()
start_time = time.time()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    
    x, y = nx, ny
    
end_time = time.time()
print(f"result : {(x, y)}, {end_time - start_time:.5f}")


# Problem 2
## the number of cases which include 3 in the time span (00:00:00 ~ N:59:59)
## input  : 5
## output : 11475

### My Answer

n = int(input())
start_time = time.time()

total = (n + 1) * 6 * 10 * 6 * 10
if n >= 3:
    result = total - (n * 5 * 9 * 5 * 9)
elif 1 <= n <= 2:
    result = total - ((n + 1) * 5 * 9 * 5 * 9)
else:
    total = 6 * 10 * 6 * 10
    result = total - (5 * 9 * 5 * 9)

end_time = time.time()
print(f"result : {result}, {end_time - start_time:.5f}")

### Solution

h = int(input())
start_time = time.time()

count = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

end_time = time.time()
print(f"result : {count}, {end_time - start_time:.5f}")


# Problem 3
## the number of Knight's direction cases in the 8 x 8 chess
## input  : a1
## output : 2

### My Answer

x, y = input()
start_time = time.time()

x_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
count = 0

dir_list = [
      [1, 2], [1, -2], [-1, 2], [-1, -2]
    , [2, 1], [2, -1], [-2, 1], [-2, -1] 
    ]

for x_num, x_str in enumerate(x_list, 1):
    if x_str == x:
        for dir in dir_list:
            nx = x_num + dir[0]
            ny = int(y) + dir[1]
            
            if (1 <= nx <= 8) and (1 <= ny <= 8):
                count += 1

end_time = time.time()
print(f"result : {count}, {end_time - start_time:.5f}")

### Solution

input_data = input()
start_time = time.time()

row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    
    if next_row >= 1 and next_row <= 8 and next_column >=1 and next_column <= 8:
        result += 1
        
end_time = time.time()
print(f"result : {result}, {end_time - start_time:.5f}")


# Problem 4
## print ordered strings and sum of 1 digit numbers
## input  : K1KA5CB7 / AJKDLSI412K4JSJ9D
## output : ABCKK13  / ADDIJJJKKLSS20

### My Answer

string = input()
start_time = time.time()

num = 0
new_string = []
for idx, s in enumerate(map(ord, string)):
    if s < ord('A'):
        num += int(string[idx])
    else:
        new_string.append(string[idx])

new_string = sorted(new_string)
if num != 0:
    new_string.append(str(num))
    print(new_string)

result = ''.join(new_string)

end_time = time.time()  
print(f"result : {result}, {end_time - start_time:.5f}")

### Solution

data = input()
start_time = time.time()

result = []
value = 0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)
        
result.sort()

if value != 0:
    result.append(str(value))
    
end_time = time.time()  
print(f"result : {''.join(result)}, {end_time - start_time:.5f}")