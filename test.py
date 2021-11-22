import os


def start():
    old = ' \ '.replace(' ', '')
    new = ' / '.replace(' ', '')
    dir = os.getcwd().replace(old, new).replace('c:', 'C:')
    print(dir+'/data')


if __name__ == '__main__':
    start()
