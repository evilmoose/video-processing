import cv2
import os

vid = cv2.VideoCapture("C:/Users/ronni/Portfolio/Video-Processing/videos/I_dont_know_if_I_like_the_BAS-B.mp4")
currentframe = 0

if not os.path.exists('data'):
    os.makedirs('data')

while True:
    success, frame = vid.read()

    cv2.imshow("Output", frame)
    cv2.imwrite('./data/' + str(currentframe) + '.jpg', frame)
    currentframe += 1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()