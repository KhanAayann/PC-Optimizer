#Vortex Optimizer

'''
Name: Aayan Ahmad Khan
Date: 08/01/2026
INFO: This is an PC Tweak Tool that Optimized the pc to get the best gaming performence.
'''

import tkinter as tk
from tkinter import *
from tkinter import messagebox
import os
import colorama
import random
import webbrowser
from PIL import Image, ImageTk
import ctypes
import shutil
import tempfile
import subprocess
from tkvideo import tkvideo
import pyperclip

welcome = r"""
 __     __                       __                                 ______              __      __                __                               
|  \   |  \                     |  \                               /      \            |  \    |  \              |  \                              
| $$   | $$  ______    ______  _| $$_     ______   __    __       |  $$$$$$\  ______  _| $$_    \$$ ______ ____   \$$ ________   ______    ______  
| $$   | $$ /      \  /      \|   $$ \   /      \ |  \  /  \      | $$  | $$ /      \|   $$ \  |  \|      \    \ |  \|        \ /      \  /      \ 
 \$$\ /  $$|  $$$$$$\|  $$$$$$\\$$$$$$  |  $$$$$$\ \$$\/  $$      | $$  | $$|  $$$$$$\\$$$$$$  | $$| $$$$$$\$$$$\| $$ \$$$$$$$$|  $$$$$$\|  $$$$$$\
  \$$\  $$ | $$  | $$| $$   \$$ | $$ __ | $$    $$  >$$  $$       | $$  | $$| $$  | $$ | $$ __ | $$| $$ | $$ | $$| $$  /    $$ | $$    $$| $$   \$$
   \$$ $$  | $$__/ $$| $$       | $$|  \| $$$$$$$$ /  $$$$\       | $$__/ $$| $$__/ $$ | $$|  \| $$| $$ | $$ | $$| $$ /  $$$$_ | $$$$$$$$| $$      
    \$$$    \$$    $$| $$        \$$  $$ \$$     \|  $$ \$$\       \$$    $$| $$    $$  \$$  $$| $$| $$ | $$ | $$| $$|  $$    \ \$$     \| $$      
     \$      \$$$$$$  \$$         \$$$$   \$$$$$$$ \$$   \$$        \$$$$$$ | $$$$$$$    \$$$$  \$$ \$$  \$$  \$$ \$$ \$$$$$$$$  \$$$$$$$ \$$      
                                                                            | $$                                                                   
                                                                            | $$                                                                   
                                                                             \$$    

                                                                Follow us on Github!                                                               
"""

print(colorama.Fore.BLUE + welcome)

root = tk.Tk()
root.geometry("300x500")
root.title("Vortex Optimizer")
root.config(bg="Black")
root.resizable(False, False)

messagebox.showinfo("IMPORTANT NOTE", "This PC Tweak Tool is designed to optimize system settings to improve gaming performance, reduce input lag, and enhance overall system responsiveness.  Use responsibly and only on systems you understand. A restart may be required for some tweaks to take effect. MADE BY PROFESSORDEV")

try:
    root.iconbitmap(r"C:\Users\Aayan\Desktop\Freelancing\napster.ico")
except Exception as e:
    print(f"Warning: Could not load icon.ico — {e}")

try:
    original_image = Image.open(r"C:\Users\Aayan\Desktop\Freelancing\vortextoptimizer.png")
    
    resized_image = original_image.resize((240, 180))
    
    photo = ImageTk.PhotoImage(resized_image)
    
    label = tk.Label(root, image=photo, bg="black")
    label.place(x=40, y=-35)

    label.image = photo
except Exception as e:
    print(f"Warning: Could not load image — {e}")

def goweb():
    webbrowser.open("https://guns.lol/professordev")

Devlabel = Button(root, text="MADE by: ProfessorDev π", bg="black", fg="Red", bd=0, command=goweb, font=("Impact", 10))
Devlabel.place(x=6, y=461)

def change_color():
    colors = ["#FF073A", "#FF6F00", "#FFFF00", "#39FF14", "#1B03A3", "#FF10F0", "#9B4DFF", "#00FFFF", "#FF00FF", "#32CD32"]
    Devlabel["fg"] = random.choice(colors)
    root.after(300, change_color)

change_color()

clearspace = Label(root, text="Free Up Space (Clear temp first!):", bg="black", fg="white",font=("Impact", 10))
clearspace.place(x=10, y=105)

def empty_recycle_bin():
    ctypes.windll.shell32.SHEmptyRecycleBinW(
        None,
        None,
        0x00000001 | 0x00000002 | 0x00000004
    )

Recyclebutton = Button(root, text="📁 Clear Recycling Bin", bg="grey",command=empty_recycle_bin ,font=("Impact", 10))
Recyclebutton.place(x=15, y=130)

def clear_temp_folders():
    temp_paths = [
        tempfile.gettempdir(),
        r"C:\Windows\Temp"
    ]

    for temp_path in temp_paths:
        if not os.path.exists(temp_path):       
            continue

        for item in os.listdir(temp_path):
            item_path = os.path.join(temp_path, item)

            try:
                if os.path.isfile(item_path) or os.path.islink(item_path):
                    os.unlink(item_path)
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path, ignore_errors=True)
            except PermissionError:
                pass
            except Exception as e:
                print(f"Failed to delete {item_path}: {e}")

Tempbutton = Button(root, text="📁 Clear Temporary Files", bg="grey",command=clear_temp_folders ,font=("Impact", 10))
Tempbutton.place(x=15, y=165)

SettingLabel = Label(root, text="Windows Settings:", bg="black", fg="white",font=("Impact", 10))
SettingLabel.place(x=15, y=195)


###
showing = r"&{$p='HKCU:\Software\Microsoft\GameBar';Set-ItemProperty -Path $p -Name AllowAutoGameMode -Type DWord -Value 1}"

cmd = r"""
# Set overall visual effects to best performance
Set-ItemProperty -Path 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\VisualEffects' -Name VisualFXSetting -Type DWord -Value 2;

# Disable animations
Set-ItemProperty -Path 'HKCU:\Control Panel\Desktop' -Name UserPreferencesMask -Value ([byte[]](144,18,3,128,16,0,0,0));

# Disable menu animations
Set-ItemProperty -Path 'HKCU:\Control Panel\Desktop' -Name MenuShowDelay -Value 0;

# Disable taskbar animations
Set-ItemProperty -Path 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced' -Name TaskbarAnimations -Type DWord -Value 0;

# Disable window animations
Set-ItemProperty -Path 'HKCU:\Control Panel\Desktop\WindowMetrics' -Name MinAnimate -Value 0;
"""

def run(cmd):
    subprocess.run(["powershell", "-Command", cmd])

def editenv(cmd):
    subprocess.run(["powershell", "-Command", cmd])

GameModeButton = Button(root,text="🎮 Turn Game Mode On",bg="grey", command=lambda: run(showing), font=("Impact", 10))
GameModeButton.place(x=15, y=219)
Editenv = Button(root,text="✨Disable Animations",bg="grey", command=lambda: run(cmd), font=("Impact", 10))
Editenv.place(x=15,y=253)
###

NoteLabel = Label(root, text="NOTE: Click the button only once to apply the changes.", bg="black", fg="white", font=("Impact", 10))
NoteLabel.place(x=5, y=480)
###
DisService = Label(root, text="Disable Services:(Read Infos First!)", bg="black", fg="white", font=("Impact", 10))
DisService.place(x=15, y=285)

def Dser():
    services = [
        "Spooler",
        "Fax",
        "XblGameSave",
        "XboxGipSvc",
        "XboxNetApiSvc",
        "MapsBroker",
        "TabletInputService",
        "RemoteRegistry",
        "bthserv",
        "WSearch",
        "DiagTrack",
        "RetailDemo"
    ]

    for service in services:
        try:
            subprocess.run(
                ["powershell", "-Command", f"Stop-Service -Name {service} -Force -ErrorAction SilentlyContinue"],
                capture_output=True
            )

            subprocess.run(
                ["powershell", "-Command", f"Set-Service -Name {service} -StartupType Disabled"],
                capture_output=True
            )

            print(f"Disabled: {service}")

        except Exception as e:
            print(f"Failed: {service} -> {e}")

DisSeButton = Button(root,text="🔨 Disable Unneeded Services", bg="grey", font=("Impact", 10), command=Dser)
DisSeButton.place(x=15, y= 306)

def SerInfoLink():
    webbrowser.open("https://pastebin.com/jZSNDffz")

SerInfo = Button(root, text="🔎", bg="grey", command=SerInfoLink)
SerInfo.place(x=195, y=309)

###
label_video = None
player = None

def play_video():
    global label_video, player

    label_video = tk.Label(root)
    label_video.place(x=0, y=0, relwidth=1, relheight=1)

    player = tkvideo("video.mp4", label_video, loop=1, size=(500, 500))
    player.play()

    label_video.lower()

var = tk.IntVar()

def toggle_action():
    global label_video

    if var.get() == 1:
        if label_video is None:
            play_video()
        else:
            label_video.place(x=0, y=0, relwidth=1, relheight=1)
    else:
        if label_video is not None:
            label_video.place_forget()


chk = Checkbutton(root, text="Play BG Video",variable=var, bg="black", fg="red", font=("Impact", 10), command=toggle_action)
chk.place(x=140, y=461)
###

def copytweaker():
    pyperclip.copy("irm christitus.com/win | iex")

tweaker_button = Button(root, text="Copy📄", command=copytweaker)
tweaker_button.place(x=170, y=365)

tweaker_label = Label(root, text="Advance Tweaker(Recommended):", bg="black", fg="white",font=("Impact", 10))
tweaker_label.place(x=15, y=340)

tweaker_label1 = Label(root, text="irm christitus.com/win | iex", bg="grey", fg="black", font=("Impact", 10))
tweaker_label1.place(x=15, y=365)

root.mainloop()