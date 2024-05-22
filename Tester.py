import tkinter as tk
from tkinter import ttk

# Set up the main window
root = tk.Tk()
root.title("Risk Adjustment Input Table")

# Create a frame for the table
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Create the table header
headers = ["Line of Business", "Risk Adjustment"]
for col, text in enumerate(headers):
    header = tk.Label(frame, text=text, borderwidth=1, relief="solid")
    header.grid(row=0, column=col, padx=5, pady=5)

# Create the input fields
entries = []
for row in range(1, 15):  # 14 rows of inputs
    row_entries = []
    for col in range(2):  # 2 columns
        entry = tk.Entry(frame, borderwidth=1, relief="solid")
        entry.grid(row=row, column=col, padx=5, pady=5)
        row_entries.append(entry)
    entries.append(row_entries)

# Create a submit button
def submit():
    data = [[entry.get() for entry in row] for row in entries]
    print(data)  # Or process the data as needed

submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack(pady=10)

# Run the main loop
root.mainloop()
