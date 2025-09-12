import cv2  
import math 



def get_center(contour)->None:
    M = cv2.moments(contour)
    if M['m00'] == 0:
        return None 
    cx = int(M['m10']/ M['m00'])
    cy = int(M['m01']/ M['m00'])
    
    return (cx, cy)

def euclidean_distance():...
