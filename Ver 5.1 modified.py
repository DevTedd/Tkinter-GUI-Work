import tkinter as tk
from tkinter import messagebox, filedialog

# Create the main window
window = tk.Tk()
window.title("LC Calculation General Business?")

# Create the main frame
frame = tk.Frame(window)
frame.pack()

# Function to update button state
def update_button_state():
    if final_check_var.get() and final_check_tick_var.get():
        button.config(state=tk.NORMAL)
    else:
        button.config(state=tk.DISABLED)

# Function to run LC calculations
def run_calculations():
    if final_check_var.get() and final_check_tick_var.get():
        # Placeholder for the actual LC calculations
        loss_component.set(123.45)  # Example value for the loss component
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

# Add the second label frame
run_section = tk.LabelFrame(frame, text="Run the LC Calculation")
run_section.grid(row=0, column=1, sticky="news")

# Variables to track checkbox states
final_check_var = tk.BooleanVar()
final_check_tick_var = tk.BooleanVar()

# Creating checkbuttons
final_check = tk.Checkbutton(run_section, text="Check conditions before running LC Calculations",
                             variable=final_check_var, command=update_button_state)
final_check.grid(row=1, column=0)

final_check_tick = tk.Checkbutton(run_section, text="Checked file paths",
                                  variable=final_check_tick_var, command=update_button_state)
final_check_tick.grid(row=1, column=1)

# Creating the button
button = tk.Button(run_section, text="Run LC Calculations", command=run_calculations, state=tk.DISABLED)
button.grid(row=2, column=1)

# Add a label frame for modifiable variables
variables_section = tk.LabelFrame(frame, text="Modifiable Variables")
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
    tk.Label(variables_section, text=var_name).grid(row=i, column=0, padx=5, pady=5)
    entry = tk.Entry(variables_section)
    entry.grid(row=i, column=1, padx=5, pady=5)
    variable_entries[var_name] = entry

# Collect variable values button (for demonstration)
collect_button = tk.Button(variables_section, text="Collect Variable Values", command=get_variable_values)
collect_button.grid(row=len(variable_names), column=1, pady=10)

# Add a label frame for output
output_section = tk.LabelFrame(frame, text="Output")
output_section.grid(row=2, column=1, sticky="news")

# Loss component display
loss_component_label = tk.Label(output_section, text="Loss Component:")
loss_component_label.grid(row=0, column=0, padx=5, pady=5)
loss_component = tk.DoubleVar()
loss_component_display = tk.Label(output_section, textvariable=loss_component)
loss_component_display.grid(row=0, column=1, padx=5, pady=5)

# Output file selection
output_file_var = tk.StringVar()
output_file_button = tk.Button(output_section, text="Select Output File Location", command=select_output_file)
output_file_button.grid(row=1, column=0, padx=5, pady=5)
output_file_display = tk.Entry(output_section, textvariable=output_file_var, state='readonly')
output_file_display.grid(row=1, column=1, padx=5, pady=5)

# Start the GUI event loop
window.mainloop()
