import os

folder = "G:\\\\graduation_database\\\\Night"

for filename in os.listdir(folder):
    a = folder + "\\\\" + filename
    print(a)