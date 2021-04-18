# install section
pip install numpy
pip install sympy
pip intall matplotlib

# library
import numpy as np
import sympy as sy
import matplotlib.pyplot as plt
plt.style.use('ggplot')

# quantity x
x = np.linspace(0,20,100)

# functions with visualization
'''
def supply(x, slope, intercept):
  qs = [intercept + slope * i for i in x]
  qs = {'quantity':qs, 'price':x}
  return qs

  def demand(x, slope, intercept):
  qd = [intercept - slope * i for i in x]
  qd = {'quantity':qd, 'price':x}
  return qd
'''

# functions with equations
def supply(x, slope, intercept):
  return intercept + slope * x

def demand(x, slope, intercept):
  return intercept - slope * x

# equilibrium point
q = sy.Symbol('q')
eq = sy.Eq(supply(q, 0.72, 19.4), demand(q, 1.8, 48.32))
p_eq = sy.solve(eq)[0]
q_eq = supply(p_eq, 0.72, 19.4)
print('\n','Price equilibrium:', p_eq, '\n',
      'Quantity equilibrium:', q_eq)


# draw supply and demand curve
plt.plot(supply(x, 0.72, 19.4), x,  label= 'Supply')
plt.plot(demand(x, 1.8, 48.32), x,  label= 'Demand')
plt.plot(q_eq, p_eq, 'o', markersize = 10, color='grey')

plt.hlines(y=3, xmin=0, xmax=42.96, color='green')
plt.vlines(21.56, 0, 14.86, linestyle="dashed")
plt.hlines(14.86, 0,  21.56, linestyle="dashed")

plt.vlines(27.66, 0, 11.47 , linestyle="dashed", color='grey')
plt.hlines(11.47, 0,  27.66, linestyle="dashed", color='grey')

plt.vlines(42.96, 0, 3, linestyles='dashed', color='green')
plt.margins(x=0, y=0)

ax = plt.axes()
ax.annotate(f'Equilibrium at \n ({round(q_eq, 2)}, {round(p_eq, 2)})', xy=(q_eq, p_eq), xytext=(q_eq+2, p_eq))
ax.annotate('A', xy=(10, 7.5), xytext=(10, 7.5), size=13)
ax.annotate('B', xy=(23, 12.5), xytext=(23, 12.5), size=13)
ax.annotate('C', xy=(23, 8.5), xytext=(23, 8.5), size=13)

plt.title("Supply and Demand")
plt.legend(frameon = False)
plt.xlabel("Quantity")
plt.ylabel("Price")

plt.savefig('curve.png', dpi=1200)
