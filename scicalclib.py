from cgi import print_environ
from copy import error
from email.mime import message
import math
import sympy
def round_it(x, sig):
        return round(x, sig-int(math.floor(math.log10(abs(x))))-1)
class measurement(float):
    
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
        value = round_it(value, importantdigits)

        return (value,importantdigits,error,self.unit+"*"+self.unit)

    def __add__(self, other) :
        self.impd = min(self.impd,other.impd)
        other.impd = self.impd
        self.value = float(self.limittosigfig()) 
        other.value = float(other.limittosigfig()) 
        outvalue =super().__add__(other)
        if len(str(outvalue))> self.impd:
            sigfig = len(str(outvalue))
        else :
            sigfig = self.impd
        out = measurement(outvalue,sigfig,self.error + other.error,self.unit)
        return out
    def __sub__(self, other: float) :
        self.impd = min(self.impd,other.impd)
        other.impd = self.impd
        self.value = float(self.limittosigfig()) 
        other.value = float(other.limittosigfig()) 
        outvalue =super().__sub__(other)
        
        out = measurement(outvalue,self.impd,self.error + other.error,self.unit)
        return out
    
        
a = measurement(14.199,7,0.001,"cm")-measurement(14.1,7,0.001,"cm")
print(a)


    


    