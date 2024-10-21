import os
import time
import random

# Function to toggle Caps Lock using xdotool
def toggle_caps_lock():
    try:
        os.system("xdotool key Caps_Lock")  # Simulate pressing Caps Lock
    except Exception as e:
        print(f"System Check Resolved Error: {e}")

# Main loop to randomly toggle Caps Lock every few seconds
if __name__ == "__main__":
    while True:
        # Randomize the interval between 3 and 10 seconds
        interval = random.randint(3, 10)
        
        toggle_caps_lock()  # Toggle the Caps Lock key
        
        time.sleep(interval)  # Wait for the next random interval
