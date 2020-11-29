import time, pyautogui, webbrowser, datetime
import pytesseract as tess
from PIL import Image
from insertjadwal import kelas
from pathToThings import pathToTesseract, pathToImage


tess.pytesseract.tesseract_cmd = pathToTesseract
now = datetime.datetime.now()

class Main:
    def __init__(self):
        print('Welcome to the program')
        time.sleep(1)
        self.start()
        print(now)

    def checkTime(self):
        return 1

    def start(self):
        checkTimeNow = self.checkTime()
        if checkTimeNow == 1:
            print('starting your class, {}, now.'.format(kelas['kelas']))
            print('I will open the link you put...')
            # webbrowser.open(kelas['link'])
            time.sleep(1)
            while True:
                screenshot = pyautogui.screenshot()
                screenshot.save(pathToImage)
                img = Image.open(pathToImage)
                text = tess.image_to_string(img)
                if('Enter your name' in text):
                    print('ok.')
                    time.sleep(2)
                    pyautogui.typewrite("Muhammad Hadi")
                time.sleep(5)  
        else:
            pass


if __name__ == "__main__":
    main = Main()
