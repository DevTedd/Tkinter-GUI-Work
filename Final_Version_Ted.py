import tkinter#importing the library  
from tkinter import * 
from tkinter import filedialog ,messagebox
import pandas as pd
from tkinter import Listbox


window = tkinter.Tk()

# Variables to hold the file paths
transactional_file_path = tkinter.StringVar()
actuarial_file_path = tkinter.StringVar()
# Variables to track checkbox states
final_check_var = tkinter.BooleanVar()
final_check_tick_var = tkinter.BooleanVar()
quarter_check_var = tkinter.BooleanVar()



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
    if final_check_var.get() and final_check_tick_var.get() and quarter_check_var.get():
        button.config(state=tkinter.NORMAL)
    else:
        button.config(state=tkinter.DISABLED)
        


        
# Function to trigger the script to run LC calculations
def run_calculations():
    
    if final_check_var.get() and final_check_tick_var.get() and quarter_check_var.get():
        # Placeholder for the actual LC calculations, would now call in the script pass on the file paths, blah blah 
        messagebox.showinfo("Success", "Running LC Calculations...")
    else:
        messagebox.showerror("Error", "Both conditions must be checked to run LC Calculations.")
        
# Function to select output file location
def select_output_file():
    output_path = filedialog.asksaveasfilename(
        title="Select Output File",
        filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
    )
    if output_path:
        output_file_var.set(output_path)

# Function to get selected quarter and perform an action
def get_selected_quarter():
    selected_quarter = quater_option.get(quater_option.curselection())
    print("Selected Quarter:", selected_quarter)  # Replace this with the actual action you want to perform
    quarter_check_var.set(True)  # Set the checkbox to checked state
    update_button_state()  # Update the button state 


window.title("LC Calculation General Business")
frame = tkinter.Frame(window)#cREATING THE WIDGET
frame.pack()


# Going into the second frame
file_paths_frame = tkinter.LabelFrame(frame, text="Source and Destination File Path Names")
file_paths_frame.grid(row=0, column=0, sticky="news")

# Button to open transactional file dialog
transactional_file_button = tkinter.Button(file_paths_frame, text="Select Transactional File", command=get_transactional_file,bg='purple', fg='white')
transactional_file_button.grid(row=4, column=0)

# Label to show the selected transactional file path
transactional_file_label = tkinter.Label(file_paths_frame, textvariable=transactional_file_path)
transactional_file_label.grid(row=5, column=0, columnspan=2)

# Button to open actuarial file dialog
actuarial_file_button = tkinter.Button(file_paths_frame, text="Select Actuarial File", command=get_actuarial_file,bg='blue', fg='white')
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

final_check = tkinter.Checkbutton(run_section, text="Checked risk adjustment values before running LC Calculations",variable=final_check_var, command=update_button_state)
final_check.grid(row=1, column=0)
final_check_tick = tkinter.Checkbutton(run_section, text="Checked file paths",variable=final_check_tick_var, command=update_button_state)
final_check_tick.grid(row=2, column=0)

# Creating a button, in this version we add a function to the button
button = tkinter.Button(run_section, text="Run LC Calculations", command=run_calculations, state=tkinter.DISABLED,bg='red', fg='white')
button.grid(row=2, column=1)

# Add the new checkbox for confirming quarter selection
quarter_check = tkinter.Checkbutton(run_section, text="Confirmed quarter selection", variable=quarter_check_var, command=update_button_state)
quarter_check.grid(row=3, column=0)


for child in run_section.winfo_children():
    child.grid_configure(padx=20, pady=20) 
 
 ####################################################################################################################################   
    
#Frame to modify the risk adjustment figures 

risk_adjustment_frame = tkinter.LabelFrame(frame, text="Update Risk Adjustment Figures (Optional)")
risk_adjustment_frame.grid(row=1, column=0,sticky="news")

# List of line of business names
variable_names = ["Engineering", "Fire", "Liability","Marine","Medical","Miscellaneous","Motor","Personal Accident","Theft","Workmens Compensation"]
variable_entries = {}

def get_variable_values():
    variable_values = {}
    for var_name, entry in variable_entries.items():
        variable_values[var_name] = entry.get()
    print("Variable values:", variable_values)  # Placeholder for further processing, this will be used to update the figures in the script
    final_check_var.set(True)
    return variable_values

# Create entry widgets for each variable
for i, var_name in enumerate(variable_names):
    tkinter.Label(risk_adjustment_frame, text=var_name).grid(row=i, column=0, padx=5, pady=5)
    entry = tkinter.Entry(risk_adjustment_frame)
    entry.grid(row=i, column=1, padx=5, pady=5)
    variable_entries[var_name] = entry

# Collect variable values button (for demonstration)
collect_button = tkinter.Button(risk_adjustment_frame, text="Collect Variable Values", command=get_variable_values, bg='yellow', fg='black')
collect_button.grid(row=len(variable_names), column=1, pady=10)
 ####################################################################################################################################   

#Creating an output section

output_section = tkinter.LabelFrame(frame, text="Output Section")
output_section.grid(row=1, column=1,sticky="news")

# Output file path selection
output_file_var = tkinter.StringVar()
output_file_button = tkinter.Button(output_section, text="Select Output File Location", command=select_output_file, bg='green', fg='white')
output_file_button.grid(row=4, column=0, padx=5, pady=5)
output_file_display = tkinter.Entry(output_section, textvariable=output_file_var, state='readonly')
output_file_display.grid(row=4, column=1, padx=5, pady=5)

# Loss component display section 
loss_component_label = tkinter.Label(output_section, text="Loss Component:")
loss_component_label.grid(row=5, column=0, padx=5, pady=5)
loss_component = tkinter.DoubleVar()
loss_component_display = tkinter.Label(output_section, textvariable=loss_component)
loss_component_display.grid(row=5, column=1, padx=5, pady=5)

#The date selecting calendar 
quater_select = tkinter.Button(output_section, text="Select Quarter", command=get_selected_quarter, bg='orange', fg='white')
quater_select.grid(row=2, column=0, padx=5, pady=20)

quater_option = Listbox(output_section, width=10, height=6)
quater_option.insert(1, "2022 Q1")
quater_option.insert(2, "2022 Q2")
quater_option.insert(3, "2022 Q3")
quater_option.insert(4, "2022 Q4")
quater_option.insert(5, "2023 Q1")
quater_option.insert(6, "2023 Q2")
quater_option.insert(7, "2023 Q3")
quater_option.insert(8, "2023 Q4")
quater_option.insert(9, "2024 Q1")
quater_option.insert(10, "2024 Q2")
quater_option.insert(11, "2024 Q3")
quater_option.insert(12, "2024 Q4")
quater_option.grid(row=2, column=1, padx=5, pady=20)

# year = tkinter.Spinbox(run_section, from_=2000, to=2030, width=5)
# year.grid(row=3, column=2)

 
 
window.mainloop()
