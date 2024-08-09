def single_digit(n):
    # اگر عدد تک‌رقمی است، آن را برگردان
    if n < 10:
        return n
    # محاسبه مجموع ارقام عدد
    sum_digits = sum(int(digit) for digit in str(n))
    # فراخوانی بازگشتی تابع برای مجموع ارقام
    return single_digit(sum_digits)

# دریافت ورودی از کاربر
n = int(input("Enter n:"))
print(single_digit(n))

#پایان

