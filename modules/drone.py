import time  
import logging
from pymavlink import mavutil
from dronekit import VehicleMode, connect

logging.basicConfig(level=logging.INFO)

class DroneAPI:
    def __init__(self, connection_string, baudrate=57600) -> None:
        self.logger = logging.getLogger("DroneAPI")
        self.vehice = connect(connection_string, wait_ready=True, baud=baudrate)
        self.logger.info('Connected to drone')
        
    def disconnection(self):
        self.vehice.close()
        self.logger.info('Disconnection to Drone')
        
        
    def get_version(self):
        return self.vehice.version
    
    
    def get_location(self):
        return  self.vehice.location.global_frame
    
    
    def get_altitude(self):
        return self.vehice.location.global_relative_frame.alt 
    
    
    
    def get_velocity(self):
        return  self.vehice.velocity
    
    
    def get_battery(self):
        return self.vehice.battery
    
    
    def get_mode(self):
        return self.vehice.mode
    
    
    def arm_and_takeoff(self, target_altitude, groundspeed=3):
        self.logger.info("Arming and taking off...")
        self.vehice.mode = VehicleMode("GUIDED")
        self.vehice.groundspeed = groundspeed
        
        
        for _ in range(30):
            if self.vehice.is_armable:
                break
            time.sleep(1)
        else:
            raise TimeoutError('Drone not armable')
        
        self.vehice.armed = True
        
        while not self.vehice.armed:
            time.sleep(1)
            
        self.vehice.simple_takeoff(target_altitude)
        
        
        while True:
            alt = self.get_altitude()
            self.logger.info(f"Altitude:{alt:.2f}m")
            if alt >= target_altitude * 0.95:
                self.logger.info('Reached target altitude')
                break
            time.sleep(1)
            
            
            
    def len(self):
        self.logger.info('Landing...')
        self.vehice.mode = VehicleMode("LAND")
        
        
    def rtl(self):
        self.logger.info('Returning to launch (no obstacle avoidance!)')
        self.vehice.mode = VehicleMode('RTL')
        
        
    def send_yaw_command(self, heading, speed=30):
        direction = 1 if heading >= 0 else -1
        heading = abs(heading)

        msg = self.vehice.message_factory.command_long_encode(
            0, 0,
            mavutil.mavlink.MAV_CMD_CONDITION_YAW,
            0,
            heading, speed, direction, 1,
            0, 0, 0
        )
        self.vehice.send_mavlink(msg)
        self.logger.info(f"Yaw command: {heading} deg, dir={direction}")
