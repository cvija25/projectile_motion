import numpy as np
import matplotlib.pyplot as plt

g = -9.81
ax = 0
vy = 0
t = 0
x = 0

h = float(input('Unesite visinu: '))
m = float(input('Unesite masu: '))
C = float(input('Unesite balisticki koeficijent: '))
S = float(input('Unesite povrsinu tela: '))
vx = float(input('Unesite pocetnu brzinu tela: '))

dt = 1e-3

H=[]
T=[]
R=[]

ro = 1.23

while h >= 0:
	
	v=np.sqrt(vx**2+vy**2)

	ax = -(C*S*ro*v*vx)/(2*m)
	vx += ax*dt
	x += vx*dt
	
	ay = g + (C*S*ro*v*vy)/(2*m)
	vy += ay*dt
	h += vy*dt
	
	t += dt
	
	H.append(h)
	T.append(t)
	R.append(x)

	
print('Vreme utroseno u letu: ' ,t)
print('Predjena distanca: ' ,x)
print('Maksimalna dostignuta brzina: ' ,np.sqrt(vx*vx + vy*vy))

plt.figure()
plt.plot(R, H)
plt.xlabel('Promena x ose [m]')
plt.ylabel('Promena visine [m]')
plt.title('Kretanje tela pri horizontalnom hicu')
plt.show()

