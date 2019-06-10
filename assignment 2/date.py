def date_check(listOfDate):
    if(len(listOfDate[0])==2 and len(listOfDate[2] == 4)):
        year(int(listOfDate[2]))
        if(int(listOfDate[0]) >= 01 and int(listOfDate[0]) <= 12):
            month(int(listOfDate), listOfDate(1))
        elif : day(int(listOfDate[0]))
        else : return ("wrong format")
        
            
    else:
        return ("wrong format")
def month(noOfMonth, days):
    if(noOfMonth == 02 and feb(int(days))):
        return True
    elif(noOfMonth == 01 or noOfMonth == 03 or noOfMonth == 05 or noOfMonth == 07 or noOfMonth == 08 or noOfMonth == 10 or noOfMonth == 12):
        return (day31(int(days)))
    elif(noOfMonth == 04 or noOfMonth == 06 or noOfMonth == 09 or noOfMonth == 11):
        return (day30(int(days)))
    else: return False
          
def feb(days):
    if (days >= 01 and days <=29):
        return True
    else:
        return False
def day30(days):
    if(days >= 01 and days <= 30):
        return True
    else:
        return False
        

def day31(days):
    if (days >= 01 and days <= 31):
        return True
    else:
        return False

def day(day):
    n_th_day = int(day[0])
    if (n_th_day >= 01 and n_th_day <=31):
        return True
    else:
        return False
def year(years,days):
    if (year % 4 == 0):
       return if feb(days)
    else:
        return False
        
    

date = input()
list_date = date.split("/")
print(date_check(list_date))
