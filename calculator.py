num1=float(input("""

Lütfen Birinci Sayiyi Giriniz :

"""))
num2=float(input("""

Lüfen İkinci Sayiyi Giriniz:
                 
"""))

op=input("""
Bir İslem Seciniz 
(+,-,*,/,^): 

""")

while True:
    if op=="+":
        print(num1,"+",num2,"=",num1+num2)
    elif op=="-":
        print(num1,"-",num2,"=",num1-num2)
    elif op =="*":
        print(num1,"*",num2,"=",num1*num2)
    elif op=="/":
        print(num1,"/",num2,"=",num1/num2)
    elif op=="^":
        print(num1,"^",num2,"=",num1**num2)
    
    else:
        print("Hesap Makinemizde Böyle Bir İslem Gecersizdir!!!")
    break

