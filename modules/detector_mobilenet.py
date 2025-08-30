import cv2 
import numpy as np 
import jetson.inference
import jetson.utils



class JetsonPersonDetector:
    def __init__(self, 
                 model="ssd-mobilenet-v2", 
                 camera_uri="csi://0", 
                 filter_classes=[1]):  
        """
        :param model: name of detection model
        :param camera_uri: source for video (csi://0, /dev/video0, file://, rtsp://)
        :param filter_classes: list of class IDs to keep (1 = person in COCO)
        """
        self.net = jetson.inference.detectNet(model)
        self.camera = jetson.utils.videoSource(camera_uri)
        self.filter_classes = set(filter_classes)
        
        
    def get_image_size(self):
        return self.camera.GetWidth(), self.camera.GetWidth()
    
    def close(self):
        self.camera.Close()
        
        
        
    def get_detections(self, return_frame=True):
        """
        Capture a frame, run detection, and return filtered results.
        :return: (detections, fps, frame_bgr)
        """
        img = self.camera.Capture(timeout=1000)  # ms
        if img is None:
            return [], 0.0, None

        detections = self.net.Detect(img)
        filtered = []
        for det in detections:
            if det.ClassID in self.filter_classes:
                filtered.append({
                    "class_id": det.ClassID,
                    "confidence": det.Confidence,
                    "bbox": (det.Left, det.Top, det.Right, det.Bottom)
                })

        fps = self.net.GetNetworkFPS()

        frame_bgr = None
        if return_frame:
            frame_bgr = cv2.cvtColor(jetson.utils.cudaToNumpy(img), cv2.COLOR_RGBA2BGR)

        return filtered, fps, frame_bgr
        
        
        