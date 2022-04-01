
import math
import sympy
def round_it(x, sig):
        return round(x, sig-int(math.floor(math.log10(abs(x))))-1)


    
class measurement(float):
    
    def limittosigfig(self):
        sfig = (str(self.value)+(self.impd*"0"))[:self.impd+1]
        return sfig
    def __new__(self, value, importantdigits,error,unit):
        value = float((str(value)+(importantdigits*"0"))[:importantdigits+1])
        self.value = value
        return float.__new__(self,value)
    def __init__(self, value, importantdigits,error,unit):
        self.error = error
        self.impd = importantdigits
        self.unit = unit
        float.__init__(value)
    def __str__(self):
        return self.limittosigfig()+self.unit+ " +- "+str(self.error) + self.unit + " with "+str(self.impd)+"significant figures" 
        
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

    def __add__(self, other) :
        newsigfig = min(self.impd,other.impd)
        other.impd = newsigfig
        self.impd = newsigfig
        self.value = float(self.limittosigfig()) 
        other.value = 15.000
        addedterm = measurement(float(other.limittosigfig()),newsigfig,other.error,other.unit)
        
        print(other)
        print(self)
        outvalue =super().__add__(other)
        
        if len(str(outvalue))> self.impd:
            sigfig = self.impd + 1
        else :
            sigfig = self.impd
        out = measurement(outvalue,sigfig,self.error + other.error,self.unit)
        
        return out

    def __sub__(self, other: float) :
        self.impd = min(self.impd,other.impd)
        other.impd = self.impd-1
        self.value = float(self.limittosigfig()) 
        other.value = float(other.limittosigfig()) 
        outvalue =super().__sub__(other)
        
        out = measurement(outvalue,self.impd,self.error + other.error,self.unit)

        return out
    
        
a = measurement(5.134,5,0,'')+measurement(7.4857 ,5,0,'')
print(a)

    