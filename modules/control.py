import logging
import time 
from simple_pid import PID

logger = logging.getLogger(__name__) 

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



def configure_PID(control):
   
    global pidRoll, pidYaw
    
    """Creates PID """
    
    logger.info('Configuring control')
    
    if control == "PID":
        pidYaw = PID(P_YAW, I_YAW, D_YAW, setpoint=0)       # I = 0.001
        pidYaw.output_limits = (-MAX_YAW, MAX_YAW)          # PID Range
        pidRoll = PID(P_ROLL, I_ROLL, D_ROLL, setpoint=0)   # I = 0.001
        pidRoll.output_limits = (-MAX_SPEED, MAX_SPEED)     # PID Range
        
        logger.info('Configuring PID')
        
    else:
        pidYaw = PID(P_YAW, 0, 0, setpoint=0)               # I = 0.001
        pidYaw.output_limits = (-MAX_YAW, MAX_YAW)          # PID Range
        pidRoll = PID(P_ROLL, 0, 0, setpoint=0)             # I = 0.001
        pidRoll.output_limits = (-MAX_SPEED, MAX_SPEED)     # PID Range
        
        logger.info('Configuring PID')
        
        
def connect_drone(drone_location):...




