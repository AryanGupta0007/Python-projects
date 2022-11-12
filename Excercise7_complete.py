
# Healthy Programmer
# Every 30 min do a Walk # Remainder (Play some music (mp3))
# Every 45 Min do a Excercise #Remainder (Play some music (.mp3))
# 3.5 L Water (15-18 glasses of water)(9 Am - 5Pm) #Remainder (Play some music(mp3))
# input("Done"# To stop the music)
# log into a Daily Activity journal  
# 8 hours , every 35 min (16)





import datetime
from datetime import date, timedelta # to make gap between time (new)
from pygame import mixer # To play music in python (new)
import time

# strr = datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day, datetime.datetime.now().hour, datetime.datetime.now().minute)
# print(strr)

Current_time = datetime.datetime.now().strftime("%Y%m%d %H:%M:%S") # gives current date and time
# print(Current_time)
# if(Current_time < today9am or Current_time > today5pm):

# def clock():
#     while True:
#        print(datetime.datetime.now().strftime("%H:%M:%S"), end="\r")
Current_time = datetime.datetime.strptime(Current_time, "%Y%m%d %H:%M:%S")
# print(Current_time)
       

thirty_min_gap = datetime.timedelta(minutes=30) # 30 min 
thirty_five_min_gap = datetime.timedelta(minutes=35) # 35 min 
forty_five_min_gap = datetime.timedelta(minutes=45) # 45 min 

today9am = Current_time.replace(hour = 9,minute = 0 , second = 00)
result = today9am
today5pm = Current_time.replace(hour = 17,minute=0 , second = 00)
# testtime = Current_time.replace(hour = 23,minute=30 , second = 45)

time_30 = list() 
# while(result < today5pm):
#    result += thirty_min_gap
#    time_30.append(result)
while(result < today5pm):
    result += thirty_min_gap
    time_30.append(result)
# time_30.append(testtime)
time_35 = list()
today9_35am = Current_time.replace(hour = 9,minute = 35)
result_35 = today9_35am
while(result_35 < today5pm):
    result_35 += thirty_min_gap
    time_35.append(result_35)

today9_45am = Current_time.replace(hour = 9,minute = 45)
result_45 = today9_45am
time_45 = list()
while(result_45 < today5pm):
    result_45 +=  forty_five_min_gap
    time_45.append(result_45)

while True:
    while(Current_time not in time_30 and Current_time not in time_35 and Current_time not in time_45):
        Current_time = datetime.datetime.now().strftime("%Y%m%d %H:%M:%S")
        Current_time = datetime.datetime.strptime(Current_time, "%Y%m%d %H:%M:%S")
        print(Current_time,end="\r") #end="\r" new Concept

    while(Current_time  in time_30 or Current_time  in time_35 or Current_time  in time_45):
        

        mixer.init()

        if(Current_time in time_30):
            mixer.music.load(r"C:\Users\panka\Desktop\KIDS\Aryan\Python\Take_a_Walk_(getmp3.pro).mp3")
            """with r print function accepts the string as it as means it doesn't
            require any escape sequence"""
            mixer.music.play()
            user_name = input("Enter client name ")
            user__name = user_name.title() #Capitalizes the first letter and makes all the other charac small
            client_file = (user__name +".txt")
            ClientFile = open(client_file,"a+")

            

            user_Walk = input("Do a  walk for 5  min . Type done after you"
            " have completed the task to stop the music ")
            user_Walk = user_Walk.title()
        
            if(user_Walk == "Done"):
                
                mixer.music.stop()
                ClientFile.write("\nWalk completed at "+ str(Current_time))
                ClientFile.close()
                Current_time = datetime.datetime.now().strftime("%Y%m%d %H:%M:%S")
                Current_time = datetime.datetime.strptime(Current_time, "%Y%m%d %H:%M:%S")
        
        
        
        elif(Current_time in time_35):
            mixer.music.load(r"C:\Users\panka\Desktop\KIDS\Aryan\Python\Jai.mp3")
            mixer.music.play()
            user_name = input("Enter client name ")
            user__name = user_name.title() #Capitalizes the first letter and makes all the other charac small
            client_file = (user__name +".txt")
            ClientFile = open(client_file,"a+")


            user_Water = input("Drink a glass of water. Type done after " 
            "you have completed the task to stop the music ")
            user_Water = user_Water.title()
        
            if(user_Water == "Done"):
                mixer.music.stop()
                ClientFile.write("\nWater drunk at "+ str(Current_time))
                ClientFile.close()
                Current_time = datetime.datetime.now().strftime("%Y%m%d %H:%M:%S")
                Current_time = datetime.datetime.strptime(Current_time, "%Y%m%d %H:%M:%S")
        
        
        
        
        elif(Current_time in time_45):
            mixer.music.load(r"C:\Users\panka\Desktop\KIDS\Aryan\Python\Cartoon.mp3")
            mixer.music.play()
            user_name = input("Enter client name ")
            user__name = user_name.title() #Capitalizes the first letter and makes all the other charac small
            client_file = (user__name +".txt")
            ClientFile = open(client_file,"a+")



            user_WorkOut = input("Do a little Excercise  . Type done"
            " after you have completed the task to stop the music ")
            user_WorkOut = user_WorkOut.title()
            if(user_WorkOut == "Done"):
                mixer.music.stop()
                ClientFile.write("\nWorkOut completed at "+ str(Current_time))
                ClientFile.close()
                Current_time = datetime.datetime.now().strftime("%Y%m%d %H:%M:%S")
                Current_time = datetime.datetime.strptime(Current_time, "%Y%m%d %H:%M:%S")
        