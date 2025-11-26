import pyzed.sl as sl 
import cv2
import time 
import logging 


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
    init_params.coordinate_units = sl.UNIT.METER
    init_params.depth_minimum_distance = min_range
    init_params.depth_maximum_distance = max_range
    
    status = self.depth_camera.open(init_params)
    
    if status != sl.ERROR_CODE.SUCCESS:
        raise RuntimeError(f'ZED camera failed to open: {status}')
    
    
    self.runtime_params = sl.RuntimeParameters()
    self.runtime_params.sensing_code = sl.SENSING_MODE.STANDARD
    
    
    def grab_frame(self) -> tuple | None:
        
        
        
        if self.depth_camera.grab(self.runtime_params) == sl.ERROR_CODE.SUCCESS:
            self.depth_camera.retrieve_image(self.rgb_mat, sl.VIEW.LEFT)
            self.depth_camera.retrieve_measure(self.depth_mat, sl.MEASURE.DEPTH)
            
            
            rgb = self.rgb_mat.get_data()
            depth = self.depth_mat.get_data()
            
            
            return rgb, depth 
        
    def close(self) -> None:
        self.depth_camera.close()