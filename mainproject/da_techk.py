from datetime import datetime
current_year = datetime.today().year
def date_ver(dd,mm,yy):
    if type(dd)==str or type(mm) == str or type(yy) == str or yy<1900 or yy>=current_year:
        return -1

    if(mm==1 or mm==3 or mm==5 or mm==7 or mm==8 or mm==10 or mm==12):
        max1=31
    elif(mm==4 or mm==6 or mm==9 or mm==11):
        max1=30
    elif(yy%4==0 and yy%100!=0 or yy%400==0):
        max1=29
    else:
        max1=28
    if(mm<1 or mm>12):
        # print("Date is invalid.")
        return -1
    elif(dd<1 or dd>max1):
        return -1
    else:
        return 0

# x = date_ver(29,2,1900)
# print(x)
