import pyzed.sl as sl 
import cv2
import time 



class ZEDWrapper:
    def __init__(self, performance_mode: bool = True, min_range: float = 1.0, max_range: float = 6.0, resolution:sl.RESOLUTION = sl.RESOLUTION.HD720) -> None:
        
        self.performance_mode = performance_mode
        self.min_range = min_range
        self.max_range = max_range
        self.depth_camera = sl.Camera()
        self.depth_mat = sl.Mat()
        self.rgb_mat = sl.Mat()
        
        
    init_params = sl.InitParameters()
    init_params.camera_resolution = resolution 
    init_params.camera_fps = fps
    init_params.depth_mode = (
        sl.DEPTH_MODE.PERFORMANCE if performance_mode else sl.DEPTH_MODE.ULTRA
    )
    
