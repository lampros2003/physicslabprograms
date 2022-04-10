from cmath import sqrt
import math
from requests import put
import sympy
import sigfig
def round_it(x, sig):
        return round(x, sig-int(math.floor(math.log10(abs(x))))-1)


    
class measurement(float):
    
    def limittosigfig(self):
        sfig = (str(self.value)+(self.impd*"0"))[:self.impd+1]
        return sfig
    def __new__(self, value ,sigfigs,error,unit):
        value = float((str(value)+(sigfigs*"0"))[:sigfigs+1])
        self.value = value
        
        



        return float.__new__(self,value)
    def __init__(self, value, sigfigs,error,unit):
        self.error = float(error)
        self.sfig = sigfigs
        self.unit = unit
        float.__init__(value)
    def __str__(self):
        return self.limittosigfig()+self.unit+ " +- "+str(self.error) + self.unit + " with "+str(self.impd)+" significant figures" 
        