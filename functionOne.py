import numpy as np
from matplotlib import pyplot as plt
import math

t = np.linspace(0, 5, 800)
fx = np.exp(-t)
xi = 0.25
xih = 1
true_value = math.exp(-xih)
print("true value = ",+true_value)

orders = {}
orders["0"] =  math.exp(-xi)
orders["1"] = orders["0"] - orders["0"] * (xih - xi)
orders["2"] =  orders["1"] + (orders["0"] * math.pow(xih - xi,2)) / math.factorial(2)
orders["3"] =  orders["2"] - (orders["0"] * math.pow(xih - xi,3)) / math.factorial(3)

for order in orders:
    print("Order ",order," = ",+orders[order])

print("==========================================")

for order in orders:
    print("Et",order," = ",+((true_value - orders[order]) / true_value) * 100 )

plt.plot(t, fx, label='exp ^ -x')
plt.plot(1, true_value,'bo',label='Xi + 1')
plt.axhline(y=true_value, color='b', linestyle='-')
plt.plot(0.25, orders["0"],"go", label='Xi / Order 0')
plt.plot(0.25, orders["1"],'x', label='Order 1')
plt.plot(0.25, orders["2"],'x', label='Order 2')
plt.plot(0.25, orders["3"],'x', label='Order 3')
plt.legend()
plt.grid(True)
plt.title('Taylor Series Approximation')
plt.show()