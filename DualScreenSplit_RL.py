'''
Program to change the resolution settings for Rocket League
'''

# set the variables
settings_file = r'C:\Users\delsuckahh\Documents\My Games\Rocket League\TAGame\Config\TASystemSettings.ini'
params = ["ResX", "ResY", "Borderless", "Fullscreen"]
profiles = {"single screen": [1920, 1080, True, False],
            "dual screen":   [3840, 1080, False, True]}
options = '\n'.join(profiles.keys())

# define the function
def changeFile(inFile, k, v):
    with open(inFile, 'r') as f:
        lines = [k+'='+str(v) if l.startswith(k) else l for l in f]
    
    with open(inFile, 'w') as f:
        for line in lines:
            print(line, file=f)

# get the options
print("This program will change resolution settings for Rocket League")
print("Please select a profile from the following:", options, sep='\n')
user_choice = input("> ")
while user_choice not in profiles:
    print("Invalid choice. Please try again:", options, sep='\n')
    user_choice = input("> ")

# change the settings
settings = profiles[user_choice]
print("Changing resolution to %dx%d" % tuple(settings[:2]))
for k, v in zip(params, settings):
    print("Setting {} to {}".format(k, v))
    changeFile(settings_file, k, v)

# finish the thing
print("Resolution settings have been updated!")
print("Procedure done. Press Enter to exit, or any other key to delay your inevitable fate")
input()
