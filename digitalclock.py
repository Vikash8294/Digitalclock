import tkinter as tk
import time

def update_time():
    # Get the current local time
    current_time = time.strftime('%H:%M:%S')  # Hour:Minute:Second format
    label.config(text=current_time)  # Update the label text with the current time
    # Call update_time function every 1000ms (1 second)
    label.after(1000, update_time)

# Create the main window
root = tk.Tk()
root.title("Digital Clock")

# Set the size of the window
root.geometry("400x200")

# Create a label widget to display the time
label = tk.Label(root, font=("Helvetica", 48), fg="black")
label.pack(anchor="center", pady=50)

# Call the update_time function to display the current time
update_time()

# Start the Tkinter event loop
root.mainloop()
