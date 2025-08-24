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
    
       
    
    
     
        