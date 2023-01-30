
numberone=float(input ("x1= "))
while True: 
    print("Введите знак операции")
    znak = input()
  
   
    if znak in ('+','-','/','*','^'):
        
        result=float
        if znak=='+':
            numbertwo=float(input ("x2= "))
            numberone=numberone+numbertwo
            print(numberone)
            
        if znak =='-':
            numbertwo=float(input ("x2= "))
            numberone=numberone-numbertwo
            print(numberone)
        if znak=='*':
            numbertwo=float(input ("x2= "))
            numberone=numberone*numbertwo
            print(numberone)
         
        if znak=='/':
            numbertwo=float(input ("x2= "))
            if numbertwo==0:
                print("Деление на ноль невозможно")
            elif numbertwo>0:
                numberone=numberone/numbertwo
                print(numberone)
              
        if znak=='^':
            numbertwo=float(input ("x2= "))
            numberone=pow(numberone,numbertwo)
            print(numberone)
    else:
        print("Неверная операция")
  

        
       
            

       

