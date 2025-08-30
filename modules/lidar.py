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
