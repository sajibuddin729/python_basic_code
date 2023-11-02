import pyautogui
try:
    rows = int(input("Enter number: "))
    for i in range(rows):
        pyautogui.typewrite('#' * (i + 1))
        pyautogui.typewrite('\n')
except:
    print("Please enter a valid integer.")
