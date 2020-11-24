
import PySimpleGUI as sg

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


def show_gui():

    layout = [[sg.Text("Hello World")], [sg.Button("OK")]]

    # Create the window
    window = sg.Window("Demo", layout)

    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == "OK" or event == sg.WIN_CLOSED:
            break

    window.close()


if __name__ == '__main__':
    #num = 19.5
    #print_me(num)
    show_gui()

