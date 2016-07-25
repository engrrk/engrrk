class rectangle:
   def __init__(self,l,w ):
      self.name = 'RECTANGLE'
      self.l = l
      self.w = w

   def getarea(self):
      return self.l * self.w


m = rectangle(6,4)

print(m.getarea())
# above and below are two ways
print(rectangle.getarea(m))


#http://zetcode.com/lang/python/oop/