## Discord Auto text Bot (Python)<br>
#This is a small Python automation script that sends a "brb" message in Discord when a keyboard shortcut is pressed, and then switches back to the previously active window.<br>

## WHAT THIS SCRIPT DOES<br>
#Runs continuously in the background<br>
#Listens for the keyboard shortcut Ctrl + B<br>
#When pressed:<br>
* Detects the currently active window
* Searches for an open Discord window
* Brings Discord to the foreground
* Types "brb" and presses Enter
* Switches back to the original window
* Keeps running until manually stopped

## HOW THE SCRIPT WORKS<br>
#Keyboard Detection<br>
* Uses the "keyboard" module to listen for Ctrl + B globally.
* Window Handling
* Uses "pygetwindow" to:
** Get the currently active window
** Find a window with "Discord" in its title
** Activate and restore windows
#Key Press Automation<br>
* Uses "pyautogui" to:
** type text
** Simulate pressing the Enter key
#Window Restoration<br>
* Saves the previously active window and restores it after sending the message.

## REQUIREMENT<br>
#Python 3.8 or newer<br>
#Discord must be running and logged in<br>
#Script must be allowed to capture global keyboard input<br>

## Python packages required:<br>
#pyautogui<br>
#keyboard<br>
#pygetwindow<br>

##INSTALLATION<br>
#Clone the repository:<br>
```bash
git clone https://github.com/R81194/discord-text-bot-.git
cd discord-text-bot-
```
#Install dependencies:<br>
`pip install pyautogui keyboard pygetwindow`

##RUNNING THE SCRIPT<br>
#From the project folder, run:<br>
```bash
python bot.py
```

#Once running, the terminal will show:<br>
* "Running... Press Ctrl+B"<br>
* "Ctrl+C to stop"<br>

#KEYBOARD SHORTCUTS<br>
* Ctrl + B → Sends "brb" in Discord<br>
* Ctrl + C → Stops the script<br>

## AUTO KEY PRESSER / PERMISSIONS NOTES<br>
#This script does NOT require any external auto key presser software.<br>
#All key presses are simulated internally using pyautogui.<br>
#You will need an external third party auto key presser for pressing Ctrl + B as this will do the work.<br>
* You should have an opened particular channel in which u want send spam text.<br>
* You can u use any auto key presser available on internet for automating Ctrl + B presses.<br>
* It is highly recommended to dont spam Ctrl + B as this bot has a sleep time. You can set auto key press time to 5 sec or above.<br>
* Please do this in dedicated spam channels.<br>
* This can be against discord policies or channel rules.<br>
* This is just for educational purposes.<br>
* You can watch youtube or listen music while running this bot. But this can cause problems in games and other stuff. <br>

#Windows:<br>
* Run the terminal as Administrator<br>
* Required for global keyboard detection<br>

## LIMITATIONS<br>
#Discord must not be minimized to tray<br>
#Discord window title must contain the word "Discord"<br>

