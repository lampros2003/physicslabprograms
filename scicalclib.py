from copy import error
import math
import sympy

class measurement(float):
    def round_it(x, sig):
        return round(x, sig-int(math.floor(math.log10(abs(x))))-1)
    def limittosigfig(self):
        sfig = (str(self.value)+(self.impd*"0"))[:self.impd+1]
        return sfig
    def __new__(self, value, importantdigits,error,unit):
        value = float(format(value,'.'+str(importantdigits+1)+'g'))
        self.value = value
        return float.__new__(self,value)
    def __init__(self, value, importantdigits,error,unit):
        self.error = error
        self.impd = importantdigits
        self.unit = unit
        float.__init__(value)
    def __str__(self):
        return self.limittosigfig()+self.unit+ " +- "+str(self.error) + self.unit
        
    def __mul__(self, __x) :
        value = super().__mul__(__x)
        importantdigits = min(self.impd,__x.impd)
        error = self.error

        return (value,importantdigits,error,self.unit+"*"+self.unit)

    
        
a = measurement(14.199,6,0.001,"cm")*measurement(14.1,6,0.001,"cm")
print(measurement(a[0],a[1],a[2],a[3]))
    


    