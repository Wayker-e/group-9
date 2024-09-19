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