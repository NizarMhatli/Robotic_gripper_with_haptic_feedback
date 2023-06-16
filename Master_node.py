import sys

import PySimpleGUI as sg
from GRipper_Controll_F import gri_set,grip_op_dynamic_w_blocker
from Sensor_Data_absorber import Get_Sensor_values_degital


def LEDIndicator(key=None, radius=300):
    return sg.Graph(canvas_size=(radius, radius),
             graph_bottom_left=(-radius, -radius),
             graph_top_right=(radius, radius),
             pad=(0, 0), key=key)

def SetLED(window, key, color,color1):
    graph = window[key]
    graph.erase()
    graph.draw_circle((0, 0), 200, fill_color=color, line_color=color1)

def LEDIndicator1(key=None, radius=150):
    return sg.Graph(canvas_size=(radius, radius),
             graph_bottom_left=(-radius, -radius),
             graph_top_right=(radius, radius),
             pad=(0, 0), key=key)




layout = [[[sg.Text('             '),
            sg.Frame('GRIPPER CONTROL',[[sg.Button('Gripper set'),sg.Text(''),sg.Button('GRIP')]]),

             ],[LEDIndicator('grip ok')],
             sg.Text('                        '),sg.Text('GRIP Status')]]
gui = sg.Window(title="Robotic gripper  haptic feedback test", layout=layout,size=(300, 400), finalize=True,resizable=True)
event1=0
n = 0
while True:

    (event, values) = gui.read(timeout=0)
    SetLED(gui, 'grip ok','blue' if n == 1 else 'red', 'white' )
    if event ==  'Gripper set':
        ser = gri_set(PORT='COM3')
    if event ==  'GRIP':
        puredata = Get_Sensor_values_degital('COM1')
        puredata1 = Get_Sensor_values_degital('COM2')
        mean = sum(puredata)/8 + sum(puredata1)/8
        n = grip_op_dynamic_w_blocker(ser,220,250,250,0.05,1, mean,1)
    if event == sg.WIN_CLOSED:
        sys.exit()