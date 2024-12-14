import numpy as np

def isinteger(x):
    return np.abs(x - np.round(x)) < 0.001 

def read_input_file(file_path):
    As = []
    Ys = []
    A = []
    Y = []

    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith("Button A:") or line.startswith("Button B:"):
                parts = line.split(":")[1].strip().split(", ")
                x = int(parts[0].replace("X+", ""))
                y = int(parts[1].replace("Y+", ""))
                A.append([x, y])
            elif line.startswith("Prize:"):
                parts = line.split(":")[1].strip().split(", ")
                x = int(parts[0].replace("X=", ""))
                y = int(parts[1].replace("Y=", ""))
                Y = [x, y]
                
                A = np.array(A).transpose()
                Y = np.array(Y).reshape(-1, 1)
                As.append(A)
                Ys.append(Y)    
                A = []
                Y = []
    
    return As, Ys

def solve_for_x(A, Y, limit=100, k=None):
    try:
        A_inv = np.linalg.inv(A)
        x = np.dot(A_inv, Y)
        x = x if k is None else np.dot(A_inv, k) + x
        if np.all((x >= 0) & (x <= limit)) and np.all(isinteger(x)):
            return x, A_inv
        else:
            return f'Invalid range of x= ${x}', None
    except np.linalg.LinAlgError:
        return "Matrix A is singular and cannot be inverted.", None


# Solution
#
#   Ax = b
#   A_inv * Ax = A_inv * b
#   x = A_inv * b
#
#   With constraints for x being a positive integer and x <= 100. This should probably been solved with [Hermite Normal Form](https://en.wikipedia.org/wiki/Hermite_normal_form)



# Part 1
prize = np.array([3, 1])
cost = 0
As, Ys = read_input_file('input.txt')
for A, Y in zip(As, Ys):
    x, A_inv = solve_for_x(A, Y)
    if type(x) != str:
        cost = cost + np.dot(prize, x)

print(f'Total cost Part One: ${cost[0]}')

# Part 2
# The second part is basicsally the same, only with a translation of the coordinates by a vector k = [10000000000000, 10000000000000]
#
#   Ax = k + b
#   A_inv * Ax = A_inv * k  * A_inv * b
#   x = A_inv * k  * A_inv * b
#
#   With constraints for x being a positive integer and x <= 100. This should probably been solved with [Hermite Normal Form](https://en.wikipedia.org/wiki/Hermite_normal_form)

translation = 10000000000000
cost_part_2 = 0
As, Ys = read_input_file('input.txt')
k = translation * np.ones([2, 1])
failed = 0
for A, Y in zip(As, Ys):
    x, A_inv = solve_for_x(A, Y, limit=translation*2, k=k)
    if type(x) != str:
        cost_part_2 = cost_part_2 + np.dot(prize, x)
    else:
        failed += 1
print(f'Failed: {100 * failed/len(As)} %') # Just out of curiosity
print(f'Total cost Part 2: $ {int(cost_part_2)}')
