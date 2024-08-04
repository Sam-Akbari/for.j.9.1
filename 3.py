def avalbodan(number):#تابع اول بودن
    if number <= 1:#اگر عدد کوچکتر از 1 باشد خطا وارد میشود
        return False#خطا
    for i in range(2, int(number**0.5) + 1):#حلقه
        if number % i == 0:#اگر عدد یا همون نام متغیرمون باقی مانده بیاره و صفر شه 
            return False#خطا میده
    return True#صدا زدن تابع


inputs = int(input("Enter your number:"))#گرفتن عدد از کاربر
if avalbodan(inputs):#اگر عدد تابع خطا باشد
    print("aval")#اول است
elif inputs == 1:#یا اگر عدد کاربر 1 باشد
    print("one")#یک را چاپ میکند زیرا نه اول است و نه مرکب
else:#در غیر این صورت
    print("morakab")#مرکب است

#پایان

