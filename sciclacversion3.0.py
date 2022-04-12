
from cmath import log10
from distutils.log import error
import math
from symtable import Symbol

import sympy
#from  sympy.abc import x,y
import sigfig
def round_it(x, sig):
        return round(x, sig-int(math.floor(math.log10(abs(x))))-1)
def truncate_it(f, n):
    return math.floor(f * 10 ** n) / 10 ** n
def findofm(num):
    return math.floor(math.log10(abs(num)))


    
class measurement(float):
    
    def limittosigfig(self):
        strval =str(self.value)
        if self.value < 1:
            i=0
            
            sfig = ''
            counter = 0
            counter = self.sfig + strval.count('.')
            numcheck=0 
            while counter != 1 and i <len(strval):
                print(strval[i])
                sfig += strval[i]
                if strval[i] in '123456789':
                    numcheck == 1
                
                if (strval[i]!='0' or numcheck == 1) and strval[i]!='.' and strval[i]!='-' :
                    
                    counter -= 1
                
                i+=1
                
            while counter >1:
                sfig +=  '0'
                counter -=1
            return sfig
        else:
            strval += (1-strval.count('.'))*'.'
            strval += self.sfig *'0'
            
            sfig = strval[:self.sfig + strval.count('.')]
            
            return sfig
           
    def __new__(self, value =0 , sigfigs = 1,error = 0,unit = '',symb = ''):
       
        
        



        return float.__new__(self,value)
    def __init__(self, value =0 , sigfigs = 1,error = 0,unit = '1',symb=''):
        self.error = float(error)
        self.sfig = sigfigs
        self.unit = unit
        self.value = value
        
        
        
    def __str__(self):
        return self.limittosigfig() + self.unit.replace('1','')+ " +- "+str(self.error) + self.unit.replace('1','') + " with "+str(self.sfig)+" significant figures" 
    def __add__(self, x ):
        print("added")
        
        #print(other)
        decs1 = len(self.limittosigfig()) -len(self.limittosigfig().split(".")[0]) - self.limittosigfig().count('.')
        decs2 =len(x.limittosigfig()) -len(x.limittosigfig().split(".")[0]) - self.limittosigfig().count('.')
        
        decs = min(decs1,decs2)
        

        outvalue = truncate_it(self.value,decs) + truncate_it(x.value,decs)
        if x.value > self.value:
            sigfigs = x.sfig
        else :
            sigfigs = self.sfig

        if findofm(outvalue)> findofm(max(x.value,self.value)):
            sigfigs +=1
        elif findofm(outvalue)< findofm(max(x.value,self.value)):
            sigfigs -=1
        if self.unit != x.unit :
            raise ValueError("Imposible to perform addition operation between different units")
        
        error = (self.error**2 + x.error ** 2)**0.5
        return measurement(outvalue,sigfigs,round_it(error, 1),self.unit)
    def __sub__(self, x ):
      
        
        
        decs1 = len(self.limittosigfig()) -len(self.limittosigfig().split(".")[0]) - self.limittosigfig().count('.')
        decs2 =len(x.limittosigfig()) -len(x.limittosigfig().split(".")[0]) - self.limittosigfig().count('.')
        
        decs = min(decs1,decs2)
        

        outvalue = truncate_it(self.value,decs) + truncate_it(-x.value,decs)
        if x.value > self.value:
            sigfigs = x.sfig
        else :
            sigfigs = self.sfig

        if findofm(outvalue)> findofm(max(x.value,self.value)):
            sigfigs +=1
        elif findofm(outvalue)< findofm(max(x.value,self.value)):
            sigfigs -=1
        if self.unit != x.unit :
            raise ValueError("Imposible to perform addition operation between different units")
        
        error = (self.error**2 + x.error ** 2)**0.5
        return measurement(outvalue,sigfigs,round_it(error, 1),self.unit)
    def __mul__(self, x):
        sigfigs = min(self.sfig,x.sfig)
        outvalue = self.value * x.value 
        error = error = (2*(self.error*x.error )**2)**0.5
        unit = ((self.unit + '*' +x.unit ).replace("*1",'')).replace('1*','')

        return measurement(outvalue,sigfigs,round_it(error, 1),unit)

    def __truediv__(self, x):
        sigfigs = min(self.sfig,x.sfig)
        newval = 1/x.value 
        outvalue = self.value * newval
        error = error = (2*(self.error*x.error )**2)**0.5

        
        if self.unit == x.unit:
            unit = '1'
        else:
            unit = ((self.unit + '/' +x.unit ).replace("/1",'')).replace('1/','/')
            

        return measurement(outvalue,sigfigs,round_it(error, 1),unit)
class expression():
    def __init__(self,strval,*args) -> None:
        self.args = args
        self.str = strval
        self.symstrs = []
        self.symbs = []
        self.symbs = sympy.symbols(self.args)    
        self.symexp = sympy.sympify(strval)
    def deriveall(self):
        derivs = []
        i=0
        while i < len(self.symbs):
            derivs.append(sympy.Derivative(self.symexp,self.symbs[i],evaluate = True ))
            i +=1 

        return derivs
    def derivetwice(self):
        derivs = []
        i=0
        while i < len(self.symbs):
            derivs.append(sympy.Derivative(sympy.Derivative(self.symexp,self.symbs[i],evaluate = True )))
            i +=1 

        return derivs
    def calcerrorexpr(self):
        self.errormatix = self.deriveall()
        c= 0
        for i in self.symbs:
            self.errormatix[c] =self.errormatix[c] * i   
            c +=1

        return self.errormatix

e = expression('a*b+12*c','a','b','c')
print(e.calcerrorexpr() )
            

        




        



  

 




        
        







