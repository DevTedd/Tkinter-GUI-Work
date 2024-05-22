import tkinter#importing the library  
from tkinter import ttk   #Along with supporting libs


window = tkinter.Tk()#creating an instance of the class

#Adding a title section
window.title("LC Calculation General Busines?")
#The above only generates the title of the window along with the instance of tkinter
#We need a section to draw/add our widgets too

#Adding a frame to the window(THE FRAME IS INSIDE THE WINDOW)
frame = tkinter.Frame(window)#cREATING THE WIDGET
frame.pack()#Allows us to draw the widget

#The process is create the instnace then add it into the window

#We will add 3 frames into the window, to seprate the different sections of our GUI
#The first one will be regarding taking in user/file path info
user_info_frame = tkinter.LabelFrame(frame, text="User Information")
user_info_frame.grid(row=0, column=0, padx=20, pady=20)
#We are creating our first widget
first_name_label = tkinter.Label(user_info_frame, text="First Name:")
first_name_label.grid(row=0, column=0, padx=5, pady=5)
#Creating a similar widget, now for the second section of user input 
last_name_label = tkinter.Label(user_info_frame, text="Last Name:")
last_name_label.grid(row=1, column=0, padx=5, pady=5)

#Lets create s widget for user input
first_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=0, column=1, padx=5, pady=5)
last_name_entry = tkinter.Entry(user_info_frame)
last_name_entry.grid(row=1, column=1, padx=5, pady=5)


#Next is the GUI title, first we create an instnace then add it to the grid
title_label = tkinter.Label(user_info_frame, text="LC Calculation General Business")
title_combobox = ttk.Combobox(user_info_frame, values=["Fire","Motor","Eng", "Marine", "Misc", "Personal Accident", "General Business"])
title_label.grid(row = 2, column=0, padx=10,pady=10)
title_combobox.grid(row=2, column=2, padx=10, pady=10)

#Creating an integer entry box and stuff
age_label = tkinter.Label(user_info_frame, text="Your Age is?")
age_label.grid(row=3, column=0, padx=5, pady=5)
# age_entry = ttk.Combobox(user_info_frame, values=["0-10", "11-20", "21-30", "31-40", "41-50", "51-60", "61-70", "71-80", "81-90", "91-100"])
# age_entry.grid(row=3, column=1, padx=5, pady=5)
#We can also use a spinbox
age_spinbox = tkinter.Spinbox(user_info_frame, from_=18, to=99)
age_spinbox.grid(row=3, column=1, padx=5, pady=5)

#And for another combobox example well just plug in best month
best_month_label = tkinter.Label(user_info_frame, text="What is your Best Month?")
best_month_label.grid(row=4, column=0, padx=5, pady=5)
best_month_combo = ttk.Combobox(user_info_frame, values=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
best_month_combo.grid(row=4, column=2, padx=5, pady=5)


#If we need to change the padding accross the board for a specific frame, in this instance its the user info one
for child in user_info_frame.winfo_children():
    child.grid_configure(padx=10, pady=10) 

    #but for our use case
    #file_paths_frame = tkinter.LabelFrame(frame, text="File Sources and Destination")
    #file_paths_frame.grid(row=0, column=0, padx=5, pady=5)




window.mainloop()#Main loop that continously runs and sustain the window