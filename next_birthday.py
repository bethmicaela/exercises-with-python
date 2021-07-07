from datetime import datetime
from datetime import timedelta

def birthday():
    now = datetime.now()
    # print(now)
    
    new_date = now + timedelta(days=2)
    print(new_date)

    # year =(now) 
    # month = (now.month)
    # day = (now.day)
    # print("{}/{}/{}".format(day, month, year))

    my_birthday = (int(input("Enter your birthday in format --/-/--: ")))
    # print(my_birthday)
  

if __name__ == "__main__":
    birthday()

    
# TERMINAR