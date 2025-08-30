import struct
import serial
import time

class TFLuna:
    FRAME_HEADER = 0x59
    DISTANCE_FRAME_SIZE = 9
    
    
    
    def __init__(self, port: str, baudrate: int = 115200, timeout: float = 0.1):
        self.ser = serial.Serial(port=port,baudrate=baudrate,timeout=timeout)
        
    def close(self):
        if self.ser.is_open:
            self.ser.close()
            
            
    def is_connected(self)-> bool:
        return self.ser.is_open
    
    
    def _read_frame(self):
        """
        Reads a full 9-byte frame from TF-Luna.
        Returns raw bytes or None if timeout.
        """
        data = self.ser.read(self.DISTANCE_FRAME_SIZE)
        if len(data) != self.DISTANCE_FRAME_SIZE:
            return None
        if data[0] != self.FRAME_HEADER or data[1] != self.FRAME_HEADER:
            return None

        # Checksum validation
        checksum = sum(data[0:8]) & 0xFF
        if checksum != data[8]:
            return None
        return data


    def read_measurement(self):
        """
        Reads one distance + strength + temperature measurement.
        Returns dict {distance_m, strength, temperature_c}
        or None if no valid frame.
        """
        frame = self._read_frame()
        if frame is None:
            return None

        distance = frame[2] + (frame[3] << 8)   # cm
        strength = frame[4] + (frame[5] << 8)
        temperature = (frame[6] + (frame[7] << 8)) / 8.0 - 256.0

        return {
            "distance_m": distance / 100.0,   # meters
            "strength": strength,
            "temperature_c": temperature
        }