import numpy as np
import matplotlib.pyplot as plt

g = 9.81

m = float(input('Unesite masu: '))
C = float(input('Unesite balisticki koeficijent: '))
S = float(input('Unesite povrsinu tela: '))
v0 = float(input('Unesite pocetnu brzinu tela: '))
alfa = np.deg2rad(float(input('Unesite ugao izbacaja tela: ')))

dt = 1e-3

vx=v0*np.cos(alfa)
vy=v0*np.sin(alfa)

# Bez otpora
X=[] 
Y=[]

t = 0
x=0; y=0

while y>=0:
    vy+=-g*dt
    x+=vx*dt
    y+=vy*dt
    t+=dt
    X.append(x)
    Y.append(y)

# Sa otporom
ro=1.23

Xo=[]
Yo=[]

to = 0
xo=0; yo=0
vxo=v0*np.cos(alfa); vyo=v0*np.sin(alfa)

#Fo = -(C*S*ro*v**2)/2

while yo>=0:
    vo=np.sqrt(vxo**2+vyo**2)
    axo=-C*S*ro*vo*vxo/(2*m)
    ayo=-g-C*S*ro*vo*vyo/(2*m)

    vxo+=axo*dt
    vyo+=ayo*dt
    xo+=vxo*dt
    yo+=vyo*dt

    to+=dt

    Xo.append(xo)
    Yo.append(yo)

X=np.array(X)
Y=np.array(Y)
Xo=np.array(Xo)
Yo=np.array(Yo)

#bez otpora
H = np.amax(Y)
Domet = X[-1]

#sa otporom
Ho=np.amax(Yo)
DometO = Xo[-1]


print('Vreme leta bez otpora = ',t,'\n')
print('Vreme leta sa otporom = ',to,'\n')
print('Domet bez otpora = ',Domet,'\n')
print('Domet sa otporom = ',DometO,'\n')
print('Maksimalna visina bez otpora = ',H,'\n')
print('Maksimalna visina sa otporom = ',Ho,'\n')

plt.figure()
plt.plot(X, Y, 'b')
plt.plot(Xo, Yo, 'r')
plt.plot(X[np.argwhere(Y==H)],H,'ob')
plt.plot(Xo[np.argwhere(Yo==Ho)],Ho,'or')
plt.plot(Domet,Y[-1],'ob')
plt.plot(DometO,Yo[-1],'or')

plt.show()
