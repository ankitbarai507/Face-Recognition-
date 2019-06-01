import os
import cv2


nm=input("enter name : ")
img_counter = 0
print('high')
os.chdir('imgdb/')
os.mkdir(nm)
os.chdir(nm)


cam = cv2.VideoCapture(0)

cv2.namedWindow("test")
while True:
    ret, frame = cam.read()
    cv2.imshow("test", frame)
    if not ret:
        break
    k = cv2.waitKey(1)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k == ord('t'):
        # SPACE pressed
        img_name = "opencv_frame_{}.jpg".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()