import pyperclip
import time
import keyboard
import subprocess

while True:
    flag = False
    title = input('セクション名を入力してください：')

    title = title.replace(' ', '_')
    title = title + '.txt'

    subprocess.Popen(['code', title], shell=True)

    while True:
        f = open(title, 'a', encoding='UTF-8')
        originalText = pyperclip.paste()
        while True:
            currentText = pyperclip.paste()
            if currentText != originalText:
                currentText = currentText.replace('\r\n', ' ')
                f.write(currentText)
                f.close()
                break
            time.sleep(0.01)
            if keyboard.is_pressed('enter'):
            # if True:
                f.write('\n')
                f.close
                time.sleep(0.5)
                break
            if keyboard.is_pressed('escape'):
                f.close
                flag = True
                break
        if flag == True:
            break

    ans = input('さらにコピーを続けますか？(y/n)：')
    if ans == 'n':
        break