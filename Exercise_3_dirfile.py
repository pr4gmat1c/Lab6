import os
filepath = "C:\\Users\\Yerik\\PycharmProjects\\Lab6\\dir-and-files\\Exercise_2.py"
resExist = os.access(filepath, os.F_OK)
if resExist == True:
    directory = os.path.dirname(filepath)
    filename = os.path.basename(filepath)
    print(f'File directory {directory}; File name: {filename}')
