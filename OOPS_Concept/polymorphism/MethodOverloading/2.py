class Adding:

    ## Passing Default Arguments 
    def add(self,a = None, b = None, c= None ):
        sum = 0
        if a!=None and b!=None and c!=None:
            sum = a + b + c
            
        elif(a!=None and b!=None and c==None):
            sum = a + b

        return sum 

obj = Adding()
print(obj.add(10, 20))
print(obj.add(10, 20, 30))
