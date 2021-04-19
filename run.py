import curve

# criação do objeto
mercado = curve.Market(48.32, 1.8, 19.4, 0.72, 3.0)

# plot with equilibrium point
mercado.equilibrium()
mercado.plot()

# plot with new equilibrium point after price ceiling #3
mercado.new_equilibrium()
mercado.plot(True)

# plot with new equilibrium point after price ceiling #5
mercado.new_equilibrium(5)
mercado.plot(True)