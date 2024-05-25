import tkinter#importing the library  
from tkinter import ttk 
from tkinter import filedialog
import subprocess 
import pandas as pd


window = tkinter.Tk()

def enter_data():
    print('The data has been succesfully entered, see below ')
    print('First Name: ', first_name_entry.get())
    first = first_name_entry.get()
    print('Last Name: ', last_name_entry.get())
    last = last_name_entry.get()
    print('Age: ', age_spinbox.get())
    age = age_spinbox.get()
    print('Best Month: ', best_month_combo.get())
    month = best_month_combo.get()
    print("Welcome to the Matrix... I know you are ",first," ",last,". You are ",age,"years old and born in ",month)


def get_actuarial_file():
    """Opens a file dialog for selecting the actuarial file and returns the path.

    Returns:
        str: The path of the selected actuarial file, or None if no file is selected.
    """
    filename = filedialog.askopenfilename(
        title="Select Actuarial File",
        filetypes=[("Excel files", "*.xlsx *.xlsm"), ("All files", "*.*")],
    )
    return filename


def read_df(filepath, filetype):
    """Reads a file into a DataFrame based on its filetype.

    Args:
        filepath (str): The path of the file to read.
        filetype (str): The type of the file (e.g., "transactional", "actuarial").

    Returns:
        pandas.DataFrame: The DataFrame created from the file, or None if there's an error.
    """

    if not filepath:
        return None  # Indicate no file selected

    try:
        if filetype == "transactional":
            # Adjust delimiter as needed for your text file
            df = pd.read_csv(filepath, delimiter="\t")
        elif filetype == "actuarial":
            df = pd.read_excel(filepath)
        else:
            print(f"Unsupported file type: {filetype}")
            return None
    except Exception as e:
        print(f"Error reading file: {filepath} - {e}")
        return None

    return df


window.title("LC Calculation General Busines?")
frame = tkinter.Frame(window)#cREATING THE WIDGET
frame.pack()

user_info_frame = tkinter.LabelFrame(frame, text="User Information")
user_info_frame.grid(row=0, column=0,sticky="news")
# We are creating our first widget
first_name_label = tkinter.Label(user_info_frame, text="First Name:")
first_name_label.grid(row=0, column=0)
# Creating a similar widget, now for the second section of user input
last_name_label = tkinter.Label(user_info_frame, text="Last Name:")
last_name_label.grid(row=1, column=0)

# Lets create s widget for user input
first_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=0, column=1)
last_name_entry = tkinter.Entry(user_info_frame)
last_name_entry.grid(row=1, column=1)


# Next is the GUI title, first we create an instance then add it to the grid
title_label = tkinter.Label(user_info_frame, text="LC Calculation General Business")
title_combobox = ttk.Combobox(user_info_frame, values=["Fire","Motor","Eng", "Marine", "Misc", "Personal Accident", "General Business"])
title_label.grid(row = 2, column=0)
title_combobox.grid(row=2, column=2)

# Creating an integer entry box and stuff
age_label = tkinter.Label(user_info_frame, text="Your Age is?")
age_label.grid(row=3, column=0)
# age_entry = ttk.Combobox(user_info_frame, values=["0-10", "11-20", "21-30", "31-40", "41-50", "51-60", "61-70", "71-80", "81-90", "91-100"])
# age_entry.grid(row=3, column=1)
# We can also use a spinbox
age_spinbox = tkinter.Spinbox(user_info_frame, from_=18, to=99)
age_spinbox.grid(row=3, column=1)

# And for another combobox example well just plug in best month
best_month_label = tkinter.Label(user_info_frame, text="What is your Best Month?")
best_month_label.grid(row=4, column=0)
best_month_combo = ttk.Combobox(user_info_frame, values=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
best_month_combo.grid(row=4, column=2)


# If we need to change the padding accross the board for a specific frame, in this instance its the user info one
for child in user_info_frame.winfo_children():
    child.grid_configure(padx=20, pady=20) 


# Going into the second frame
file_paths_frame = tkinter.LabelFrame(frame, text="Source and Destination FilePath Names")
file_paths_frame.grid(row=1, column=0, sticky="news")

# ACT Input file
actInput_file_label = tkinter.Label(file_paths_frame, text="ACT Input File Path ->  ")
actInput_file_check = tkinter.Checkbutton(file_paths_frame, text="Check to include ACT Input File")
actInput_file_label.grid(row=0, column=0)
actInput_file_check.grid(row=1, column=0)

# Lets add a random spinbox
numberofFiles_label = tkinter.Label(file_paths_frame, text="Number of Files to be Processed ->  ")
numberofFiles_spinbox = tkinter.Spinbox(file_paths_frame, from_=1, to=4)
numberofFiles_label.grid(row=2, column=0)
numberofFiles_spinbox.grid(row=2, column=1)

# and a second one
outputs_label = tkinter.Label(file_paths_frame, text="Output file version is ->  ")
outputs_spinbox = tkinter.Spinbox(file_paths_frame, from_=1, to=10)
outputs_label.grid(row=3, column=0)
outputs_spinbox.grid(row=3, column=1)


for child in file_paths_frame.winfo_children():
    child.grid_configure(padx=20, pady=20) 


# Downwards we are adding our 3rd label frame
run_section = tkinter.LabelFrame(frame, text="Run the LC Calculation")
run_section.grid(row=0, column=1,sticky="news")

final_check = tkinter.Checkbutton(run_section, text="Check conditions before running LC Calculations")
final_check.grid(row=1, column=0)
final_check_tick = tkinter.Checkbutton(run_section, text="Checked file paths")
final_check_tick.grid(row=1, column=1)

# Creating a button, in this version we add a function to the button
button = tkinter.Button(run_section, text="Run LC Calculations",command=enter_data)
button.grid(row=2, column=1)

for child in run_section.winfo_children():
    child.grid_configure(padx=20, pady=20) 

window.mainloop()
