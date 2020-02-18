#!/usr/bin/env python
import serial
import rospy
import struct
from geometry_msgs.msg import Twist

def cmd_vel_cb(data):
    print(port)
    steer = float(data.angular.z)
    speed = float(data.linear.x)
    steer = int(steer * 15.0)
    speed = int(speed * 30.0)

    msg = '{:03d}{:03d}'.format(steer, speed)
    print(msg)
    port.write(msg)
    port.flush()

if __name__ == '__main__':
    rospy.init_node('motor_control', anonymous=True)

    rospy.Subscriber('/cmd_vel', Twist, cmd_vel_cb)

    port_name = rospy.get_param('~port_name', '/dev/ttyUSB0')
    baudrate = rospy.get_param('~baudrate', 115200)
    port = serial.Serial(port=port_name, baudrate=baudrate)
    
    print(port)
    rospy.spin()
    port.close()