from mtcnn import MTCNN
import cv2
# img = cv2.cvtColor(cv2.imread("ivan.jpg"), cv2.COLOR_BGR2RGB)
detector = MTCNN()
def check_face(img):
	results = detector.detect_faces(img)
	for face in results:
		bounding_box = face['box']
		keypoints = face['keypoints']

		cv2.rectangle(img,
		              (bounding_box[0], bounding_box[1]),
		              (bounding_box[0]+bounding_box[2], bounding_box[1] + bounding_box[3]),
		              (0,155,255),
		              2)

		cv2.circle(img,(keypoints['left_eye']), 2, (0,155,255), 2)
		cv2.circle(img,(keypoints['right_eye']), 2, (0,155,255), 2)
		cv2.circle(img,(keypoints['nose']), 2, (0,155,255), 2)
		cv2.circle(img,(keypoints['mouth_left']), 2, (0,155,255), 2)
		cv2.circle(img,(keypoints['mouth_right']), 2, (0,155,255), 2)
	return img

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    frame = check_face(frame)

    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()