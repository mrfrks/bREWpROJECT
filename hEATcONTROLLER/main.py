
#import PySimpleGUI as sg

def print_me(num):

    with open('input.txt', 'a') as f:
        f.truncate(0)
        while(1):
            f.write('%lf,\n' % (num + 0.5))
            f.write('%lf,\n' % (num + 0.85))
            if(num + 1 < 100):
                num = num + 1
            else:
                break;

if __name__ == '__main__':
    num = 19.5
    print_me(num)
    #sg.Window(title="Hello World", layout=[[]], margins=(100, 50)).read()

