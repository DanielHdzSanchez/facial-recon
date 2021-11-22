import capture_faces
import training
import facial_recon
import os


def start():
    response = 1
    while response in range(1, 3):
        print("""
        Facial Recognition System by Dan
        1. Train
        2. Test video
        Press another number to exit.
        """)
        try:
            response = int(input("Enter your choice: "))
        except ValueError:
            print("\nPlease enter a number.")
            continue
        if response == 1:
            another_person = True
            while another_person:
                capture_faces.capture(input('Who are you identifying? '))
                another_person = input('Another person? (y/n) ') == 'y'
            training.train()
        if response == 2:
            old = ' \ '.replace(' ', '')
            new = ' / '.replace(' ', '')
            curr_dir = os.getcwd().replace(old, new).replace('c:', 'C:')
            data_path = curr_dir+'/data'
            people_list = os.listdir(data_path)
            persons = [person for person in people_list]
            ix = 0
            for i, person in enumerate(persons):
                print(f'{i}. {person}')
            try:
                ix = int(input('Which video do you want to test? '))
                facial_recon.start(persons[ix])
            except Exception as e:
                print()
                print(f'Error, please try again.')


if __name__ == "__main__":
    start()
