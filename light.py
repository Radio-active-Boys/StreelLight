import tkinter as tk
import serial
import csv

# Global variable to track the serial status (started or stopped)
serial_started = False

def start_reading():
    global serial_started
    if not serial_started:
        port = port_entry.get()
        baud_rate = baud_rate_entry.get()
        ser = serial.Serial(port, baud_rate)

        with open('serial_data.txt', 'w') as file:
            while serial_started:
                data = ser.readline()
                data_str = data.decode()
                text.insert('end', data_str)
                file.write(data_str)

def stop_reading():
    global serial_started
    serial_started = False

def download_csv():
    with open('serial_data.txt', 'r') as file:
        lines = file.readlines()
        with open('data.csv', 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            for line in lines:
                csv_writer.writerow([line.strip()])

app = tk.Tk()
app.title("Serial Monitor Reader")

# Create frames for layout
left_frame = tk.Frame(app)
left_frame.pack(side="left", padx=10, pady=10)
right_frame = tk.Frame(app)
right_frame.pack(side="right", padx=10, pady=10)

# Left Frame: Display received data
text = tk.Text(left_frame, bg='black', fg='white')  # Set background to black and text color to white
text.pack(fill="both", expand=True)

# Right Frame: Buttons and input fields
port_label = tk.Label(right_frame, text="Serial Port:")
port_label.pack()

port_entry = tk.Entry(right_frame)
port_entry.pack()

baud_rate_label = tk.Label(right_frame, text="Baud Rate:")
baud_rate_label.pack()

baud_rate_entry = tk.Entry(right_frame)
baud_rate_entry.pack()

start_button = tk.Button(right_frame, text="Start Serial", command=start_reading, bg='blue', fg='white')
start_button.pack()

stop_button = tk.Button(right_frame, text="Stop Serial", command=stop_reading, bg='red', fg='white')
stop_button.pack()

download_button = tk.Button(right_frame, text="Download CSV", command=download_csv, bg='blue', fg='white')
download_button.pack()

app.mainloop()
