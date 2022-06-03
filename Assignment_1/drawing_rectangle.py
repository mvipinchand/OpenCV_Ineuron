import cv2
image = cv2.imread(filename='Test_image.jpg', flags=1)

start_point = (100,100) #left top point of rectangle
end_point = (1000,500) #right botton point
color = (0,0,255)
thickness = 10
cv2.rectangle(img=image,pt1=start_point,pt2=end_point,color=color,thickness=thickness)


cv2.imshow('my',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
