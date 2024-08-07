import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import serial
import threading

# Define the serial port settings
ser = None  # Placeholder for the serial connection

# Function to initialize the serial connection
def start_serial():
    global ser
    try:
        ser = serial.Serial('COM1', 9600)  # Replace with your serial port settings
        serial_status_label.config(text="Serial Status: Connected", foreground="green")
        start_serial_button.config(state=tk.DISABLED)
    except Exception as e:
        serial_status_label.config(text=f"Serial Status: Error - {e}", foreground="red")

# Function to check street light status (dummy function)
def check_street_light():
    if ser is not None and ser.is_open:
        # Replace this with actual code to check street light status
        light_status = "Green"  # Dummy value
        light_status_label.config(text=f"Street Light Status: {light_status}", foreground="green")
    else:
        light_status_label.config(text="Street Light Status: Serial not connected", foreground="red")

# Function to switch off street light (dummy function)
def switch_off_light():
    if ser is not None and ser.is_open:
        # Replace this with actual code to switch off the street light
        light_status_label.config(text="Street Light Status: Off", foreground="red")
    else:
        light_status_label.config(text="Street Light Status: Serial not connected", foreground="red")

# Function to download and save data
def download_and_save_data():
    if ser is not None and ser.is_open:
        # Replace this with code to download and save data
        pass
    else:
        serial_status_label.config(text="Serial Status: Not connected", foreground="red")

# Function to upload data (dummy function)
def upload_data():
    if ser is not None and ser.is_open:
        # Replace this with actual code to upload data
        pass
    else:
        serial_status_label.config(text="Serial Status: Not connected", foreground="red")

# Function to read and display serial data
def read_serial_data():
    while True:
        if ser is not None and ser.is_open and ser.in_waiting > 0:
            data = ser.readline().decode('utf-8')
            serial_monitor.insert(tk.END, data)

# Create the main window
window = tk.Tk()
window.title("Street Light Monitoring")

# Configure window background color
window.configure(bg="#f0f0f0")  # Light gray background

# Create a style for buttons with black text
button_style_black_text = ttk.Style()
button_style_black_text.configure("BlackText.TButton", foreground="black", background="#007acc")  # Black text on blue button style

# Create the "Start Serial" button with black text
start_serial_button = ttk.Button(window, text="Connect to Device", command=start_serial, style="BlackText.TButton")
start_serial_button.grid(row=0, column=0, padx=10, pady=10, sticky="w")

# ... (other buttons using the "BlackText.TButton" style)

# Create a label to display serial connection status
serial_status_label = ttk.Label(window, text="Serial Status: Not connected", foreground="blue", background="#f0f0f0")  # Blue text on light gray background
serial_status_label.grid(row=0, column=1, padx=10, pady=10, sticky="w")

# Create a frame for street light controls
light_control_frame = ttk.Frame(window)
light_control_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

# Create a label for the frame
light_control_label = ttk.Label(light_control_frame, text="Street Light Control", font=("Arial", 14), foreground="blue", background="#f0f0f0")  # Blue text on light gray background
light_control_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

# Create the "Check Street Light" button
check_light_button = ttk.Button(light_control_frame, text="Check Status", command=check_street_light, style="ColorButton.TButton")
check_light_button.grid(row=1, column=0, padx=5, pady=5, sticky="w")

# Create the "Switch Off Light" button
switch_off_button = ttk.Button(light_control_frame, text="Switch Off Light", command=switch_off_light, style="ColorButton.TButton")
switch_off_button.grid(row=1, column=1, padx=5, pady=5, sticky="w")

# Create a label to display street light status
light_status_label = ttk.Label(window, text="Street Light Status: Unknown", foreground="blue", font=("Arial", 14), background="#f0f0f0")  # Blue text on light gray background
light_status_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

# Create a frame for data operations
data_operations_frame = ttk.Frame(window)
data_operations_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

# Create a label for the frame
data_operations_label = ttk.Label(data_operations_frame, text="Data Operations", font=("Arial", 14), foreground="blue", background="#f0f0f0")  # Blue text on light gray background
data_operations_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

# Create the "Download and Save Data" button
download_button = ttk.Button(data_operations_frame, text="Download Data", command=download_and_save_data, style="ColorButton.TButton")
download_button.grid(row=1, column=0, padx=5, pady=5, sticky="w")

# Create the "Upload" button
upload_button = ttk.Button(data_operations_frame, text="Upload Data", command=upload_data, style="ColorButton.TButton")
upload_button.grid(row=1, column=1, padx=5, pady=5, sticky="w")

# Create a scrolled text widget for displaying serial data
serial_monitor = scrolledtext.ScrolledText(window, wrap=tk.WORD, height=10)
serial_monitor.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

# Create a thread to continuously read and display serial data
serial_thread = threading.Thread(target=read_serial_data)
serial_thread.daemon = True
serial_thread.start()

# Configure row and column weights for resizing
window.grid_rowconfigure(4, weight=1)
window.grid_columnconfigure(1, weight=1)

# Start the main GUI loop
window.mainloop()
