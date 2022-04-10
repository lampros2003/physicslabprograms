
from cmath import sqrt
import math
import sympy
import sigfig

def round_it(x, sig):
        return round(x, sig-int(math.floor(math.log10(abs(x))))-1)


    
class measurement(float):
    def leadingzzero(self):
        i=0
        while str(self.value)[i]=='0' or str(self.value)[i]=='.':
            i +=1 
            self.nm +=1



    def limittosigfig(self):
        adjustment = 0 
        if self.value>1:
            adjustment += 1
        sfig = (str(self.value)+(self.impd*"0"))[:self.impd+adjustment-1]
        return sfig
    def __new__(self, value, importantdigits,error,unit):
        
        self.value = value
        return float.__new__(self,value)
    def __init__(self, value, importantdigits,error,unit):
        float.__init__(value)
        self.error = float(error)
        self.nm = 0
        self.leadingzzero()
        self.impdtoprint = importantdigits
        self.impd = importantdigits+ self.nm
        
        self.unit = unit
        
        
    def __str__(self):
        return self.limittosigfig()+self.unit+ " +- "+str(self.error) + self.unit + " with "+str(self.impdtoprint-self.nm )+" significant figures" 
        
    def __mul__(self, __x) :
        value = super().__mul__(__x)
        importantdigits = min(self.impd,__x.impd)
        error = self.error
        value = round_it(value, importantdigits)
        out = measurement(value,importantdigits,error,self.unit+"*"+self.unit)
        
        return out

    def __truediv__(self, other) :
        value = super().__truediv__(other)
        importantdigits = min(self.impd,other.impd)
        value = round_it(value, importantdigits)
        error = self.error
        out = measurement(value,importantdigits,error,self.unit+"*"+self.unit)
        return out
    
    def __add__(self, x ) :

        if x.unit != self.unit:
            raise Exception("Addition operation between different units is not possible")
        out = measurement(0,6,0,'')
        out.error = round_it((self.error**2 + x.error**2)**0.5,1)

        out.value = super().__add__(x)
        out.impd = (min (self.impd , x.impd))
        out.limittosigfig
        return out
        

        
        

    def __sub__(self, other: float) :
        self.impd = min(self.impd,other.impd)
        other.impd = self.impd-1
        self.value = float(self.limittosigfig()) 
        other.value = float(other.limittosigfig()) 
        outvalue =super().__sub__(other)
        
        out = measurement(outvalue,self.impd,self.error + other.error,self.unit)

        return out
    
        
a = measurement(5,4,0.04,'') * measurement(0.5,4,0.04,'') 
print(a)

    