I made this tool for pasting from my host machine into the cloud (vSphere or others).  It will take any copied text and emulate keys being pressed on the keyboard. It can paste a large script file.    There is a 2 second delay so you can click into the cloud environment and it will send the copied text/script into the cloud. I have this script on a keyboard shortcut on Linux.  I think its possible to add it to a keyboard shortcut on Windows, but I will have to research that. I will export an all inclusive EXE for Windows so users without python installed can utilize this tool.

Install Python

Install required libraries

pip install pyperclip

pip install pyautogui

python cloudpasta.py

