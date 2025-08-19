import logging
import time 
from simple_pid import PID



USE_PID_YAW = True
USE_PID_ROLL = False


MAX_SPEED = 4
MAX_YAW = 15


P_YAW = 0.02
I_YAW = 0
D_YAW = 0


P_ROLL = 0.22
I_ROLL = 0
D_ROLL = 0

control_loop_active = True
pidYaw = None
pidRoll = None
movementYawAngle = 0
movementRollAngle = 0
inputValueYaw = 0
inputValueVelocityX = 0
control_loop_active = True 
flight_altitude = 4

debug_yaw = None
debug_velocity = None