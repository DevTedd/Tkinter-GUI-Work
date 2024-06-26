import tkinter#importing the library  
from tkinter import ttk 
from tkinter import filedialog ,messagebox
import subprocess 
import pandas as pd


window = tkinter.Tk()

# Variables to hold the file paths
transactional_file_path = tkinter.StringVar()
actuarial_file_path = tkinter.StringVar()
# Variables to track checkbox states
final_check_var = tkinter.BooleanVar()
final_check_tick_var = tkinter.BooleanVar()

def get_transactional_file():
    """Opens a file dialog for selecting the transactional file and returns the path.

    Returns:
        str: The path of the selected transactional file, or None if no file is selected.
    """
    filename = filedialog.askopenfilename(
        title="Select the current Transactional File",
        filetypes=[("Excel files", "*.xlsx *.xlsm")],
    )
    return filename


def get_actuarial_file():
    """Opens a file dialog for selecting the actuarial file and returns the path.

    Returns:
        str: The path of the selected actuarial file, or None if no file is selected.
    """
    filename = filedialog.askopenfilename(
        title="Select the current Actuarial File",
        filetypes=[("Excel files", "*.xlsx *.xlsm")],
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

# Function to update button state, to ensure that the user has loaded the correct files 
def update_button_state():
    if final_check_var.get() and final_check_tick_var.get():
        button.config(state=tkinter.NORMAL)
    else:
        button.config(state=tkinter.DISABLED)
        
# Function to trigger the script to run LC calculations
def run_calculations():
    if final_check_var.get() and final_check_tick_var.get():
        # Placeholder for the actual LC calculations, would now call in the script pass on the file paths, blah blah 
        messagebox.showinfo("Success", "Running LC Calculations...")
    else:
        messagebox.showerror("Error", "Both conditions must be checked to run LC Calculations.")



window.title("LC Calculation General Business")
frame = tkinter.Frame(window)#cREATING THE WIDGET
frame.pack()


# Going into the second frame
file_paths_frame = tkinter.LabelFrame(frame, text="Source and Destination File Path Names")
file_paths_frame.grid(row=0, column=0, sticky="news")

# Button to open transactional file dialog
transactional_file_button = tkinter.Button(file_paths_frame, text="Select Transactional File", command=get_transactional_file)
transactional_file_button.grid(row=4, column=0)

# Label to show the selected transactional file path
transactional_file_label = tkinter.Label(file_paths_frame, textvariable=transactional_file_path)
transactional_file_label.grid(row=5, column=0, columnspan=2)

# Button to open actuarial file dialog
actuarial_file_button = tkinter.Button(file_paths_frame, text="Select Actuarial File", command=get_actuarial_file)
actuarial_file_button.grid(row=4, column=1)

# Label to show the selected actuarial file path
actuarial_file_label = tkinter.Label(file_paths_frame, textvariable=actuarial_file_path)
actuarial_file_label.grid(row=7, column=0, columnspan=2)

for child in file_paths_frame.winfo_children():
    child.grid_configure(padx=20, pady=20)

#######################################################################################################################################################

# Downwards we are adding our 2nd label frame
run_section = tkinter.LabelFrame(frame, text="Run the LC Calculation")
run_section.grid(row=0, column=1,sticky="news")

final_check = tkinter.Checkbutton(run_section, text="Check conditions before running LC Calculations",variable=final_check_var, command=update_button_state)
final_check.grid(row=1, column=0)
final_check_tick = tkinter.Checkbutton(run_section, text="Checked file paths",variable=final_check_tick_var, command=update_button_state)
final_check_tick.grid(row=1, column=1)

# Creating a button, in this version we add a function to the button
button = tkinter.Button(run_section, text="Run LC Calculations", command=run_calculations, state=tkinter.DISABLED)
button.grid(row=2, column=1)

for child in run_section.winfo_children():
    child.grid_configure(padx=20, pady=20) 
 
 ####################################################################################################################################   
    
#Frame to modify the risk adjustment figures 

risk_adjustment_frame = tkinter.LabelFrame(frame, text="Current Risk Adjustment Figures")
risk_adjustment_frame.grid(row=1, column=0,sticky="news")

window.mainloop()
