def mosallas():#تابع مثلث
    if (a * a) == (b * b) + (c * c):#اگر رابطه فیثاغورث برقرار بود
        print("Yes")#بله را چاپ کن
    else:#در غیر این صورت
        print("No")#نه رو چاپ کن

    return True

a = int(input())#متغیر اول
b = int(input())#متغیر دوم
c = int(input())#متغیر سوم

mosallas()#چاپ

#پایان