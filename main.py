import win32com.client as comclt
import win32gui as wgui
import win32process as wproc
import win32api as wapi
import pyautogui
import time 
import random 
import CharacterController 

def main(*argv):
    print("AI Game Solver for Binding of Isaac")
    if not argv:
        window_name = "Binding of Isaac: Repentance"
    else:
        window_name = argv[0]

    handle = wgui.FindWindow(None, window_name)
    print("Window `{0:s}` handle: 0x{1:016X}".format(window_name, handle))
    if not handle:
        print("Invalid window handle")
        return
    remote_thread, _ = wproc.GetWindowThreadProcessId(handle)
    wproc.AttachThreadInput(wapi.GetCurrentThreadId(), remote_thread, True)
    prev_handle = wgui.SetFocus(handle)
    
    pyautogui.keyDown('esc')
    time.sleep(0.01)
    pyautogui.keyUp('esc')
    
    player = CharacterController.CharacterController()
    
    while(True):
        action = random.randint(0,13)
        if action == 0:
            player.moveNorth()
        elif action == 1:
            player.moveEast()
        elif action == 2:
            player.moveWest()
        elif action == 3:
            player.moveSouth()
        elif action == 4:
            player.moveNorthEast
        elif action == 5:
            player.moveNorthWest()
        elif action == 6:
            player.moveSouthEast()
        elif action == 7:
            player.moveSouthWest()
        elif action == 8:
            player.shootEast()
        elif action == 9:
            player.shootNorth()
        elif action == 10:
            player.shootSouth()
        elif action == 11:
            player.shootWest()
        elif action == 12:
            player.useBomb()
        elif action == 13:
            player.useItem()
        
if __name__ == '__main__':
    main()