import tkinter 
from tkinter import messagebox, filedialog
from datetime import datetime

# Create the main window
window = tkinter.Tk()
window.title("LC Calculation General Business?")

# Create the main frame
frame = tkinter.Frame(window)
frame.pack()

# Function to update button state
def update_button_state():
    if final_check_var.get() and final_check_tick_var.get() and date_var.get():
        button.config(state=tkinter.NORMAL, bg='green', fg='white')
    else:
        button.config(state=tkinter.DISABLED, bg='red', fg='black')

# Function to run LC calculations
def run_calculations():
    if final_check_var.get() and final_check_tick_var.get() and date_var.get():
        # Placeholder for the actual LC calculations
        loss_component.set(123.45)  # Example value for the loss component
        messagebox.showinfo("Success", "Running LC Calculations...")
    else:
        messagebox.showerror("Error", "All conditions must be met to run LC Calculations.")

# Function to select output file location
def select_output_file():
    output_path = filedialog.asksaveasfilename(
        title="Select Output File",
        filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
    )
    if output_path:
        output_file_var.set(output_path)

# Add the second label frame
run_section = tkinter.LabelFrame(frame, text="Run the LC Calculation")
run_section.grid(row=0, column=1, sticky="news")

# Variables to track checkbox states
final_check_var = tkinter.BooleanVar()
final_check_tick_var = tkinter.BooleanVar()

# Creating checkbuttons
final_check = tkinter.Checkbutton(run_section, text="Check conditions before running LC Calculations",
                             variable=final_check_var, command=update_button_state)
final_check.grid(row=1, column=0)

final_check_tick = tkinter.Checkbutton(run_section, text="Checked file paths",
                                  variable=final_check_tick_var, command=update_button_state)
final_check_tick.grid(row=1, column=1)

# Creating the button
button = tkinter.Button(run_section, text="Run LC Calculations", command=run_calculations, state=tkinter.DISABLED,
                   bg='red', fg='black')
button.grid(row=2, column=1)

# Add a label frame for modifiable variables
variables_section = tkinter.LabelFrame(frame, text="Modifiable Variables")
variables_section.grid(row=1, column=1, sticky="news")

# List of variable names
variable_names = ["Variable 1", "Variable 2", "Variable 3"]
variable_entries = {}

# Function to collect variable values
def get_variable_values():
    variable_values = {}
    for var_name, entry in variable_entries.items():
        variable_values[var_name] = entry.get()
    print("Variable values:", variable_values)  # Placeholder for further processing
    return variable_values

# Create entry widgets for each variable
for i, var_name in enumerate(variable_names):
    tkinter.Label(variables_section, text=var_name).grid(row=i, column=0, padx=5, pady=5)
    entry = tkinter.Entry(variables_section)
    entry.grid(row=i, column=1, padx=5, pady=5)
    variable_entries[var_name] = entry

# Collect variable values button (for demonstration)
collect_button = tkinter.Button(variables_section, text="Collect Variable Values", command=get_variable_values,
                           bg='blue', fg='white')
collect_button.grid(row=len(variable_names), column=1, pady=10)

# Add a label frame for output
output_section = tkinter.LabelFrame(frame, text="Output")
output_section.grid(row=2, column=1, sticky="news")

# Loss component display
loss_component_label = tkinter.Label(output_section, text="Loss Component:")
loss_component_label.grid(row=0, column=0, padx=5, pady=5)
loss_component = tkinter.DoubleVar()
loss_component_display = tkinter.Label(output_section, textvariable=loss_component)
loss_component_display.grid(row=0, column=1, padx=5, pady=5)

# Output file selection
output_file_var = tkinter.StringVar()
output_file_button = tkinter.Button(output_section, text="Select Output File Location", command=select_output_file,
                               bg='purple', fg='white')
output_file_button.grid(row=1, column=0, padx=5, pady=5)
output_file_display = tkinter.Entry(output_section, textvariable=output_file_var, state='readonly')
output_file_display.grid(row=1, column=1, padx=5, pady=5)

# Add a label frame for date selection
date_frame = tkinter.LabelFrame(frame, text="Select Date")
date_frame.grid(row=0, column=0, sticky="news", padx=10, pady=10)

# Create a string variable to store selected date
date_var = tkinter.StringVar()

# Function to update date variable
def update_date(*args):
    date_var.set(date_combobox.get())

# Create a combobox for date selection
date_combobox = tkinter.Combobox(date_frame, textvariable=date_var, state="readonly")
date_combobox["values"] = [""]  # Initialize with empty string
date_combobox.grid(row=0, column=0)
