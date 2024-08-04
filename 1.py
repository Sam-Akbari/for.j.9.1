
def bealaveh(num1, num2):#تابع اضافه
    return num1 + num2#عدد 1 با عدد 2 جمع میشود

def menha(num1, num2):#تابع منها
    return num1 - num2#عدد1 منها عدد2 میشود

def zarb(num1, num2):#تابع ضرب
    return num1 * num2#عدد1 ضرب عدد2 میشود

def taghsim(num1, num2):#تابع تقسیم
    if num1 != 0:#اگر عدد یک صفر نباشد
        return num1 / num2#عدد1 تقسیم عدد2 میشود
    if num2 != 0:#اگر عدد دو صفر نباشد همچنین
        return num1 / num2#عدد1 تقسیم عدد2 میشود
    else:#در غیر این صورت
        print("0 is false")#این جمله را چاپ میکند

num1 = int(input("Enter your number 1:  "))#عدد 1
num2 = int(input("Enter your number 2:  "))#عدد 2

print("+:", bealaveh(num1, num2))#چاپ جمع انها
print("-:", menha(num1, num2))#چاپ تفریق انها
print("*:", zarb(num1, num2))#چاپ ضرب انها
print("/:", taghsim(num1, num2))#چاپ تقسیم انها

#پایان






