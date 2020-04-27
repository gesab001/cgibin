import subprocess
from datetime import date
from datetime import datetime



# datetime object containing current date and time
now = datetime.now()
 
#print("now =", now)

# dd/mm/YY H:M:S
#time_string = now.strftime("%H:%M:%S")
#print("date and time =", dt_string)	
date_string = now.strftime("%A, %B %d %Y %r")
print(date_string)
#date=str(date_string)
#day, month, year = date.split(' ')     
#day_name = datetime.date(int(year), int(month), int(day)) 
#print(day_name.strftime("%A")) 

#today = date.today()
# Textual month, day and year	
#d2 = today.strftime("%B %d, %Y")
#print("d2 =", d2)

command = "echo " + str(date_string) + " NZ" + " >../html/headlines/lastNewsUpdate.txt"
subprocess.call(command, shell=True) 


