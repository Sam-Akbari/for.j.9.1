def separator(ls):#تعریف تابع
    even_numbers = [x for x in ls if x % 2 == 0]#اعدد زوج
    odd_numbers = [x for x in ls if x % 2 != 0]#اعداد فرد
    return (even_numbers, odd_numbers)#برگرداندن اعداد زوج و فرد

# نمونه‌ها
print(separator([-3, -2, -1, 0, 1, 2, 3]))  # ([-2, 0, 2], [-3, -1, 1, 3])
print(separator([1, 11, 5, 7, 3]))          # ([], [1, 11, 5, 7, 3])

#پایان