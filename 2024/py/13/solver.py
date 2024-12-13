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

def solve_for_x(A, Y):
    try:
        A_inv = np.linalg.inv(A)
        x = np.dot(A_inv, Y)
        if np.all((x >= 0) & (x <= 100)) and np.all(isinteger(x)):
            return x
        else:
            return f'Invalid range of x= ${x}'
    except np.linalg.LinAlgError:
        return "Matrix A is singular and cannot be inverted."



prize = np.array([3, 1])
cost = 0
As, Ys = read_input_file('input.txt')
for A, Y in zip(As, Ys):
    x = solve_for_x(A, Y)
    if type(x) != str:
        cost = cost + np.dot(prize, x)

print(f'Total cost: ${cost}')

