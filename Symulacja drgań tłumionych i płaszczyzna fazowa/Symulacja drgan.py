## Skrypt realizujący symulacje dla przykładu z wahadłem matematycznym bez tłumienia 
import numpy as np
import matplotlib.pyplot as plt
import pylab
#from matplotlib import pyplot as plt
plt.rcParams['figure.figsize']=[12,7]
plt.rcParams['figure.dpi'] = 150
# ----------------------------------------------------------------------------------
print("|-------------------------------------------------------------|")
print("|Damian Skuraś | Informatyka III rok | VI semestr | Nr:142873 |")
print("|Zadanie: Symulacja drgańtłumionych i analiza fazowa          |")
print("|-------------------------------------------------------------|")
# ----------------------------------------------------------------------------------
# Dane wejściowe|
g = 9.81
l = 1.2
# ----------------------------------------------------------------------------------
# Model Matematyczny|
A = np.identity(2)
B = np.zeros((2,2))
# ----------------------------------------------------------------------------------
# Zapewnienie spójności modelu|
B[1,0] = -1
# ----------------------------------------------------------------------------------
# Wprowadzenie współczynnika tłumienia do ukłądu równan |
B[0,0] = 0.5
# ----------------------------------------------------------------------------------
# Tworzenie pustego wektoru prawej strony ukłądu równań|
F = np.zeros((2,1))
# ----------------------------------------------------------------------------------
# Definicja dziedziny czasu| Warunki symulacji |
t0 = 0
tf = 20
dt = 1E-4
t = np.arrange(t0,tf,dt)
# Warunki początkowe | wektor dwuelementowy |
y0 = np.array([[9],[0*np.pi]])
# Alokacja pamięci
wyn = np.zeros((2, t.size))
Result = y0.copy()
for i in range(0,max(y0.shape)):
    wyn[i,0] = y0[i]
f = lambda x:(-g/l)*np.sin(x)
# Wprowadzenie funkcji metodą Eulera |
for k in range (0,max(t.shape)-1):
    F[0] = f(Result[1])
    Result += np.linalg.inv(A) @ (F - B @ Result)*dt
    wyn[0, k+1] = Result[0]
    wyn[1, k+1] = Result[1]
# Rysowanie wykresu |
fig, axs = plt.subplots(2)
axs[0].plot(t, wyn)
axs[0].gird()
axs[0].set_ylabel('Czas')
axs[1].plot(t, wyn[1, :])
axs[1].gird()
axs[1].set_xlabel('Wartosc analizy')  
axs[1].set_ylabel('Theta')
axs[1].set_title('Wahadlo')
# Model Matematyczny|
A = np.identity(2)
B = np.zeros((2,2))
# ----------------------------------------------------------------------------------
# Zapewnienie spójności modelu|
B[1,0] = -1
# ----------------------------------------------------------------------------------
# Wprowadzenie współczynnika tłumienia do ukłądu równan |
B[0,0] = 0.5
# ----------------------------------------------------------------------------------
# Tworzenie pustego wektoru prawej strony ukłądu równań|
F = np.zeros((2,1))
# ----------------------------------------------------------------------------------
# Definicja dziedziny czasu| Warunki symulacji |
t0 = 0
tf = 20
dt = 1E-4
t = np.arrange(t0,tf,dt)
# Warunki początkowe | wektor dwuelementowy |
y0 = np.array([[9],[0*np.pi]])
# Alokacja pamięci
wyn = np.zeros((2, t.size))
Result = y0.copy()
for i in range(0,max(y0.shape)):
    wyn[i,0] = y0[i]
f = lambda x:(-g/l)*np.sin(x)
# Wprowadzenie funkcji metodą Eulera |
for k in range (0,max(t.shape)-1):
    F[0] = f(Result[1])
    Result += np.linalg.inv(A) @ (F - B @ Result)*dt
    wyn[0, k+1] = Result[0]
    wyn[1, k+1] = Result[1]
plt.figure(2)
plt.quiver(theta, omega, ph[:,:,1], ph[:,:,0], minshaft=0.2, color='blue', headwidth=2, headlength=5, 
          headaxislength=3)
plt.xlabel('theta')
plt.ylabel('omega')
plt.title('plaszczyzna fazowa')
plt.grid()
# -- dodaje przebieg rozwiazania
plt.plot(wyn[1,:], wyn[0,:], color='red')