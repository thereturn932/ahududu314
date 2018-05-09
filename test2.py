import cv2

capture=cv.VideoCapture(0)

while(1):
    ret, frame = capture.read()

    grayscale(frame)
    canny(frame, )

def canny(img, low_threshold, high_threshold):
    """Applies the Canny transform"""
    return cv2.Canny(img, low_threshold, high_threshold)

def grayscale(img):
    """Applies the Grayscale transform
    This will return an image with only one color channel
    but NOTE: to see the returned image as grayscale
    you should call plt.imshow(gray, cmap='gray')"""
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def region_of_interest(img, vertices):
    """
    Applies an image mask.
    
    Only keeps the region of the image defined by the polygon
    formed from `vertices`. The rest of the image is set to black.
    """
    #defining a blank mask to start with
    mask = np.zeros_like(img)   
    
    #defining a 3 channel or 1 channel color to fill the mask with depending on the input image
    if len(img.shape) > 2:
        channel_count = img.shape[2]  # i.e. 3 or 4 depending on your image
        ignore_mask_color = (255,) * channel_count
    else:
        ignore_mask_color = 255
        
    #filling pixels inside the polygon defined by "vertices" with the fill color    
    cv2.fillPoly(mask, vertices, ignore_mask_color)
    
    #returning the image only where mask pixels are nonzero
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image

def draw_lines(img, lines, color=[255, 0, 0], thickness=10):
    imshape = img.shape
    left_x1 = []
    left_x2 = []
    right_x1 = []
    right_x2 = [] 
    y_min = img.shape[0]
    y_max = int(img.shape[0]*0.611)
    for line in lines:
        for x1,y1,x2,y2 in line:
            if ((y2-y1)/(x2-x1)) < 0:
                mc = np.polyfit([x1, x2], [y1, y2], 1)
                left_x1.append(np.int(np.float((y_min - mc[1]))/np.float(mc[0])))
                left_x2.append(np.int(np.float((y_max - mc[1]))/np.float(mc[0])))
#           cv2.line(img, (xone, imshape[0]), (xtwo, 330), color, thickness)
            elif ((y2-y1)/(x2-x1)) > 0:
                mc = np.polyfit([x1, x2], [y1, y2], 1)
                right_x1.append(np.int(np.float((y_min - mc[1]))/np.float(mc[0])))
                right_x2.append(np.int(np.float((y_max - mc[1]))/np.float(mc[0])))
#           cv2.line(img, (xone, imshape[0]), (xtwo, 330), color, thickness)
    l_avg_x1 = np.int(np.nanmean(left_x1))
    l_avg_x2 = np.int(np.nanmean(left_x2))
    r_avg_x1 = np.int(np.nanmean(right_x1))
    r_avg_x2 = np.int(np.nanmean(right_x2))
#     print([l_avg_x1, l_avg_x2, r_avg_x1, r_avg_x2])
    cv2.line(img, (l_avg_x1, y_min), (l_avg_x2, y_max), color, thickness)
    cv2.line(img, (r_avg_x1, y_min), (r_avg_x2, y_max), color, thickness)    

def hough_lines(img, rho, theta, threshold, min_line_len, max_line_gap):
    """
    `img` should be the output of a Canny transform.
        
    Returns an image with hough lines drawn.
    """
    lines = cv2.HoughLinesP(img, rho, theta, threshold, np.array([]), minLineLength=min_line_len, maxLineGap=max_line_gap)
    line_img = np.zeros((*img.shape, 3), dtype=np.uint8)
    draw_lines(line_img, lines)
    return line_img
