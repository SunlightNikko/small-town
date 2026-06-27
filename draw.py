import keyboard
import time
import pyautogui
from PIL import Image, ImageGrab
import json
import numpy as np
from collections import Counter
import tkinter as tk
from tkinter import filedialog

with open("colors copy.json", "r", encoding="utf-8") as f:
    name_to_rgb = json.load(f)

with open("colors.json", "r", encoding="utf-8") as f:
    name_rgb = json.load(f)

with open("calibration.json", "r", encoding="utf-8") as f:
    data = json.load(f)

paused = False

def toggle_pause():
    global paused
    paused = not paused
    print("⏸ 暫停" if paused else "▶ 繼續")

keyboard.add_hotkey("F8", toggle_pause)

def wait_if_paused():
    while paused:
        time.sleep(0.1)



size = input("畫布比例(169/43/11/34/916)：")



x1 = data[f"{size}_x1"]
y1 = data[f"{size}_y1"]
x2 = data[f"{size}_x2"]
y2 = data[f"{size}_y2"]



root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename(
    title="請選擇一張圖片",
    filetypes=[("圖片檔案", "*.png *.jpg *.jpeg *.bmp *.webp"), ("所有檔案", "*.*")]
)
if file_path:
    img = Image.open(file_path).convert("RGB")
    print(import_file := f"成功讀取檔案：{file_path}")
    w, h = img.size

    pixels = img.load()
    color_counter = Counter()
    for y in range(h):
        for x in range(w):
            color = pixels[x, y]
            color_counter[color] += 1

    colors = list(color_counter.keys())
    json_rgb_set = {tuple(v) for v in name_to_rgb.values()}
    missing_colors = [c for c in colors if c not in json_rgb_set]

    if missing_colors:
        print("❌ 發現圖片中有 colors copy.json 沒定義的顏色：")
        for c in missing_colors:
            print("  ", c)
        raise SystemExit("先去網站洗一下色再繼續")
    print(f"總共使用 {len(colors)} 種顏色")

    def pixel_to_screen(x, y):
        sx = round(x1 + x * (x2 - x1) / (w - 1))
        sy = round(y1 + y * (y2 - y1) / (h - 1))
        return sx, sy
    
    def format_time(seconds):
        seconds = int(seconds)
        h = seconds // 3600
        m = (seconds % 3600) // 60
        s = seconds % 60
        return f"{h:02d}:{m:02d}:{s:02d}"

    def verify_color(x, y, color_name):
        screenshot = ImageGrab.grab(bbox=(x, y, x+1, y+1))
        now_color = np.array(screenshot)[0][0]
        if now_color[0] == (name_rgb[color_name][0]) and now_color[1] == (name_rgb[color_name][1]) and now_color[2] == (name_rgb[color_name][2]):
            return True
        return False

    input("按Enter後 用滑鼠點一下小鎮 隨即將開始畫...")
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("開始")

    start_time = time.time()

    pyautogui.PAUSE = 0
    stime = 0.5
    current_letter = "H"

    LETTER_ORDER = ["H","A","B","C","D","E","F","G","I","J","K","L","M"]

    def click_left(times):
        for _ in range(times):
            pyautogui.moveTo(data["L_color_x"], data["L_color_y"], duration=0.2)
            pyautogui.mouseDown()
            pyautogui.mouseUp()
            time.sleep(stime)

    def click_right(times):
        for _ in range(times):
            pyautogui.moveTo(data["R_color_x"], data["R_color_y"], duration=0.2)
            pyautogui.mouseDown()
            pyautogui.mouseUp()
            time.sleep(stime)

    COLOR_MAP = {tuple(v): k for k, v in name_to_rgb.items()}
    for idx, color in enumerate(colors, 1):
        color_name = COLOR_MAP.get(color, str(color))
        pixel_count = color_counter[color]
        print(f"\n[{idx}/{len(colors)}] 切換顏色到 {color_name}（共 {pixel_count} 格）")

        target_letter = color_name[0]
        cur_idx = LETTER_ORDER.index(current_letter)
        tar_idx = LETTER_ORDER.index(target_letter)
        diff = tar_idx - cur_idx
        if diff > 0:
            click_right(diff)
        elif diff < 0:
            click_left(-diff)
        current_letter = target_letter

        number = color_name[1:]
        pyautogui.moveTo(data[f"{number}_x"], data[f"{number}_y"], duration=0.2)
        pyautogui.mouseDown()
        pyautogui.mouseUp()

        time.sleep(1)

        for y in range(h):
            for x in range(w):
                wait_if_paused()

                if pixels[x, y] == color:
                    sx, sy = pixel_to_screen(x, y)
                    pyautogui.moveTo(sx, sy, duration=0.1)
                    pyautogui.mouseDown()
                    pyautogui.mouseUp()
                    dot_time = 0
                    while True:
                        wait_if_paused()
                        time.sleep(0.05)
                        if not verify_color(sx, sy, color_name):
                            pyautogui.mouseDown()
                            pyautogui.mouseUp()
                            dot_time += 1
                            if dot_time == 1:
                                print(f"\n重複點擊 {dot_time}", end='')
                            elif dot_time % 40 != 0:
                                print(f"\r重複點擊 {dot_time}", end='')
                            else:
                                for _ in range(13):
                                    pyautogui.moveTo(data["L_color_x"], data["L_color_y"], duration=0.2)
                                    pyautogui.mouseDown()
                                    pyautogui.mouseUp()
                                    time.sleep(stime)
                                if "A" in color_name:
                                    for _ in range(1):
                                        pyautogui.moveTo(data["R_color_x"], data["R_color_y"], duration=0.2)
                                        pyautogui.mouseDown()
                                        pyautogui.mouseUp()
                                        time.sleep(stime)
                                elif "B" in color_name:
                                    for _ in range(2):
                                        pyautogui.moveTo(data["R_color_x"], data["R_color_y"], duration=0.2)
                                        pyautogui.mouseDown()
                                        pyautogui.mouseUp()
                                        time.sleep(stime)
                                elif "C" in color_name:
                                    for _ in range(3):
                                        pyautogui.moveTo(data["R_color_x"], data["R_color_y"], duration=0.2)
                                        pyautogui.mouseDown()
                                        pyautogui.mouseUp()
                                        time.sleep(stime)
                                elif "D" in color_name:
                                    for _ in range(4):
                                        pyautogui.moveTo(data["R_color_x"], data["R_color_y"], duration=0.2)
                                        pyautogui.mouseDown()
                                        pyautogui.mouseUp()
                                        time.sleep(stime)
                                elif "E" in color_name:
                                    for _ in range(5):
                                        pyautogui.moveTo(data["R_color_x"], data["R_color_y"], duration=0.2)
                                        pyautogui.mouseDown()
                                        pyautogui.mouseUp()
                                        time.sleep(stime)
                                elif "F" in color_name:
                                    for _ in range(6):
                                        pyautogui.moveTo(data["R_color_x"], data["R_color_y"], duration=0.2)
                                        pyautogui.mouseDown()
                                        pyautogui.mouseUp()
                                        time.sleep(stime)
                                elif "G" in color_name:
                                    for _ in range(7):
                                        pyautogui.moveTo(data["R_color_x"], data["R_color_y"], duration=0.2)
                                        pyautogui.mouseDown()
                                        pyautogui.mouseUp()
                                        time.sleep(stime)
                                elif "I" in color_name:
                                    for _ in range(8):
                                        pyautogui.moveTo(data["R_color_x"], data["R_color_y"], duration=0.2)
                                        pyautogui.mouseDown()
                                        pyautogui.mouseUp()
                                        time.sleep(stime)
                                elif "J" in color_name:
                                    for _ in range(9):
                                        pyautogui.moveTo(data["R_color_x"], data["R_color_y"], duration=0.2)
                                        pyautogui.mouseDown()
                                        pyautogui.mouseUp()
                                        time.sleep(stime)
                                elif "K" in color_name:
                                    for _ in range(10):
                                        pyautogui.moveTo(data["R_color_x"], data["R_color_y"], duration=0.2)
                                        pyautogui.mouseDown()
                                        pyautogui.mouseUp()
                                        time.sleep(stime)
                                elif "L" in color_name:
                                    for _ in range(11):
                                        pyautogui.moveTo(data["R_color_x"], data["R_color_y"], duration=0.2)
                                        pyautogui.mouseDown()
                                        pyautogui.mouseUp()
                                        time.sleep(stime)
                                elif "M" in color_name:
                                    for _ in range(12):
                                        pyautogui.moveTo(data["R_color_x"], data["R_color_y"], duration=0.2)
                                        pyautogui.mouseDown()
                                        pyautogui.mouseUp()
                                        time.sleep(stime)
                                else:
                                    pass
                                if "1" in color_name and "0" not in color_name:
                                    pyautogui.moveTo(data["1_x"], data["1_y"], duration=0.2)
                                    pyautogui.mouseDown()
                                    pyautogui.mouseUp()
                                elif "2" in color_name:
                                    pyautogui.moveTo(data["2_x"], data["2_y"], duration=0.2)
                                    pyautogui.mouseDown()
                                    pyautogui.mouseUp()
                                elif "3" in color_name:
                                    pyautogui.moveTo(data["3_x"], data["3_y"], duration=0.2)
                                    pyautogui.mouseDown()
                                    pyautogui.mouseUp()
                                elif "4" in color_name:
                                    pyautogui.moveTo(data["4_x"], data["4_y"], duration=0.2)
                                    pyautogui.mouseDown()
                                    pyautogui.mouseUp()
                                elif "5" in color_name:
                                    pyautogui.moveTo(data["5_x"], data["5_y"], duration=0.2)
                                    pyautogui.mouseDown()
                                    pyautogui.mouseUp()
                                elif "6" in color_name:
                                    pyautogui.moveTo(data["6_x"], data["6_y"], duration=0.2)
                                    pyautogui.mouseDown()
                                    pyautogui.mouseUp()
                                elif "7" in color_name:
                                    pyautogui.moveTo(data["7_x"], data["7_y"], duration=0.2)
                                    pyautogui.mouseDown()
                                    pyautogui.mouseUp()
                                elif "8" in color_name:
                                    pyautogui.moveTo(data["8_x"], data["8_y"], duration=0.2)
                                    pyautogui.mouseDown()
                                    pyautogui.mouseUp()
                                elif "9" in color_name:
                                    pyautogui.moveTo(data["9_x"], data["9_y"], duration=0.2)
                                    pyautogui.mouseDown()
                                    pyautogui.mouseUp()
                                elif "10" in color_name:
                                    pyautogui.moveTo(data["10_x"], data["10_y"], duration=0.2)
                                    pyautogui.mouseDown()
                                    pyautogui.mouseUp()
                                else:
                                    pass
                            time.sleep(0.2)
                        else:
                            break
        print("結束")

    total_time = time.time() - start_time
    print(f"✅ 全部畫完！總耗時 {format_time(total_time)}")

else:
    print("使用者取消了選擇檔案。")