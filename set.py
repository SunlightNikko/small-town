import json
import keyboard
import pyautogui

with open("calibration.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print("先開16:9畫布，大小不要動\n將滑鼠移到畫布左上角，點一下確定可以畫上一格像素，將滑鼠盡量移在該像素的中間後 按F6")
keyboard.wait("F6")
x1, y1 = pyautogui.position()
data["169_x1"] = x1
data["169_y1"] = y1
print(f"左上角：{x1}, {y1}\n")
print("將滑鼠移到畫布右下角，點一下確定可以畫上一格像素，將滑鼠盡量移在該像素的中間後 按F6")
keyboard.wait("F6")
x1, y1 = pyautogui.position()
data["169_x2"] = x1
data["169_y2"] = y1
print(f"右下角：{x1}, {y1}\n")

print("再開4:3畫布，大小不要動\n將滑鼠移到畫布左上角，點一下確定可以畫上一格像素，將滑鼠盡量移在該像素的中間後 按F6")
keyboard.wait("F6")
x1, y1 = pyautogui.position()
data["43_x1"] = x1
data["43_y1"] = y1
print(f"左上角：{x1}, {y1}\n")
print("將滑鼠移到畫布右下角，點一下確定可以畫上一格像素，將滑鼠盡量移在該像素的中間後 按F6")
keyboard.wait("F6")
x1, y1 = pyautogui.position()
data["43_x2"] = x1
data["43_y2"] = y1
print(f"右下角：{x1}, {y1}\n")

print("再開1:1畫布，大小不要動\n將滑鼠移到畫布左上角，點一下確定可以畫上一格像素，將滑鼠盡量移在該像素的中間後 按F6")
keyboard.wait("F6")
x1, y1 = pyautogui.position()
data["11_x1"] = x1
data["11_y1"] = y1
print(f"左上角：{x1}, {y1}\n")
print("將滑鼠移到畫布右下角，點一下確定可以畫上一格像素，將滑鼠盡量移在該像素的中間後 按F6")
keyboard.wait("F6")
x1, y1 = pyautogui.position()
data["11_x2"] = x1
data["11_y2"] = y1
print(f"右下角：{x1}, {y1}\n")

print("再開3:4畫布，大小不要動\n將滑鼠移到畫布左上角，點一下確定可以畫上一格像素，將滑鼠盡量移在該像素的中間後 按F6")
keyboard.wait("F6")
x1, y1 = pyautogui.position()
data["34_x1"] = x1
data["34_y1"] = y1
print(f"左上角：{x1}, {y1}\n")
print("將滑鼠移到畫布右下角，點一下確定可以畫上一格像素，將滑鼠盡量移在該像素的中間後 按F6")
keyboard.wait("F6")
x1, y1 = pyautogui.position()
data["34_x2"] = x1
data["34_y2"] = y1
print(f"右下角：{x1}, {y1}\n")

print("再開9:16畫布，大小不要動\n將滑鼠移到畫布左上角，點一下確定可以畫上一格像素，將滑鼠盡量移在該像素的中間後 按F6")
keyboard.wait("F6")
x1, y1 = pyautogui.position()
data["916_x1"] = x1
data["916_y1"] = y1
print(f"左上角：{x1}, {y1}\n")
print("將滑鼠移到畫布右下角，點一下確定可以畫上一格像素，將滑鼠盡量移在該像素的中間後 按F6")
keyboard.wait("F6")
x1, y1 = pyautogui.position()
data["916_x2"] = x1
data["916_y2"] = y1
print(f"右下角：{x1}, {y1}\n\n\n")

print("將滑鼠移到 切換左顏色(圖)，將滑鼠盡量移在中間後 按F6")
keyboard.wait("F6")
x1, y1 = pyautogui.position()
data["L_color_x"] = x1
data["L_color_y"] = y1
print(f"切換左顏色：{x1}, {y1}\n")

print("將滑鼠移到 切換右顏色(圖)，將滑鼠盡量移在中間後 按F6")
keyboard.wait("F6")
x1, y1 = pyautogui.position()
data["R_color_x"] = x1
data["R_color_y"] = y1
print(f"切換右顏色：{x1}, {y1}\n")

print("將滑鼠移到 1(圖)，將滑鼠盡量移在中間後 按F6")
keyboard.wait("F6")
x1, y1 = pyautogui.position()
data["1_x"] = x1
data["1_y"] = y1
print(f"切換 1：{x1}, {y1}\n")

print("將滑鼠移到 2(圖)，將滑鼠盡量移在中間後 按F6")
keyboard.wait("F6")
x1, y1 = pyautogui.position()
data["2_x"] = x1
data["2_y"] = y1
print(f"切換 2：{x1}, {y1}\n")

print("將滑鼠移到 3(圖)，將滑鼠盡量移在中間後 按F6")
keyboard.wait("F6")
x1, y1 = pyautogui.position()
data["3_x"] = x1
data["3_y"] = y1
print(f"切換 3：{x1}, {y1}\n")

print("將滑鼠移到 4(圖)，將滑鼠盡量移在中間後 按F6")
keyboard.wait("F6")
x1, y1 = pyautogui.position()
data["4_x"] = x1
data["4_y"] = y1
print(f"切換 4：{x1}, {y1}\n")

print("將滑鼠移到 5(圖)，將滑鼠盡量移在中間後 按F6")
keyboard.wait("F6")
x1, y1 = pyautogui.position()
data["5_x"] = x1
data["5_y"] = y1
print(f"切換 5：{x1}, {y1}\n")

print("將滑鼠移到 6(圖)，將滑鼠盡量移在中間後 按F6")
keyboard.wait("F6")
x1, y1 = pyautogui.position()
data["6_x"] = x1
data["6_y"] = y1
print(f"切換 6：{x1}, {y1}\n")

print("將滑鼠移到 7(圖)，將滑鼠盡量移在中間後 按F6")
keyboard.wait("F6")
x1, y1 = pyautogui.position()
data["7_x"] = x1
data["7_y"] = y1
print(f"切換 7：{x1}, {y1}\n")

print("將滑鼠移到 8(圖)，將滑鼠盡量移在中間後 按F6")
keyboard.wait("F6")
x1, y1 = pyautogui.position()
data["8_x"] = x1
data["8_y"] = y1
print(f"切換 8：{x1}, {y1}\n")

print("將滑鼠移到 9(圖)，將滑鼠盡量移在中間後 按F6")
keyboard.wait("F6")
x1, y1 = pyautogui.position()
data["9_x"] = x1
data["9_y"] = y1
print(f"切換 9：{x1}, {y1}\n")

print("將滑鼠移到 10(圖)，將滑鼠盡量移在中間後 按F6")
keyboard.wait("F6")
x1, y1 = pyautogui.position()
data["10_x"] = x1
data["10_y"] = y1
print(f"切換 10：{x1}, {y1}\n")

print("OK")

with open("calibration.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)