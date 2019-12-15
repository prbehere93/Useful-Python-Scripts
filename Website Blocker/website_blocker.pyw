import time
from datetime import datetime as dt

temp_path='hosts'
path=r'C:\Windows\System32\drivers\etc\hosts' #path of hosts file
redirect='127.0.0.1'
website_list=["www.facebook.com","facebook.com"]

while True: #Infinite loop
    #the if statement checks if the time now is between 10 am and 8 p.m. 
    if dt(dt.now().year,dt.now().month,dt.now().day,10)< dt.now() < dt(
        dt.now().year,dt.now().month,dt.now().day,19):
        print('m')
        with open(path,'r+') as file: 
            content=file.read() #reading the host file
            for i in website_list: #check if website already present
                if i in content:
                    pass
                else:
                    file.write(redirect+" "+i+'\n')
    else:
        with open(path,'r+') as file: 
            content=file.readlines() #reading the host file line by line
            file.seek(0) #Replace the cursor at the beginning (the cursor will have reached the end after using readlines())

            for line in content: #Iterating through each line
                
                #checking if there is any of our websites in the line (if not then write the line in the file)
                if not any(website in line for website in website_list): 
                    file.write(line)
                file.truncate() #not sure that we need this    

        print('nope')
    time.sleep(5)
