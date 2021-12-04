import cv2
import os
import imutils

FRAME_WIDTH = 650
FACE_SIZE = 200
TOTAL_PHOTOS = 300


def capture(name):
    old = ' \ '.replace(' ', '')
    new = ' / '.replace(' ', '')
    curr_dir = os.getcwd().replace(old, new).replace('c:', 'C:')
    data_path = curr_dir+'/data'
    person_path = data_path + '/' + name

    if not os.path.exists(curr_dir+f'/{name}.mp4'):
        print('No video found, verify and try again.')
        return

    cap = cv2.VideoCapture(f'{name}.mp4')

    if not os.path.exists(person_path):
        print('New folder for: ' + name)
        os.makedirs(person_path)
    else:
        for file in os.scandir(person_path):
            os.remove(file.path)

    face_classification = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    count = 0

    while True:
        ret, frame = cap.read()
        # ret, if it is false, no frames are being read
        # frame, the frame that is being read
        # if there are no frames, capturing stops
        if ret == False:
            break
        # resizing the frames
        frame = imutils.resize(frame, FRAME_WIDTH)
        # grayscale conversion makes it easier to detect faces
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        aux_frame = frame.copy()
        # gray, the frame in grayscale
        # scaleFactor = 1.3, how much the image size is reduced
        # 1.3 means 30% reduction, it is faster
        # 1.05, the minimum possible reduction, it is slower
        # minNeighbors = 5, how many neighbors each candidate rectangle should have to retain it, 3~6 is recommended
        faces = face_classification.detectMultiScale(gray, 1.3, 5)
        # faces, the coordinates of the faces

        for (x, y, w, h) in faces:
            # x, y are the top left coordinates of the rectangle
            # w, h are the width and height of the rectangle
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            # drawing a rectangle around the face
            # (x,y) start point, (x+w, y+h) end point
            # (0,255,0) is the color of the rectangle
            # 2 is the thickness of the line
            face = aux_frame[y:y+h, x:x+w]
            face = cv2.resize(face, (FACE_SIZE, FACE_SIZE),
                              interpolation=cv2.INTER_CUBIC)
            cv2.imwrite(person_path + '/face_{}.jpg'.format(count), face)
            count += 1
        cv2.imshow('Obtaining faces...', frame)

        k = cv2.waitKey(1)
        if k == 27 or count >= TOTAL_PHOTOS:
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    capture()
