class Calculator:
    brand ='Casio-990ms'
    def add(self,num1,num2):
        s =num1+num2
        text =f'{num1} +{num2} = {s} '
        return text
    def sub(self,num1,num2):
         s =num1-num2
         text =f'{num1} - {num2} '
        
         return f'= {s}'
    def multi(self,num1,num2):
        s =num1*num2
        return s
    def div(self,num1,num2):
        s =num1/num2
        return s

cal= Calculator()
print(cal.brand)
print(cal.add(10,20))
# print(cal.sub(10,20))
# print(cal.multi(10,20))
# print(cal.div(10,20))
