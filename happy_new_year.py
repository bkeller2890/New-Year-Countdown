#Happy New Year (any new year)
#Benjamin A. Keller 
#1/2/2023
import time 

print()
def new_year_countdown(x):
        year = 2023 # new year variable 
        while x: 
                seconds = x
                countdown = "{:2d}".format(seconds)
                print(countdown, end="\r")
                time.sleep(1)
                x -= 1
        print(f"\nHappy New Year {year}!!!!!!\n") 
        

new_year_countdown(10) #countdown set


  