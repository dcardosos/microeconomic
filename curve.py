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


    def new_equilibrium(self, var_price_celling=None):
        '''
        q_celling: new equilibrium quantity
        p_celling = new equilibrium price
        d_point_celling = new demand required
        '''
        if var_price_celling == None:
          q_celling =  self.intercept_s + self.slope_s * self.price_c
          p_celling =  (q_celling - self.intercept_d)/ (- self.slope_d)
          d_point_celling = self.intercept_d - self.slope_d * self.price_c
        else:
          q_celling =  self.intercept_s + self.slope_s * var_price_celling
          p_celling =  (q_celling - self.intercept_d)/ (- self.slope_d)
          d_point_celling = self.intercept_d - self.slope_d * var_price_celling

        self.q_celling = q_celling
        self.p_celling = p_celling
        self.d_point_celling = d_point_celling

        print('\n','New Price equilibrium:', round(self.q_celling, 2), '\n', 
              'New Quantity equilibrium:', round(self.p_celling, 2), '\n',
              'New Demand Required:', round(self.d_point_celling, 2))
        return  q_celling, p_celling, d_point_celling
    
    def plot(self, price_celling=False):
        plt.plot(self.supply(), self.x,  label= 'Supply')
        plt.plot(self.demand(), self.x,  label= 'Demand')
        plt.plot(self.q_eq, self.p_eq, 'o', markersize = 10, color='grey')

        ax = plt.axes()
        ax.annotate(f'Equilibrium at \n ({round(self.q_eq, 2)}, {round(self.p_eq, 2)})', 
                    xy=(self.q_eq, self.p_eq), 
                    xytext=(self.q_eq+2, self.p_eq), fontsize=7)
        
        if price_celling != False:
            plt.hlines(y=self.price_c, xmin=0, xmax=self.d_point_celling, color='green', label='Price Ceiling')    
            plt.vlines(self.d_point_celling, 0, self.price_c, linestyles='dashed', color='green')
            plt.vlines(self.q_celling, 0, self.p_celling, linestyle="dashed", color='black')
            plt.hlines(self.p_celling, 0,  self.q_celling, linestyle="dashed", color='black')

            ax.annotate(f'({round(self.q_celling, 2)}, {round(self.p_celling, 2)})', 
                        xy=(self.q_celling, self.p_celling), 
                        xytext=(self.q_celling, self.p_celling+1), fontsize=7)
            
            ax.annotate(f'({round(self.d_point_celling, 2)}, {round(self.price_c, 2)})', 
                        xy=(self.d_point_celling, self.price_c), 
                        xytext=(self.d_point_celling-1, self.price_c+1), fontsize=7)

            

        plt.vlines(self.q_eq, 0, self.p_eq, linestyle="dashed", color='grey')
        plt.hlines(self.p_eq, 0, self.q_eq, linestyle="dashed", color='grey')

        plt.margins(x=0, y=0)
        plt.title("Supply and Demand")
        plt.legend(frameon = False, loc=1)
        plt.xlabel("Quantity")
        plt.ylabel("Price")
        p = plt.plot()
        return p