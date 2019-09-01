class student:
    
    school="BNCV"
    
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    
    
    def avg(self):
        
        return ((self.m1+self.m2)/2)
        
        '''
        DECORATORS:::::
        
        if we are working with class we have to use @classmethod
        if we are using static method we have to use @staticmethod
        we will use static method when we are not working with class(cls) as well as objects(self) 
        '''
    @staticmethod
    def static_info():
        print("it's a static so i'm independent:::::")
        
        
    @classmethod
    def class_info(cls):                  #it's a decorator 
        return cls.school
        
s1=student(10,90)
s2=student(60,70)

print(s1.avg())
print(s2.avg())
print(s1.m2)

print(s1.class_info())
student.static_info()