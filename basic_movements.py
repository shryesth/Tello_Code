from djitellopy import tello
from time import sleep

me = tello.Tello()          #made a tello object
me.connect()                #made connection to drone
print(me.get_battery())     #printing the battery of drone

me.takeoff()    #taking off the drone
sleep(1)    #sending a wait for 2 seconds
me.send_rc_control(0,50,0,0) #sending rc parameter
sleep(2)    #sending a wait for 2 seconds
me.send_rc_control(0,0,0,180) #sending rc parameter
sleep(2)    #sending a wait for 2 seconds
me.send_rc_control(0,60,0,0) #sending rc parameter
sleep(2)    #sending a wait for 2 seconds
me.send_rc_control(0,0,0,0)
me.land()   #landing the drone