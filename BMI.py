from matplotlib import pyplot as myplot
import pyttsx3
import os
#................................
os.system('cls' or 'clear')
class color : 
    GREEN = '\033[92m'
    RED = '\033[91m'
    WHITE = '\033[0m' 
#.................................
engine = pyttsx3.init() 
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-60)
#.................................................
try:   
    weight = int(input("please enter your weight whit kg  : "))
    height = int(input("please enter your height whit centimeter  : "))
    age = int(input("your age  : "))
    bmi = round(weight / ((height / 100)*(height / 100)) , 1)
    if height > 220 or height < 70:
        print("your height isnt natural but you can see in the chart")
        engine.say("your height isnt natural but you can see in the chart")
        engine.runAndWait()
    if age > 120 :
        print("your age isnt natural but you can see in the chart")
        engine.say("your age isnt natural but you can see in the chart")
        engine.runAndWait()
    if weight > 200 or weight < 20 :
        print("your weight isnt natural but you can see in the chart")
        engine.say("your weight isnt natural but you can see in the chart")
        engine.runAndWait()
#..................................................
    if bmi < 18.5 or bmi == 18.5 : 
        print("you BMI is : " , (color.RED + str(bmi)))
        if age < 17:
            print("BMI test is not for children under 17 year but its veary low")
            engine.say("BMI test is not for children under 17 year, but its veary low. you can see in the chart.")
        else:
            print(color.WHITE + "your bmi for your age(" + "\033[1m" + color.RED + str(age) + "\033[0m" + ") is veary low")
            engine.say("your bmi for your age(" + str(age) + ") is veary low. you can see in the chart.")
        engine.runAndWait() 



#.....................................................
    if bmi > 18.5 and bmi < 24.9 or bmi == 24.9:
        print("you BMI is : " , (color.RED + str(bmi)))
        if age < 17:
            print(color.WHITE + "BMI test is not for children under 17 year but its good")
            engine.say("BMI test is not for children under 17 year, but its good. you can see in the chart.")
        if age == 17 or age == 24 or age > 17 and age < 24 :
            if bmi == 20 or bmi == 22 or bmi > 20 and bmi < 22:
                print(color.WHITE + "your bmi for your age(" + "\033[1m" + color.RED + str(age) + "\033[0m" + ") is veary good")
                engine.say("your bmi for your age(" + str(age) + ") is veary good. you can see in the chart.")
            else:
                print(color.WHITE + "your bmi for your age(" + "\033[1m" + color.RED + str(age) + "\033[0m" + ") is good not veary good")
                engine.say("your bmi for your age(" + str(age) + ") is good , not veary good. you can see in the chart.")
        if age == 44 or age > 24 and age < 44 :
            if bmi > 22 and bmi < 24 or bmi == 22:
                print(color.WHITE + "your bmi for your age(" + "\033[1m" + color.RED + str(age) + "\033[0m" + ") is veary good")
                engine.say("your bmi for your age(" + str(age) + ") is veary good. you can see in the chart.")
            else:
                print(color.WHITE + "your bmi for your age(" + "\033[1m" + color.RED + str(age) + "\033[0m" + ") is good not veary good")
                engine.say("your bmi for your age(" + str(age) + ") is good , not veary good. you can see in the chart.")
        if age == 54 or age > 44 and age < 54 :
            if bmi > 24 and bmi < 24.9 or bmi == 24:
                print(color.WHITE + "your bmi for your age(" + "\033[1m" + color.RED + str(age) + "\033[0m" + ") is veary good")
                engine.say("your bmi for your age(" + str(age) + ") is veary good. you can see in the chart.")
        else:
            print(color.WHITE + "your bmi for your age(" + "\033[1m" + color.RED + str(age) + "\033[0m" + ") is good not veary good")
        engine.say("your bmi for your age(" + str(age) + ") is good , not veary good. you can see in the chart.")
        engine.runAndWait() 


        
    if bmi > 24.9 and bmi < 30 or bmi == 30:
        print("you BMI is : " , color.RED + bmi)
        if age < 17:
            print(color.WHITE +"BMI test is not for children under 17 year but you have owerweight you must be lower than now")
            engine.say("BMI test is not for children under 17 year, but you have owerweight, you must be lower than now.you can see in the chart")
        if age == 54 or age > 44 and age < 54 :
            if bmi > 24.9 and bmi < 26 or bmi == 24.9:
                print(color.WHITE + "your bmi for your age(" + "\033[1m" + color.RED + str(age) + "\033[0m" + ") is veary good")
                engine.say("your bmi for your age(" + str(age) + ") is veary good. you can see in the chart.")
        if age > 54:
            if bmi > 26 and bmi < 28 or bmi == 28:
                print(color.WHITE + "your bmi for your age(" + "\033[1m" + color.RED + str(age) + "\033[0m" + ") is veary good")
                engine.say("your bmi for your age(" + str(age) + ") is veary good. you can see in the chart.")
        else:
            print("your bmi for your age(" + str(age) + ") is bad ,  you have owerweight, you must be lower than now")
            engine.say("your bmi for your age(" + str(age) + ") is bad ,  you have owerweight, you must be lower than now.you can see in the chart")
        engine.runAndWait() 
#................................................................
    if bmi > 30 and bmi < 35 or bmi == 35:
        print("you BMI is : " , color.RED + bmi)
        if age < 17:
            print(color.WHITE + "BMI test is not for children under 17 year but you have Obesity type 1 and its bad")
            engine.say("BMI test is not for children under 17 year, but you have Obesity type 1 and its bad.you can see in the chart")
        else:
            print(color.WHITE + "your bmi for your age(" + color.RED + str(age) + ") is say us you have Obesity type 1 and its bad")
            engine.say("your bmi for your age(" + str(age) + ") is bad ,  you have Obesity type 1.you can see in the chart")
        engine.runAndWait() 
#............................................................
    if bmi > 35 and bmi < 40 or bmi == 40:
        print("you BMI is : " , color.RED + bmi)
        if age < 17:
            print(color.WHITE + "BMI test is not for children under 17 year but you have Obesity type 2 and its bad")
            engine.say("BMI test is not for children under 17 year, but you have Obesity type 2 and its bad.you can see in the chart")
        else:
            print(color.WHITE + "your bmi for your age(" + color.RED + str(age) + ") is say us you have Obesity type 2 and its bad")
            engine.say("your bmi for your age(" + str(age) + ") is bad ,  you have Obesity type 2.you can see in the chart")
        engine.runAndWait() 
#...............................................................
    if bmi > 40:
        print("you BMI is : " , color.RED + bmi)
        if age < 17:
            print(color.WHITE + "BMI test is not for children under 17 year but you have Obesity type 3 and its bad")
            engine.say("BMI test is not for children under 17 year, but you have Obesity type 3 and its bad.you can see in the chart")
        else:
            print(color.WHITE + "your bmi for your age(" + color.RED + str(age) + ") is say us you have Obesity type 3 and its bad")
            engine.say("your bmi for your age(" + str(age) + ") is bad ,  you have Obesity type 3 , and its so bad.you can see in the chart")
        engine.runAndWait()
#..............................................................



    x = [bmi]
    myplot.plot(x , marker = "." , markersize = 15 , markerfacecolor = "blue")
    myplot.axhspan(0 , 18 , alpha=0.5 , color = "blue")
    myplot.axhspan(18 , 25 , alpha=0.5 , color = "green")
    myplot.axhspan(25 , bmi+20 , alpha=0.5 , color = "red")
    myplot.title("BMI")
    myplot.show()


except ZeroDivisionError:
    print("dont give me zero")
    engine.say("you give me 0 so please dont give me zero. if you want to talk whit\
         me ,  email artinfaghanzadeh@gmail.com. email will be in the box. ") 
except ValueError:
    print("enter only number")
    engine.say("you give me not number. so if you want to work ok , give me number.\
         if you want to talk whit me ,  email artinfaghanzadeh@gmail.com. email will be in the box. ")  
except:
    print("error")
    engine.say("sorry , the program not work good , so please tray again.\
    if you want to talk whit me ,  email artinfaghanzadeh@gmail.com. email will be in the box. ")  

print("if you have any problem email whit me." , color.GREEN + "email : artinfaghanzadeh@gmail.com")

engine.runAndWait() 