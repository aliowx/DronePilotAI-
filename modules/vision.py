import cv2  
import math 



def get_center(contour)->None:
    M = cv2.moments(contour)
    if M['m00'] == 0:
        return None 
    cx = int(M['m10']/ M['m00'])
    cy = int(M['m01']/ M['m00'])
    
    return (cx, cy)

def euclidean_distance(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1]-p2[1])


def axis_delta(v1, v2):
    return v2 - v1



def point_in_rectangle(point, left, right, top, bottom):
    x, y = point
    return left < x < right and top < y < bottom


 
