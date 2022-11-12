    # Fitness Trainer nd Nutritionist
# Harry Rohan and Karan 
# 3 files for Exce , 3 for Nutrition 
# A func , which takes Client Name as input and that writes their data
# and can read according to user input

# Prints current date and time
def getdate():
    import datetime
    return datetime.datetime.now()
client_name = input("Enter the name of client ")
client_file = client_name.title() + ".txt"

open_client_file = open(client_file,"a+")

client_Activity = input("What Do you want to access  client's Diet or Fitness .Press 1 for Diet and 2 for Fitness  ")



if int(client_Activity) == 1:
    personalized_file = client_name.title() + "Diet.txt"
    
elif int(client_Activity) == 2:
    personalized_file = client_name.title() + "Fitness.txt"
    
Data_read_or_entry = input("Do you want to read the client's Data or Mark a entry . Press 1 for Reading the Data and 2 for making a entry \n")    


# def Add_Entry(file_client,client_info):
    
#     """ It adds client Activities in the log"""
#     write_entry = file_client.write(client_info)
#     # print(getdate())   
#     return write_entry   

# def Read_File(file_client):
#     """To read user's data stored in the file"""
#     read_client_data = file_client.read()
#      return read_client_data

if(int(Data_read_or_entry) == 1):
    file_client = open(personalized_file,"r")
    Read_file = file_client.read()
    print(Read_file)
    


if(int(Data_read_or_entry) == 2):
    file_client = open(personalized_file,"a+")
    
    client_info = input("Enter the client's activity ")
    Add_Entry = file_client.write(client_info)
    gap_between_entry_and_time = file_client.write(" on ")

    Add_Time = file_client.write(str(getdate()))
    New_Line = file_client.write('\n')
    
    print("Entry successfully registered")


    