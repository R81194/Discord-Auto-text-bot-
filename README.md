##Discord Auto text Bot (Python)
#This is a small Python automation script that sends a "brb" message in Discord when a keyboard shortcut is pressed, and then switches back to the previously active window.

##WHAT THIS SCRIPT DOES
#Runs continuously in the background
#Listens for the keyboard shortcut Ctrl + B
#When pressed:
;#Detects the currently active window
;#Searches for an open Discord window
;#Brings Discord to the foreground
;#Types "brb" and presses Enter
;#Switches back to the original window
;#Keeps running until manually stopped

##HOW THE SCRIPT WORKS
#Keyboard Detection
;#Uses the "keyboard" module to listen for Ctrl + B globally.
;#Window Handling
;#Uses "pygetwindow" to:
; #Get the currently active window
; #Find a window with "Discord" in its title
; #Activate and restore windows
#Key Press Automation
;#Uses "pyautogui" to:
; #type text
; #Simulate pressing the Enter key
#Window Restoration
;#Saves the previously active window and restores it after sending the message.

##REQUIREMENT
#Python 3.8 or newer
#Discord must be running and logged in
#Script must be allowed to capture global keyboard input

##Python packages required:
#pyautogui
#keyboard
#pygetwindow

##INSTALLATION
#Clone the repository:
```bash
git clone https://github.com/R81194/discord-text-bot-.git
cd discord-text-bot-
```
#Install dependencies:
`pip install pyautogui keyboard pygetwindow`

##RUNNING THE SCRIPT
#From the project folder, run:
```bash
python bot.py
```

#Once running, the terminal will show:
;#"Running... Press Ctrl+B"
;#"Ctrl+C to stop"

#KEYBOARD SHORTCUTS
;#Ctrl + B → Sends "brb" in Discord
;#Ctrl + C → Stops the script

##AUTO KEY PRESSER / PERMISSIONS NOTES
#This script does NOT require any external auto key presser software.
#All key presses are simulated internally using pyautogui.
#You will need an external third party auto key presser for pressing Ctrl + B as this will do the work.
;#You should have an opened particular channel in which u want send spam text.
;#You can u use any auto key presser available on internet for automating Ctrl + B presses.
;#It is highly recommended to dont spam Ctrl + B as this bot has a sleep time. You can set auto key press time to 5 sec or above.
;#Please do this in dedicated spam channels.
;#This can be against discord policies or channel rules.
;#This is just for educational purposes.
;#You can watch youtube or listen music while running this bot. But this can cause problems in games and other stuff. 

#Windows:
;#Run the terminal as Administrator
;#Required for global keyboard detection

##LIMITATIONS
#Discord must not be minimized to tray
#Discord window title must contain the word "Discord"

