import pyzed.sl as sl 
import cv2
import time 



class ZEDWrapper:
    def __init__(self,performance_mode: bool = True, min_range: float = 1.0, max_range: float = 6.0) -> None:
        self.depth_camera = sl.Camera()
        self.depth_mat = sl.Mat()
        self.rgb_mat = sl.Mat()
        
        
    