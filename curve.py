# install section
#pip install numpy
#pip install sympy
#pip intall matplotlib

# library
import numpy as np
import sympy as sy
import matplotlib.pyplot as plt
plt.style.use('ggplot')

class Market:
    x = np.linspace(0,20,100)
    
    def __init__(self, intercept_d, slope_d, intercept_s, slope_s, price_c=None):
        self.intercept_d = intercept_d
        self.slope_d = slope_d
        self.intercept_s = intercept_s
        self.slope_s = slope_s
        self.price_c = price_c

    def supply(self, price=None):
      if price == None:
        return self.intercept_s + self.slope_s * self.x
      else:
        return self.intercept_s + self.slope_s * price

    def demand(self, price=None):
      if price == None:
        return self.intercept_d - self.slope_d * self.x
      else:
        return self.intercept_d - self.slope_d * price
    
    def equilibrium(self):
      '''
      p_eq: equilibrium price
      q_eq: equilibrium quantity
      '''
      p_eq = p_eq = (self.intercept_d - self.intercept_s)/(self.slope_d + self.slope_s)
      q_eq = self.supply(p_eq)
      self.p_eq = p_eq
      self.q_eq = q_eq
      print('\n','Price equilibrium:', round(p_eq, 2), '\n', 
            'Quantity equilibrium:', round(q_eq, 2))
      return p_eq, q_eq


    def new_equilibrium(self, var_price_ceiling=None):
        '''
        q_ceiling: new equilibrium quantity
        p_ceiling = new equilibrium price
        d_point_ceiling = new demand required
        '''
        if var_price_ceiling == None:
          q_ceiling =  self.intercept_s + self.slope_s * self.price_c
          p_ceiling =  (q_ceiling - self.intercept_d)/ (- self.slope_d)
          d_point_ceiling = self.intercept_d - self.slope_d * self.price_c
        else:
          q_ceiling =  self.intercept_s + self.slope_s * var_price_ceiling
          p_ceiling =  (q_ceiling - self.intercept_d)/ (- self.slope_d)
          d_point_ceiling = self.intercept_d - self.slope_d * var_price_ceiling
          self.price_c = var_price_ceiling

        self.q_ceiling = q_ceiling
        self.p_ceiling = p_ceiling
        self.d_point_ceiling = d_point_ceiling

        print('\n','New Price equilibrium:', round(self.q_ceiling, 2), '\n', 
              'New Quantity equilibrium:', round(self.p_ceiling, 2), '\n',
              'New Demand Required:', round(self.d_point_ceiling, 2))
        return  q_ceiling, p_ceiling, d_point_ceiling
    
    def plot(self, price_ceiling=False):
        try:
            plt.plot(self.supply(), self.x,  label= 'Supply')
            plt.plot(self.demand(), self.x,  label= 'Demand')
            plt.plot(self.q_eq, self.p_eq, 'o', markersize = 10, color='grey')

            ax = plt.axes()
            ax.annotate(f'Equilibrium at \n ({round(self.q_eq, 2)}, {round(self.p_eq, 2)})', 
                        xy=(self.q_eq, self.p_eq), 
                        xytext=(self.q_eq+2, self.p_eq), fontsize=7) 
        except AttributeError:
            print('You didn\'t call the "equilibrium" function')

        if price_ceiling != False:
            plt.hlines(y=self.price_c, xmin=0, xmax=self.d_point_ceiling, color='green', label='Price Ceiling')    
            plt.vlines(self.d_point_ceiling, 0, self.price_c, linestyles='dashed', color='green')
            plt.vlines(self.q_ceiling, 0, self.p_ceiling, linestyle="dashed", color='black')
            plt.hlines(self.p_ceiling, 0,  self.q_ceiling, linestyle="dashed", color='black')

            ax.annotate(f'({round(self.q_ceiling, 2)}, {round(self.p_ceiling, 2)})', 
                        xy=(self.q_ceiling, self.p_ceiling), 
                        xytext=(self.q_ceiling, self.p_ceiling+1), fontsize=7)
            
            ax.annotate(f'({round(self.d_point_ceiling, 2)}, {round(self.price_c, 2)})', 
                        xy=(self.d_point_ceiling, self.price_c), 
                        xytext=(self.d_point_ceiling-1, self.price_c+1), fontsize=7)

            

        plt.vlines(self.q_eq, 0, self.p_eq, linestyle="dashed", color='grey')
        plt.hlines(self.p_eq, 0, self.q_eq, linestyle="dashed", color='grey')

        plt.margins(x=0, y=0)
        plt.title("Supply and Demand")
        plt.legend(frameon = False, loc=1)
        plt.xlabel("Quantity")
        plt.ylabel("Price")
        plt.savefig('curve.png', dpi=1200)
        p = plt.show(block=True)
        return p
