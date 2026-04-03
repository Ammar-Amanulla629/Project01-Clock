import tkinter as tk
import requests
from datetime import datetime, timedelta

current_time = None


#switched to using an API to obtain real world time
def API_clock():
    global current_time
    try:
        if current_time is None:
            url = 'https://timeapi.io/api/Time/current/zone?timeZone=Europe/London'
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
            response = requests.get(url, headers=headers, timeout=5)

            response.raise_for_status()
            data = response.json()
            dt = data['dateTime']

            current_time = datetime.fromisoformat(dt.replace('Z', ''))
        else:
            current_time += timedelta(seconds=1)
        label.config(text=current_time.strftime("%H:%M:%S"))

    except Exception as e:
        # This will print the actual error to your terminal/console!
        print(f"Debug Error: {e}") 
        label.config(text="Error catching time")
        
        # Reset current_time so it tries to hit the API again on the next loop
        current_time = None 

    # Loop every 1000ms (1 second)
    root.after(1000, API_clock)

    

root = tk.Tk()
root.title("API Clock")
root.geometry("300x150")
root.configure(bg = "Black")

label = tk.Label(root, font = ("Vienna", 40))
label.pack(pady=40)

API_clock()
root.mainloop()