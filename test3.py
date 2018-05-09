import numpy as np
import cv2
import time

capture = cv2.VideoCapture('testvid2.mp4')
#frame = cv2.imread('road.jpg',cv2.IMREAD_COLOR)

def draw_lines(img, lines):
    try:
        for line in lines:
            coords = line[0]
            cv2.line(img, (coords[0],coords[1]), (coords[2],coords[3]), [255,255,255], 2)
    except:
        pass

def roi(img, vertices):
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, vertices, 255)
    masked = cv2.bitwise_and(img,mask)
    return masked
    
def process_img(original_image):
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    processed_img = cv2.Canny(processed_img, threshold1=200, threshold2=300)
    processed_img = cv2.GaussianBlur(processed_img, (5,5), 0)
    vertices = np.array([[10,315],[10,300], [250,230], [350,230], [500,270], [460,315]], np.int32)
    processed_img = roi(processed_img, [vertices])


    lines = cv2.HoughLinesP(processed_img, 1, np.pi/180, 180, np.array([]), 5, 5)
    draw_lines(processed_img,lines)    
    return processed_img

def video_record(): 
    last_time = time.time()
    while(True):
        d, frame = capture.read()
        printscreen =  np.array(frame, dtype = 'uint8')
        new_screen = process_img(printscreen)
        
        print('loop took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        cv2.imshow('window',cv2.cvtColor(printscreen, cv2.COLOR_BGR2GRAY))
        cv2.imshow('windows2', new_screen)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

video_record()
