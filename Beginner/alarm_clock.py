import time
import datetime
import pygame

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = "my_music.mp3"                 #include your music file
    is_running = True

    while is_running:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Current time: {current_time}")

            if current_time == alarm_time:
                print("Wake UP! GODDAMMIT!!" \
                      "You are getting comfortable!!")

                pygame.mixer.init()
                pygame.mixer.music.load(sound_file)
                pygame.mixer.music.play()

                start_time = time.time()

                while pygame.mixer.music.get_busy():            
                    if time.time() - start_time >= 5:          #The alarm is set to ring 20 seconds
                         pygame.mixer.music.stop()
                         break

                    time.sleep(1)

                is_running = False
            
            time.sleep(1)                      #including time.sleep() cause it will run the commands
                                               #million times and it is dangerous to CPU
            
if __name__ == "__main__":              #we use this so that the file don't run when it is used for just
                                        #taking the components of this file 
                                        
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)
