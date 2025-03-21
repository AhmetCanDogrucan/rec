"""

"""
import win32api 
import win32con 
import time  

# aK SPRAY AYARI


RECOIL_X = -1 # YATAY DEGER
RECOIL_Y =3# dikey deger
DELAY = 30 # gecikme


#mp5 ateşleme
#RECOIL_X = 0 # YATAY DEGER
#RECOIL_Y =2# dikey deger
#DELAY = 30 # gecikme

#hlmg spray
#RECOIL_X = 1 # YATAY DEGER
#RECOIL_Y =2 # dikey deger
#DELAY = 30 # gecikme

#m2 spray
#RECOIL_X = -1 # YATAY DEGER
#RECOIL_Y =3 # dikey deger
#DELAY = 35 # gecikme

#lr-300
#RECOIL_X = 0 # YATAY DEGER
#RECOIL_Y =3 # dikey deger
#DELAY = 35 #


def mouse_move(x, y):
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, y, 0, 0)
    print(f'Move {x}, {y}')



def main():
    print('Start')

    while True:
      #f1 tuşuna basınca donguden cık
        if win32api.GetAsyncKeyState(win32con.VK_F1) < 0:
            break

        if win32api.GetAsyncKeyState(win32con.VK_LBUTTON) < 0:
            mouse_move(RECOIL_X, RECOIL_Y)

        time.sleep(DELAY / 1000)


    print('Exit')


# ana fonksyonu çalıştırma
if __name__ == '__main__':
    main()s
