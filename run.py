# Made by Pieskyy

# Hello! This script Automates clickiing the continue playing button on songsterr to allow for uninterrupted playing!
# This script looks for the button image on screen and clicks it when found
# It is reletively easy to make so comments are left down below to help you understand how it works and modify it if needed

# | Common Issues |
# 1. The script may not find the button if songsterr isnt on the primary screen
# 2. The script may not find the button if the file "playback.png" is not in the same directory as this script, make sure to download it from the github page
# 3. The script may not find the button if the button image has changed, you can take a new screenshot of the button and replace "playback.png" with it
# 4. The button may not disappear after clicking, this is a songsterr issue and not a script issue. just refresh the site

# If theres any other issues feel free to let me know on github!


import pyautogui
import time
import keyboard

time.sleep(3) # Time to switch to the screen with songsterr, if you need more time, increase this (This is just howlong it takes for the bot to start)
print("Started. Press 'q' to quit.") # can be any letter, just change it below in the next line aswell

while True:
    if keyboard.is_pressed("q"): # If the user presses q, stop the script
        print("Stopped.")
        break
    
    try:
        button = pyautogui.locateOnScreen("playback.png", confidence=0.7) # Try to find the button

        if button: # Button found
            x, y = pyautogui.center(button) # Click the center of the button
            pyautogui.click(x, y)
            time.sleep(1) # Wait a second after clicking to avoid multiple clicks
        else: # Button not found
            time.sleep(0.1)
            
    except:
        time.sleep(0.1) # If any error, just continue