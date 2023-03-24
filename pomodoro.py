# Pomodoro Technique timer app
# this app creates a GUI with a timer, a start button, and a reset button
# when the start button is clicked, the pomodoro_timer function is called to begin the 25 minute countdown
# the timer counts down, updates every second, and when it reaches 0 seconds, triggers an alarm sound
# the reset button resets the timer to 25 minutes as per the Pomodoro Technique as described in the book by Francesco Cirillo
# link to info here:  https://francescocirillo.com/products/the-pomodoro-technique
# link to how to create a timer using tkinter: https://www.tutorialspoint.com/how-to-create-a-timer-using-tkinter
# link to how to use the divmod function: https://www.programiz.com/python-programming/methods/built-in/divmod

# import required libraries

import tkinter as tk
from playsound import playsound
import time


# create a timer function to:

    # use the while loop to count down from seconds to 0, and mins and secs should be calculated based on the remaining seconds
    # calculate minutes and seconds based on the seconds value and update the timer label with the formatted time
    # use the time.sleep(1) function to pause the loop for one second between each update
    # use the playsound function to play an alarm sound when the timer gets to 0 minutes and 0 seconds


# minutes = 25

def pomodoro_timer(minutes):
    seconds = minutes * 60
    while seconds > -1:
        mins, secs = divmod(seconds, 60) # calculate the minutes and seconds part of the function's output at each iteration
        timer.set(f'{mins:02d}:{secs:02d}')
        window.update()
        time.sleep(1) # add an interval of 1 second (pause) before the next iteration is executed in the loop
        seconds -= 1  # countdown
    
    playsound('alarm.wav')

# create a TKinter GUI for the timer

window = tk.Tk()
window.title('Pomodoro Timer')
window.geometry('300x150')
window.configure(bg='#5d5e63')

timer = tk.StringVar()
timer.set('25:00')

timer_label = tk.Label(window, textvariable=timer, font=('Arial', 40), fg='#c2f230', bg='#000000')
timer_label.pack(pady=20)

start_button = tk.Button(window, text='Start', font=('Arial', 16), command=lambda: pomodoro_timer(25))
start_button.pack(side='left', padx=20)

reset_button = tk.Button(window, text='Reset', font=('Arial', 16), command=lambda: timer.set('25:00'))
reset_button.pack(side='right', padx=20)

window.mainloop()

