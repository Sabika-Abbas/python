import matplotlib.pyplot as plt

#Flashlight
If=[36,9,5,2,1]
#Candle
Ic=[0,0,0,0,0]
#LED Bulb
Il=[285,84,43,25,17]
#X-axis
X=[1,2,3,4,5]

plt.plot(X,If, c="purple", marker="o",label="Flashlight")
plt.plot(X,Ic, c="blue", marker="o",label="Candle")
plt.plot(X,Il, c="green", marker="o",label="Led Bulb")

plt.xlabel("Distance (d) [m]")
plt.ylabel("Intensity (I) [lux]")
plt.title("Intensity vs. Distance for from Source")
plt.legend()
plt.xlim(1,5)
plt.show()
