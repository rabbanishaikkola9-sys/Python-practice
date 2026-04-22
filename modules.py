import pyttsx3
engine = pyttsx3.init()

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

engine.say("hey this is rabbani and this is practice session")
engine.runAndWait()
import os

# Path of C drive
path = "C:\\"

# List all contents
try:
    contents = os.listdir(path)
    
    print(f"Contents of {path}:\n")
    for item in contents:
        print(item)

except PermissionError:
    print("Permission denied for some folders.")
except Exception as e:
    print("Error:", e)
    
import random

# Random number between 1 and 100
num = random.randint(1, 100)
print("Random number:", num)

# Random choice from a list
colors = ["red", "blue", "green", "yellow"]
choice = random.choice(colors)
print("Random color:", choice)

# Shuffle a list
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print("Shuffled list:", numbers)