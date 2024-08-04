def numbers(num):#تابع عدد ها
    if num < 2:#اگر از 2 کمتر باشد
        return False#غلط را برمیگردانه

    for i in range(2, int(num**0.5)+ 1, 1):#شروع حلقه
        if num % i == 0:#اگر عدد 0 بود
            return False#غلط را برمیگردانه
    return True#این را برای چاپ مینویسیم

def between(a, b):#تابع بین عددی
    for num in range(a, b + 1):#حلقه 
        if numbers(num):
            print(num)

a = int(input())
b = int(input())

between(a, b)

#پایان