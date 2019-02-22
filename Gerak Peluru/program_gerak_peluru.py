"""
Created on Fri Feb 15 20:01:39 2019

@author: taufikfathurahman
"""
import numpy as  np
import matplotlib.pyplot as plt

def deltaT(T, N):
    '''
        I.S : telah terdefini input T dan N dari user
        F.S : Mengembalikan nilai delta T
    '''
    return T/N

def solusi_eksak(T, N, V0, X0, Y0, theta, g):
    '''
        I.S : telah terdefini input dari user
        F.S : Mengembalikan nilai solusi eksak X dan Y
    '''
    X = []
    Y = []
    X.append(X0)
    Y.append(Y0)

    for i in range(N):
        X.append(i * deltaT(T, N) * V0 * np.cos(theta))
        Y.append(-(0.5) * g * (i * deltaT(T, N)) ** 2 + (i * deltaT(T, N)) * V0 * np.sin(theta))

    return X, Y

def solusi_numerik(T, N, V0, X0, Y0, theta, g):
    '''
        I.S : telah terdefini input dari user
        F.S : Mengembalikan nilai solusi numerik X dan Y
    '''
    Vx = V0 * np.cos(theta)
    Vy = []
    Vy.append(V0 * np.sin(theta))
    X = []
    Y = []
    X.append(X0)
    Y.append(Y0)

    for i in range(N):
        X.append(X[i] + Vx * deltaT(T,N))
        Vy.append((-g) * deltaT(T, N) + Vy[i])
        Y.append(Y[i] + Vy[i+1] * deltaT(T, N))

    return X, Y

def make_plot(X1, Y1, X2, Y2):
    '''
        I.S : Telah terdefinisi nilai dari X dan Y untuk solusi eksak dan numerik
        F.S : Mengembalikan nilai solusi numerik X dan Y
    '''
    # Melakukan plot untuk solusi eksak
    fig = plt.figure()
    rect = fig.patch
    rect.set_facecolor('grey')
    ax1 = fig.add_subplot(2, 2, 1)
    ax1.plot(X1, Y1, label='Hasil Eksak')
    ax1.set_title('Plot Solusi Eksak')
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')

    # Melakukan plot untuk solusi numerik
    ax2 = fig.add_subplot(2, 2, 2)
    ax2.scatter(X2, Y2, color='pink', label='Solusi Numerik')
    ax2.set_title('Plot Solusi Numerik')
    ax2.set_xlabel('X')
    ax2.set_ylabel('Y')

    # Melakukan plot kobinasi antara solusi eksak dan numerik utuk melihat perbedaan
    ax3 = fig.add_subplot(2, 1, 2)
    ax3.plot(X1, Y1, label='Solusi Numerik')
    ax3.scatter(X2, Y2, color='pink', label='Solusi Numerik')
    ax3.set_title('Plot Solusi Numerik & Eksak')
    ax3.set_xlabel('X')
    ax3.set_ylabel('Y')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    print('-----Input Nilai-----')
    T = int(input("1. Nilai T       : "))
    N = int(input("2. Nilai N       : "))
    V0 = int(input("3. Nilai V0      : "))
    X0 = int(input("4. Nilai X0      : "))
    Y0 = int(input("5. Nilai Y0      : "))
    g = int(input("6. Nilai g       : "))
    theta = np.pi/3
    
    X1, Y1 = solusi_eksak(T, N, V0, X0, Y0, theta, g)       # memanggil fungsi solusi eksak
    X2, Y2 = solusi_numerik(T, N, V0, X0, Y0, theta, g)     # memanggil fungsi solusi numerik

    make_plot(X1, Y1, X2, Y2)                               # memanggil procedure untuk melakukan plot