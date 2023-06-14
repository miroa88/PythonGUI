import os

unc_path = r"\\gandalf\MissionShare\/"

# List all files in the 'testing' folder
for file in os.listdir(unc_path):
    print(file)