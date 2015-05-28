import math

class Vector:
   def  __init__(self,n,vector=0):
         self.n = n
         if type(vector) == list:
            self.vector = vector
         else:
            self.vector = self.n * [vector]

   def  __str__(self):
      j=''
      if self.vector == self.n * [0]:
         for i in range(int(self.n)):
            i = str("{0:.6f}".format(0))
            j += i + "\n"
      else:
         for i in range (int(self.n)):
            i = str(float(self.vector[i]))
            j+= i + "\n"
      return j
      
   def _scalar_(self,alpha):
      return self.scalar(alpha)
      
   def scalar(self, alpha):
      temp = list(self.vector)
         
      for i in range(self.n):
         temp[i] = alpha * temp[i]
         
      sca = Vector(self.n, temp)
      return sca
      
   def _lincomb_(self, other, alpha, betha):
      return self.lincomb(other, alpha, betha)
   
   def lincomb(self, other, alpha, betha):
      v1= self.scalar(alpha).vector
      v2 = other.scalar(betha).vector
      
      for i in range (self.n):
         v1[i] = v1[i] + v2[i]
         
      comb = Vector(self.n, v1)
      return comb
      
   def _inner_(self, other):
      return self.inner(other)
   
   def inner(self, other):
      v1 = list(self.vector)
      v2 = list(other.vector)
         
      for i in range(self.n):
         v1[i]= float(v1[i]) * float(v2[i])
         
      som=0
      for j in range(self.n):
         som += v1[j]
      return som
      
   def _norm_(self):
      return self.norm()
      
   def norm(self):
      w = self.inner(self)
      return math.sqrt(w)