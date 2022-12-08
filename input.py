import pyperclip
import time
import keyboard

title = input('セクション名を入力してください：')

title = title.replace(' ', '_')
title = title + '.txt'
# f = open(title, 'w', encoding='UTF-8')

flag = False

while True:
    f = open(title, 'a', encoding='UTF-8')
    originalText = pyperclip.paste()
    while True:
        currentText = pyperclip.paste()
        if currentText != originalText:
            currentText = currentText.replace('\r\n', ' ') + '\n'
            f.write(currentText)
            f.close()
            break
        time.sleep(0.01)
        if keyboard.is_pressed('escape'):
            f.close
            flag = True
            break
    
    if flag == True:
        break

