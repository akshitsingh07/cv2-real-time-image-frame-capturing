import cv2
import random
vidcap = cv2.VideoCapture(0)
directory = r'__Path__'
if vidcap.isOpened():
    ret, frame = vidcap.read()
    if ret:
        while (True):
            cv2.imshow("Frame", frame)
            if cv2.waitKey(1) & 0xFF == ord('s'):
                cv2.imwrite(directory + 'real_time_'+f'{random.randint(0,999999)}'+'.jpg', frame)
                print("Image saved to the directory.")
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    else:
        print("Error : Failed to capture frame")
else:
    print("Cannot open camera")