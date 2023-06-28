### Importing the required libraries

import os
from datetime import datetime
import sys
import time



### Get the File Path From Command-line Arguments
if len(sys.argv) > 1:
    file_path = sys.argv[1]
else:
    print("Provide the file path as terminal argument for storing data.")
    sys.exit(1)



### 'arp' Command Execution For Getting ARP Table
def arp_table():
    arp_command_output = os.popen('arp').read()
    return arp_command_output



### Create Report of Findings
def txt_report(old_table, new_table):
    # Getting Time
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    # Appending Output To File 
    with open(file_path, 'a') as file:
        file.write('--------------------------------'+'ARP table changed! -> Time: '+dt_string+'--------------------------------'+'\n')
        file.write('Previous ARP table: '+'\n')
        file.write(old_table+'\n')
        file.write('---------------------------------------------------------------------------------------------------------------'+'\n')
        file.write('Current ARP table: '+'\n')
        file.write(new_table+'\n')        
        file.write('---------------------------------------------------------------------------------------------------------------'+'\n')
    print("ARP output has been appended to the "+file_path+" file.")



### ARP Table Comparison
def comparison(old_table, new_table):
    if old_table != new_table:
    
        # Calling Function For Report Creation
        txt_report(old_table, new_table) 

        # Print Results On Linux Terminal  
        terminal_print(old_table, new_table)
        


### This is a function for printing on Linux Terminal whatever arp table change takes place 
def terminal_print(old_table, new_table):
    # ARP Change Print On Terminal  
    print("ARP table has changed!")
    print("Previous ARP table:")
    print(old_table)
    print("Current ARP table:")
    print(new_table)
    print("---------------------")



### ARP table check
def arp_change_check_loop():
    previous_table = arp_table()
    # Forever Loop 
    while True:
        time.sleep(10)  # Wait for 10 seconds
        current_table = arp_table()
        comparison(previous_table, current_table)
        previous_table = current_table



### Main 
if __name__ == "__main__":
    arp_change_check_loop()