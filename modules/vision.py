import cv2
import numpy as np
import math


def get_center(contour, use_moments=False):
    """Get contour center. Moments = precise, bounding box = faster."""
    if use_moments:
        M = cv2.moments(contour)
        if M["m00"] == 0:  # avoid division by zero
            return None
        cx = int(M["m10"] / M["m00"])
        cy = int(M["m01"] / M["m00"])
        return (cx, cy)
    else:
        x, y, w, h = cv2.boundingRect(contour)
        return (x + w // 2, y + h // 2)


def euclidean_distance(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])


def process(output_img, area_thresh=100000.0, use_moments=False):
    """Find target contour and draw path visualization."""
    gray = cv2.cvtColor(output_img, cv2.COLOR_BGR2GRAY)

    # OpenCV 4.x returns (contours, hierarchy)
    contours, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Center of image
    centerpoint = (output_img.shape[1] // 2, output_img.shape[0] // 2)

    # Filter contours by area
    filtered_contours = [c for c in contours if cv2.contourArea(c) > area_thresh]

    target = (centerpoint, 0)

    if filtered_contours:
        # Compute centers + distances once
        centers = [get_center(c, use_moments) for c in filtered_contours]
        centers = [c for c in centers if c is not None]  # drop invalid

        if centers:
            # Vectorized distance calculation
            deltas = np.array([euclidean_distance(c, centerpoint) for c in centers])
            min_idx = np.argmin(deltas)
            target = (centers[min_idx], deltas[min_idx])

    else:
        cv2.putText(output_img, "NO TARGET", (50, 50), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 0, 255), 3, cv2.LINE_AA)


    cv2.circle(output_img, target[0], 20, (0, 0, 255), -1)  # target
    cv2.putText(output_img, f"{target[1]:.1f}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 0, 255), 3, cv2.LINE_AA)
    cv2.line(output_img, centerpoint, target[0], (255, 0, 0), 10)  # path
    cv2.circle(output_img, centerpoint, 20, (0, 255, 0), -1)  # center
    cv2.drawContours(output_img, filtered_contours, -1, (255, 255, 255), 3)  # contours

    return output_img
