import os
path = os.path.join("folder", "file.txt")
print(path)  # folder/file.txt  (Linux)

import os
print(os.path.exists("data/myfile.txt"))  # True/False

import os
print(os.path.isfile("test.txt"))  # True/False

import os
print(os.path.isdir("data"))  # True/False

import os
print(os.path.basename("/home/roger/myfile.txt"))  # myfile.txt

import os
print(os.path.dirname("/home/roger/myfile.txt"))  # /home/roger

import os
print(os.path.abspath("myfile.txt"))  
# /home/roger/whatever/myfile.txt

import os
print(os.path.split("/home/roger/myfile.txt"))  
# ('/home/roger', 'myfile.txt')

import os
print(os.path.getsize("test.txt"))  # e.g. 128

import os
print(os.path.splitext("myfile.txt"))  
# ('myfile', '.txt')

import os
print(os.path.samefile("a.txt", "b.txt"))  # True/False

os.path.isabs("/home/roger/file.txt")  # True
os.path.isabs("file.txt")  # False

os.path.normpath("folder//../folder2/file.txt")
# -> 'folder2/file.txt'

os.path.realpath("link_to_file")
# -> '/home/roger/original_file'


