cmd="run"
t=0

class Food:
    def __init__(self,name,code,rate):
        self.name=name
        self.code=code
        self.rate=rate
    
    def calculate(self,quantity):
        r=self.rate*quantity
        return r


hot_coffee=Food("Hot coffee",1,70)
cold_coffee=Food("cold coffee",2,100)
cold_coffee_icecream=Food("cold coffee (ice cream)",3,120)
french_fries  =Food("french fries",4,60)
pizza =Food("pizza",5,100)
Sandwich=Food("Sandwich",6,80)
capichino=Food("capichino",7,130)
Masala_french_fries=Food("Masala french fries ",8,70)
icecream_scops =Food("icecream (scops)    ",9,50)
soda=Food("soda",10,20)


def menu():
    print("\n*****WELCOME MAGIC CAFE*****\n")

    print("\n1:Hot coffee         `     Rs 70")
    print("2:cold coffee                Rs 100")
    print("3:cold coffee (ice cream)    Rs 120")
    print("4:french fries               Rs 60")
    print("5:pizza                      Rs 100")
    print("6:Sandwich                   Rs 80")
    print("7:capichino                  Rs 130")
    print("8:Masala french fries        Rs 70")
    print("9:icecream (scops)           Rs 50 per/-")
    print("10:soda                      Rs 20")
    print("00.exit")
    print("\n*********************************************\n")

menu()

str=""
print("Your order please :")
print("\nenter a code of item ,you will like to have ?")
while cmd=="run":
    
    order=int(input("code : "))

    if  order==1:
        q=int(input("Number of ingredients :"))
        cost=hot_coffee.calculate(q)
        t=t+cost
        str=str+ f"hot coffee               {hot_coffee.rate} X {q}     Rs {cost}\n"
        print(str)
        print("Total So Far :",t)

    elif order ==2:
        q=int(input("Number of ingredients : "))
        cost=hot_coffee.calculate(q)
        t=t+cost        
        str=str+ f"cold coffee              {cold_coffee.rate} X {q}    Rs {cost}\n"
        print(str)
        print("Total So Far :",t)


    

    elif order ==3:
        q=int(input("Number of ingredients : "))
        cost=cold_coffee_icecream.calculate(q)
        t=t+cost        
        print(str)
        print("Total So Far :",t)


        
        str=str+ f"cold_coffee_icecream     {cold_coffee_icecream.rate} X {q}    Rs {cost}\n"
    elif order ==4:
        q=int(input("Number of ingredients : "))
        cost=french_fries.calculate(q)
        t=t+cost        
        str=str+ f"french_fries             {french_fries.rate} X {q}    Rs {cost}\n"
        print(str)
        print("Total So Far :",t)

   
    elif order ==5:
        q=int(input("Number of ingredients : "))
        cost=pizza.calculate(q)
        t=t+cost        
        str=str+ f"pizza                    {pizza.rate} X {q}    Rs {cost}\n"
        print(str)
        print("Total So Far :",t)

    elif order ==6:
        q=int(input("Number of ingredients : "))
        cost=Sandwich.calculate(q)
        t=t+cost        
        str=str+ f"Sandwich                 {Sandwich.rate} X {q}    Rs {cost}\n"
        print(str)
        print("Total So Far :",t)

    elif order ==7:
        q=int(input("Number of ingredients : "))
        cost=capichino.calculate(q)
        t=t+cost        
        str=str+ f"capichino                {capichino.rate} X {q}    Rs {cost}\n"
        print(str)
        print("Total So Far :",t)
    
    elif order ==8:
        q=int(input("Number of ingredients : "))
        cost=Masala_french_fries.calculate(q)
        t=t+cost        
        str=str+ f" Masala_french_fries     {Masala_french_fries.rate} X {q}    Rs {cost}\n"
        print(str)
        print("Total So Far :",t)
    
    elif order ==9:
        q=int(input("Number of ingredients : "))
        cost=icecream_scops.calculate(q)
        t=t+cost        
        str=str+ f"icecream_scops           {icecream_scops.rate} X {q}    Rs {cost}\n"
        print(str)
        print("Total So Far :",t)

    elif order ==10:
        q=int(input("Number of ingredients : "))
        cost=soda.calculate(q)
        t=t+cost        
        str=str+ f"soda                     {soda.rate} X {q}    Rs {cost}\n"
        print(str)
        print("Total So Far :",t)

    elif order ==00:
        print("\nYour Bill  :\n")
        print (str)

        print("***************************************************\n")
        print(f"Total amount     -->                 Rs { t}       ")

        print("\nThank you so much for visiting Magic cafe")
        cmd="quit"
    

    else:
        print("Invalid code ")

        

