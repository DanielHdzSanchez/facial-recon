import cv2
import numpy as np
import os


def train():
    old = ' \ '.replace(' ', '')
    new = ' / '.replace(' ', '')
    curr_dir = os.getcwd().replace(old, new).replace('c:', 'C:')
    data_path = curr_dir+'/data'
    people_list = os.listdir(data_path)
    print('People: ', people_list)
    labels = []
    faces_data = []
    label = 0
    for i, person in enumerate(people_list):
        person_path = data_path + '/' + person
        print('Reading images...')

        for file in os.listdir(person_path):
            if file.endswith('.jpg'):
                print('Face: ' + person + '/' + file)
                labels.append(label)
                faces_data.append(cv2.imread(person_path + '/' + file, 0))
                image = cv2.imread(person_path + '/' + file, 0)
                #cv2.imshow('image', image)
                # cv2.waitKey(10)
        label += 1
    # cv2.destroyAllWindows()
    # print('Labels: ', labels)
    # print('Label 0: ', np.count_nonzero(np.array(labels) == 0))
    # print('Label 1: ', np.count_nonzero(np.array(labels) == 1))

    # Eigen Faces training
    face_recognizer = cv2.face.EigenFaceRecognizer_create()
    print('Training...')
    face_recognizer.train(faces_data, np.array(labels))
    print('Training complete.')

    face_recognizer.write('EigenFacesModel.xml')
    print('Model saved.')


if __name__ == '__main__':
    train()
