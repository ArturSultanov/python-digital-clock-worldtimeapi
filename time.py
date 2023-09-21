import requests
from tkinter import Tk, Label
from datetime import datetime


def update_time():
    """Getting proper time depend on current IP"""
    time_ms_accuracy = 1
    time_ms_coefficient = time_ms_accuracy - 6
    time_ms_update = int(1000 / (10 ^ (time_ms_accuracy-1)))


    try:
        # Get time data from  WorldTimeAPI.
        response = requests.get("https://worldtimeapi.org/api/ip")
        data = response.json()
        time_str = data["datetime"]
        current_time = datetime.fromisoformat(time_str)
        current_time_formatted = current_time.strftime("%H:%M:%S:%f")\
                                                [:time_ms_coefficient]
        window_label.config(text=current_time_formatted)

    except Exception as e:
        print(f"Error {e}")

    window.after(time_ms_update, update_time)


window = Tk()
window.title("Digital Clock")

window_label = Label(window, font=("Helvetica", 48))
window_label.pack(pady=20)

update_time()

window.mainloop()
