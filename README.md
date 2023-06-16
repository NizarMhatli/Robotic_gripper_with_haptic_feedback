# Robotic gripper with haptic feedback 

package to create application to control robotic gripper with haptic feedback using pressure sensor.

# hardware used

Touchence pressure sensor: http://www.touchence.jp/en/products/cube03.html

Robotiq f2-85 robotic gripper: https://robotiq.com/products/2f85-140-adaptive-robot-gripper


# packages used: 

= python package for touchence sensor 
- python pckage to control Robotiq gripper 

# project inspired by this video from touchence main channel: 

(all rights reserved to touchence) 

https://www.youtube.com/watch?v=-jpk3o9CFCU&ab_channel=Touchence


# Main objective: 

be able to use a Robotiq gripper to grab fragile objects like pet bottles precisely using feedback from the sensor.


![test drawio (32)](https://user-images.githubusercontent.com/47193436/159449218-03cf6de2-749e-44f5-8f27-fe24671a5fbc.png)




# Package scope:  

Picking fragile objects using robots is very high in demand right now, this project goal is to create an application to combine the precision of the Robotiq f2-85 gripper position control, and the real-time feedback from the touchence pressure sensor.

we created a simple GUI to start a simple test process.


![griptest](https://github.com/NizarMhatli/Robotic_gripper_with_haptic_feedback/assets/47193436/8448b67f-9bf3-4897-bc25-16e887c52256)


Gripper set button will reset the gripper to its initial position.

The GRIP button starts the gripping test 

the test: the gripper fingers will start closing while reading the sensor values in real time if a change in the sensor value happens the gripper will stop moving indicating there is an object detected.
