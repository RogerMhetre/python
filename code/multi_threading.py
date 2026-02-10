# multithreading = Used to perform multiple tasks concurrently (multitasking)
#                  Good for I/O bound tasks like reading files or fetching data from APIs 
#                  threading.Thread(target=my_function)
# WE do threading to accomplish more tasks at the same time 

import threading 
import time

def walk_dog(first, last):
    time.sleep(6)
    print(f"You finished walking {first} {last}")

def take_out_trash():
    time.sleep(2)
    print("You take out the trash")

def get_mail():
    time.sleep(4)
    print("You get the mail")

chore1 = threading.Thread(target=walk_dog, args=("Snoop,"))   #Use one comma if there is one item
                                                              #when passing an argument
chore1.start()

chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()

chore1.join()
chore2.join()
chore3.join()

print("All chores completed!")









