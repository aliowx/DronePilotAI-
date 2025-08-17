import cv2

cams = []

def create_camera(csi_port): 
    cap = cv2.VideoCapture(f"nvarguscamerasrc sensor-id={csi_port} ! video/x-raw(memory:NVMM), width=1280, height=720, format=NV12, framerate=30/1 ! nvvidconv ! video/x-raw, format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink", cv2.CAP_GSTREAMER)
    cams.append(cap)

def get_image_size(camera_id):
    cap = cams[camera_id]
    return int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

def get_video(camera_id):
    ret, frame = cams[camera_id].read()
    if not ret:
        raise RuntimeError("Failed to capture frame")
    return frame

def close_cameras():
    for cam in cams:
        cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    create_camera(0)
    
    while True:
        img = get_video(0)
        cv2.imshow("camera", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    close_cameras()