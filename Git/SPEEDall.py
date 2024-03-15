import serial
import time
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress  # Importing linregress for linear regression

#this code analyses your inputs (reaction speeds) and gives out info based on it

ser = serial.Serial()
ser.baudrate = 115200
ser.port = "COM3"
ser.open()


all_speeds = []

run_counter = 0  
previous_data = ""  


file_path = "speed_data.txt"
file = open(file_path, "w")

while run_counter < 5:  
    
    microbitdata = str(ser.readline())

   
    speed = microbitdata[2:]
    speed = speed.replace(" ", "")
    speed = speed.replace("\\r\\n", "")
    speed = speed.replace("'", "")

    try:
        speed = int(speed)
    except ValueError:
        continue  

    
    if microbitdata != previous_data and speed > 0:
        
        print("Your speed was ", speed, "ms.")

       
        file.write(f"Run {run_counter + 1}: {speed} ms\n")

        all_speeds.append(speed)  
        previous_data = microbitdata  
        run_counter += 1  

ser.close()

file.close()

print("All speeds:", all_speeds)

# Plotting the speeds
average_speed = np.mean(all_speeds)
x_values = range(1, len(all_speeds) + 1)

plt.plot(x_values, all_speeds, marker='o', linestyle='None', label='Speed')
plt.plot(np.unique(x_values), np.poly1d(np.polyfit(x_values, all_speeds, 1))(np.unique(x_values)), linestyle='-', color='blue', label='Line of Best Fit')

plt.axhline(y=average_speed, color='r', linestyle='--', label=f'Your Average Speed ({round(average_speed):.0f}) ms')
plt.axhline(y=300, color='g', linestyle='--', label='Human Average Speed (300ms)')
plt.axhline(y=220, color='m', linestyle='--', label='F1 Driver Average Speed (220ms)')
plt.axhline(y=150, color='b', linestyle='--', label='Cheetah Average Speed (150ms)')
plt.axhline(y=10, color='y', linestyle='--', label='Frog Average Speed (10ms)')
plt.title('Speeds from 5 Runs')
plt.xlabel('Run Number')
plt.ylabel('Speed (ms)')
plt.xticks(x_values)
plt.grid(True)
plt.legend()



slope, _, _, _, _ = linregress(x_values, all_speeds)
slope = round(slope,1)


if slope > 0:
    print("\nThe line of best fit has a positive correlation.\nTherefore we predict your future reaction times to get slower.")
elif slope < 0:
    print("\nThe line of best fit has a negative correlation.\nTherefore we predict your future reaction times to get faster.")
else:
    print("\nThe line of best fit does not indicate any correlation (horizontal line).\nTherefore we predict your future reaction times to be the same.")
    

plt.show()