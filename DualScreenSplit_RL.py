# Read file at My Documents > My Games > RocketLeague > TAGame > Config
# file named TASystemSettings.ini.
# Find a row with "ResX" and set it to 3840 (2 x 1080p), and "ResY" to 1080
# (Naturally you have to change the values if you have a different
# resolution monitors).
# Press CTRL + F and search for "borderless", when you find it,
# set it to "True". Then search for "fullscreen", and change all three
# instances to "False". Save and close the file.

# file text function saved in practice.py, copy over and implement here

# possibly get rid of custom functionality for DynamicShadows
# just have one to set split screen and one to disable

# add check for [systemsettings] or not
# get list of video settings, possibly in different program?
# or a class / function call perhaps?

list_yes = ["yes", "y", "yep", "yeppers", "ok", "sure", "si"]
list_no = ["no", "n", "nope", "nein"]

def changeFile(inFile, oldString, newString):
    with open(inFile) as f:
      s = f.readlines()
      line = [x.strip() for x in s]
      for n, i in enumerate(line):
          if i[:4]==oldString:
              line[n] = newString

    with open(inFile, "w") as f:
        for item in line:
            f.write("%s\n" % item)

def changeReso(resX, resY):
    print("Changing resolution to: " + str(resX) + " x " + str(resY) + "\n")
    changeFile("TestSettingsNew.txt","ResX","ResX=%s" % str(resX))
    changeFile("TestSettingsNew.txt","ResY","ResY=%s" % str(resY))
    changeFile("TestSettingsNew.txt","Bord","borderless=True")
    changeFile("TestSettingsNew.txt","Full","Fullscreen=False")

'''
functionality coming soon...
def changeVideoSettings():
    print("Video Settings have been changed\n")
'''


print("This program will allow dual screen split screen play for Rocket League\n")

while True:
    lo_default = input("Would you like to use default set up?\n>").lower()
    if lo_default in list_yes:
        print("You selected yes\n")
        print("Setting up default settings...\n")
        changeReso(3840,1080)
        print("Dual screen setup is complete.")
        #print("Changing video settings...\n")
        #changeVideoSettings()
        break
    elif lo_default in list_no:
        print("You selected no\n")
        while True:
            try:
                new_width = int(input("Please enter the combined width\n>"))
                break
            except ValueError:
                print("ERROR - Please input a number only\n")
        while True:
            try:
                new_height = int(input("Please enter the height\n>"))
                break
            except ValueError:
                print("ERROR - Please input a number only\n")
        #while True:
            #new_settings = str(input("Alter the video settings for performance?\n>"))
            #if not(new_settings in list_yes) and not(new_settings in list_no):
                #print("error")
            #break
        print("Setting up new resolution settings...")
        changeReso(new_width, new_height)
        print("Dual screen setup is complete.")
        #if new_settings in list_yes:
            #changeVideoSettings()
        #elif new_settings in list_no:
            #print("You did not change the video settings\n")

        break
    else:
        print("ERROR - Invalid input\n")




input("Procedure done.  Press Enter to exit")
