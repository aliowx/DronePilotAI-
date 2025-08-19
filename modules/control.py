import logging
import time 
from simple_pid import PID

logger = logging.getLogger(__name__) 




class DroneController:
    def __init__(self,
        use_pid_yaw=True,
        use_pid_roll=False,
        max_speed=4,
        max_yaw=15,
        flight_altitude=4,
        control_freq=20
        ):
        """
        High-level drone controller using PID control for yaw and roll.

        Args:
            use_pid_yaw (bool): Enable PID for yaw control.
            use_pid_roll (bool): Enable PID for roll control.
            max_speed (float): Max roll speed (m/s).
            max_yaw (float): Max yaw rate (deg/s).
            flight_altitude (float): Target altitude (meters).
            control_freq (float): Control loop frequency (Hz).
        """
        self.use_pid_yaw = use_pid_yaw
        self.use_pid_roll = use_pid_roll
        self.max_speed = max_speed
        self.max_yaw = max_yaw
        self.flight_altitude = flight_altitude
        self.control_period = 1.0 / control_freq
        
        
        