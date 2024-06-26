import tkinter#importing the library  
from tkinter import ttk 

window = tkinter.Tk()

window.title("LC Calculation General Busines?")
frame = tkinter.Frame(window)#cREATING THE WIDGET
frame.pack()

user_info_frame = tkinter.LabelFrame(frame, text="User Information")
user_info_frame.grid(row=0, column=0,sticky="news")
#We are creating our first widget
first_name_label = tkinter.Label(user_info_frame, text="First Name:")
first_name_label.grid(row=0, column=0)
#Creating a similar widget, now for the second section of user input 
last_name_label = tkinter.Label(user_info_frame, text="Last Name:")
last_name_label.grid(row=1, column=0)

#Lets create s widget for user input
first_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=0, column=1)
last_name_entry = tkinter.Entry(user_info_frame)
last_name_entry.grid(row=1, column=1)


#Next is the GUI title, first we create an instnace then add it to the grid
title_label = tkinter.Label(user_info_frame, text="LC Calculation General Business")
title_combobox = ttk.Combobox(user_info_frame, values=["Fire","Motor","Eng", "Marine", "Misc", "Personal Accident", "General Business"])
title_label.grid(row = 2, column=0)
title_combobox.grid(row=2, column=2)

#Creating an integer entry box and stuff
age_label = tkinter.Label(user_info_frame, text="Your Age is?")
age_label.grid(row=3, column=0)
# age_entry = ttk.Combobox(user_info_frame, values=["0-10", "11-20", "21-30", "31-40", "41-50", "51-60", "61-70", "71-80", "81-90", "91-100"])
# age_entry.grid(row=3, column=1)
#We can also use a spinbox
age_spinbox = tkinter.Spinbox(user_info_frame, from_=18, to=99)
age_spinbox.grid(row=3, column=1)

#And for another combobox example well just plug in best month
best_month_label = tkinter.Label(user_info_frame, text="What is your Best Month?")
best_month_label.grid(row=4, column=0)
best_month_combo = ttk.Combobox(user_info_frame, values=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
best_month_combo.grid(row=4, column=2)


#If we need to change the padding accross the board for a specific frame, in this instance its the user info one
for child in user_info_frame.winfo_children():
    child.grid_configure(padx=20, pady=20) 


#Going into the second frame
file_paths_frame = tkinter.LabelFrame(frame, text="Source and Destination FilePath Names")
file_paths_frame.grid(row=1, column=0, sticky="news")

#ACT Input file
actInput_file_label = tkinter.Label(file_paths_frame, text="ACT Input File Path ->  ")
actInput_file_check = tkinter.Checkbutton(file_paths_frame, text="Check to include ACT Input File")
actInput_file_label.grid(row=0, column=0)
actInput_file_check.grid(row=1, column=0)

#Lets add a random spinbox
numberofFiles_label = tkinter.Label(file_paths_frame, text="Number of Files to be Processed ->  ")
numberofFiles_spinbox = tkinter.Spinbox(file_paths_frame, from_=1, to=4)
numberofFiles_label.grid(row=2, column=0)
numberofFiles_spinbox.grid(row=2, column=1)

#and a second one
outputs_label = tkinter.Label(file_paths_frame, text="Output file version is ->  ")
outputs_spinbox = tkinter.Spinbox(file_paths_frame, from_=1, to=10)
outputs_label.grid(row=3, column=0)
outputs_spinbox.grid(row=3, column=1)



for child in file_paths_frame.winfo_children():
    child.grid_configure(padx=20, pady=20) 
    
    
    
    
#Downwards we are adding our 3rd label frame

 
run_section = tkinter.LabelFrame(frame, text="Run the LC Calculation")
run_section.grid(row=0, column=1,sticky="news")

final_check = tkinter.Checkbutton(run_section, text="Check conditions before running LC Calculations")
final_check.grid(row=1, column=0)
final_check_tick = tkinter.Checkbutton(run_section, text="Checked file paths")
final_check_tick.grid(row=1, column=1)

#Creating a button
button = tkinter.Button(run_section, text="Run LC Calculations")
button.grid(row=2, column=1)

for child in run_section.winfo_children():
    child.grid_configure(padx=20, pady=20) 

window.mainloop()