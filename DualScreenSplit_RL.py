'''
Program to change the resolution settings for Rocket League
'''

# variables
settings_file = "C:\\Users\\delsuckahh\\Documents\\My Games\\Rocket League\\TAGame\\Config\\TASystemSettings.ini"
list_yes = ["yes", "y", "yep", "yeppers", "ok", "sure", "si"]
list_no = ["no", "n", "nope", "nein"]
# these are the options - update this dict for additional profiles
# syntax - {profile name} : [{ResX},{ResY},{Borderless},{Fullscreen}]
profiles = {"single_screen" : [1920,1080,"True","False"],
            "dual_screen" : [3840,1080,"False","True"]}


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

print("This program will change resolution settings for Rocket League\n")
print("Please select a profile from the following:\n>")

while True:
    for key in profiles:
        print(key)
    user_choice = input()
    if user_choice not in profiles:
        print("Invalid choice...Try again.")
    else:
        print("Changing resolution to: " + str(profiles[user_choice][0]) + " x "
               + str(profiles[user_choice][1]) + "\n")
        changeFile(settings_file,"ResX","ResX=%s" % str(profiles[user_choice][0]))
        changeFile(settings_file,"ResY","ResY=%s" % str(profiles[user_choice][1]))
        changeFile(settings_file,"Bord","Borderless=%s" % profiles[user_choice][2])
        changeFile(settings_file,"Full","Fullscreen=%s" % profiles[user_choice][3])
        print("Resolution settings have been updated!")
        break

input("Procedure done.  Press Enter to exit")
