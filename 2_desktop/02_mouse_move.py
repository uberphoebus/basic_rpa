import pyautogui 
# ㅇ너랴ㅐㅇ너래ㅑㅇ너랴ㅐ머 제안

size = pyautogui.size() # 현 화면의 스크린 사이즈(가로, 세로)

pyautogui.moveTo(200, 100, duration=0.5)  # 절대위치, 시간 동안
print(pyautogui.position()) # Point(x, y) # 현 위치 출력
pyautogui.moveTo(300, 200, duration=0.5)
print(pyautogui.position()) # Point(x, y)

pyautogui.move(100, 500, duration=0.5) # 상대위치
p = pyautogui.position()
print(p[0], p[1], p.x, p.y)
