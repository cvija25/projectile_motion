import numpy as np
import matplotlib.pyplot as plt

g = -9.81
a = 0
t = 0
h = 0

m = float(input('Unesite masu: '))
Cd = float(input('Unesite balisticki koeficijent: '))
S = float(input('Unesite povrsinu tela: '))
v = float(input('Unesite pocetnu brzinu: '))

k = 0.6*Cd

dt = 1e-2

if Cd == 0:
	Vt = 0
else:
	Vt = np.sqrt((2*m*9.81)/(1.2*S*Cd))

H = np.array([h])
T = np.array([0])
counter = 0

while H[counter] >= 0:

	counter += 1
	
	if v >= 0:
		a = g - ((v*k)*(v*S)/m)
	else:
		a = g + ((v*k)*(v*S)/m)
	
	v += a*dt
	h += v*dt
	t += dt	
		
	H = np.append(H, h)
	T = np.append(T, t)
	
print('\n\n\n\n')
print('Vreme utroseno u letu: ' ,round(t, 4))
print('Maksimalna dostignuta visina: ', round(np.amax(H), 4))
print('Vreme utroseno pre slobodnog pada: ', round(T[np.argmax(H)], 4))
print('Vreme utroseno pri slobodnom padu: ', round(t - T[np.argmax(H)], 4))
print('Maksimalna dostignuta brzina pri slobodnom padu: ' ,-round(v, 4))


if Vt != 0:

	if -round(v, 0) == round(Vt, 0):
		print('Dostignuta je terminalna brzina.')
	
	else:
		print('Nije dostignuta terminalna brzina(',round(Vt, 4), ').')

	
plt.figure()
plt.plot(T, H)
plt.xlabel('Promena vremena [s]')
plt.ylabel('Promena visine [m]')
plt.title('Kretanje tela pri hicu navise')
plt.show()

input('....')	



