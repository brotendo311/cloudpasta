#!/home/juice/tools/venv/bin/python
from time import sleep
import pyperclip
import pyautogui


#with open('script','r') as f:
#	pyperclip.copy(f.read())


# Get clipboard content
clipboard_content = pyperclip.paste()
print(clipboard_content)

print('sleeping for 2 seconds, be sure to click where you want the text pasted within that 5 seconds')

sleep(2)
# Create a keyboard controller
pyautogui.write(f"{clipboard_content}")


