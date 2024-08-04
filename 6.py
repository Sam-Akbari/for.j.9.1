def tas(f):#تابع 
    
    if n == 1:#اگر 1 باشد
        print(6)#6است 
    elif n == 6:#اگر 6 باشد
        print(1)#1 است
    elif n == 2:#اگر 2 باشد
        print(5)#5 است
    elif n == 5:#اگر 5 باشد
        print(2)#2 است
    elif n == 3:#اگر 3 باشد
        print(4)#4 است
    elif n == 4:#اگر 4 باشد
        print(3)#3 است
    else:#در غیر این صورت
        print("you have to enter number 1 to 6!")#این چاپ میشود
    
    
    return n#چاپ عدد کاربر
n = int(input())#عدد را از کاربر میگیرد
print(tas(n))#چاپ تابع

#پایان