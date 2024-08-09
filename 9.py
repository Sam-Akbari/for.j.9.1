def lozy(n):#تابع
    for i in range(n):#حلقه 
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))#نمایش لوزی
    for i in range(n, -1, -1):#حلقه
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))#برای نمایش دیگری لوزی

# دریافت ورودی از کاربر
n = int(input("Enter a number: "))
lozy(n)#اجرا تابع

#پایان
