import curve

# criação do objeto
mercado = curve.Market(48.32, 1.8, 19.4, 0.72, 3.0)
print(mercado.equilibrium())

mercado.new_equilibrium()
mercado.plot()
mercado.plot(True)