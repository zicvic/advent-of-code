import numpy as np

def read_input_file(file_path):
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
    
    A = np.array(A)
    Y = np.array(Y).reshape(-1, 1)
    
    return A, Y

def solve_for_x(A, Y):
    try:
        A_inv = np.linalg.inv(A)
        x = np.dot(A_inv, Y)
        return x
    except np.linalg.LinAlgError:
        return "Matrix A is singular and cannot be inverted."

# Example usage
A, Y = read_input_file('input_1.txt')
print("A =", A)
print("Y =", Y)
x = solve_for_x(A, Y)
print("x =", x)

