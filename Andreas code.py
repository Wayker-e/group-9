import numpy as np


def create_Ybus(array):
    # Lager matrisen og definerer noen variabler som brukes i for-løkkene
    n = len(array[0]) + 1
    m = n
    c = 1
    matrix = [[0 for _ in range(n)] for _ in range(n)]

    # Lager de ikke-diagonale elementene i matrisen
    for i in range(m - 1):
        for j in range(m - 1):
            if array[i][j] != 0:
                matrix[i][j + c] = -1 / array[i][j]
                matrix[j + c][i] = -1 / array[i][j]
            else:
                continue
        m -= 1
        c += 1

    # Lager de diagonale elemente i matrisen
    for i in range(n):
        for k in range(n):
            if k != i:
                matrix[i][i] -= matrix[i][k]
            else:
                continue

    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(row)


line_data_fig2 = [[0.025 + 0.1j, 0.05 + 0.2j, ],
                  [0.025 + 0.1j]]
a = np.pi
bus_data_fig2 = [[a, a, 1.05, 0],
                 [1, a, 1.04, a],
                 [2, 1.5, a, a]]
minmax_generators_fig2 = [[a, a],
                          [a, 1],
                          [a, a]]
loads_fig2 = [a, a, a, a]


# print(create_Ybus(line_data_fig2))
# print(180-np.angle(create_Ybus(line_data_fig2)[0][1], deg=True))

def newton_raphson(lines, buses, minmax_gen, loads):
    # Find the state values
    x = np.transpose(np.zeros(len(buses)))

    # Iterate through the first two elements in each row/bus in the b
    # Find the specified valued

    # Find the calculated values
    print(x)
    return



Y = create_Ybus(line_data_fig2)

v1 = 1.05
v2 = 1.04
v3 = 0.9059
d1 = 0
d2 = -0.023589
d3 = -0.119510


P2 = (v2*v1*abs(Y[1][0])*np.cos(np.angle(Y[1][0])-d2+d1)
    + v2*v2*abs(Y[1][1])*np.cos(np.angle(Y[1][1])-d2+d2)
    + v2*v3*abs(Y[1][2])*np.cos(np.angle(Y[1][2])-d2+d3))

P3 = (v3*v1*abs(Y[2][0])*np.cos(np.angle(Y[2][0])-d3+d1)
    + v3*v2*abs(Y[2][1])*np.cos(np.angle(Y[2][1])-d3+d2)
    + v3*v3*abs(Y[2][2])*np.cos(np.angle(Y[2][2])-d3+d3))

Q2 =-(v2*v1*abs(Y[1][0])*np.sin(np.angle(Y[1][0])-d2+d1)
    + v2*v2*abs(Y[1][1])*np.sin(np.angle(Y[1][1])-d2+d2)
    + v2*v3*abs(Y[1][2])*np.sin(np.angle(Y[1][2])-d2+d3))

Q3 =-(v3*v1*abs(Y[2][0])*np.sin(np.angle(Y[2][0])-d3+d1)
    + v3*v2*abs(Y[2][1])*np.sin(np.angle(Y[2][1])-d3+d2)
    + v3*v3*abs(Y[2][2])*np.sin(np.angle(Y[2][2])-d3+d3))