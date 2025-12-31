import pyautogui
import keyboard
import time
import pygetwindow as gw

print("Running... Press Ctrl+B ")
print(" Ctrl+C to stop ")

while True:
    if keyboard.is_pressed("ctrl+b"):
        try:
            current_window = gw.getActiveWindow()
        except:
            current_window = None

        try:
            discord_window = [w for w in gw.getAllTitles() if "Discord" in w]
            if discord_window:
                gw.getWindowsWithTitle(discord_window[0])[0].activate()
                time.sleep(0.5)
                
                pyautogui.typewrite("brb")
                pyautogui.press("enter")
                time.sleep(0.5)
                
                if current_window:
                    current_window.activate()
            else:
                print("Discord not found")
        except Exception as e:
            print("Error:", e)

        time.sleep(1)  
