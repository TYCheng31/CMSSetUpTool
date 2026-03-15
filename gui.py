import tkinter as tk
from tkinter import messagebox
import subprocess
import os
import webbrowser

# ==========================================
# 終端機執行指令包裝器
# ==========================================
def run_in_terminal(command, title):
    """
    在 Ubuntu 中彈出新的 gnome-terminal 來執行指令，
    並在執行完畢後等待使用者按下 Enter 才關閉視窗。
    """
    full_command = f"{command}; echo ''; echo '========================='; read -p '執行結束，請按 Enter 鍵關閉視窗...'"
    terminal_cmd = f"gnome-terminal --title='{title}' -- bash -c \"{full_command}\""
    
    try:
        subprocess.Popen(terminal_cmd, shell=True)
    except Exception as e:
        messagebox.showerror("執行錯誤", f"無法啟動終端機:\n{e}")

# ==========================================
# 各按鈕對應的執行功能
# ==========================================
def run_setup():
    run_in_terminal("chmod +x setup.sh && ./setup.sh", "🔧 環境安裝 (setup.sh)")

def run_reset_and_run():
    run_in_terminal("chmod +x reset_and_run.sh && ./reset_and_run.sh", "🔥 終極重置與建置 (reset_and_run.sh)")

def run_python_script(script_name):
    # 自動啟動虛擬環境並執行指定的 Python 腳本
    cmd = f"source tool_env/bin/activate && python {script_name}"
    run_in_terminal(cmd, f"🚀 執行 {script_name}")

def open_tutorial():
    url = "https://hackmd.io/@OgocyKRSRuKEbEqdS0BoKg/HknGjNN9Zx" 
    webbrowser.open(url)

# ==========================================
# 建立主視窗介面
# ==========================================
root = tk.Tk()
root.title("CMS 全自動化控制面板")
root.geometry("400x800") # 稍微調整高度以符合按鈕數量
root.configure(padx=20, pady=20)

# 使用教學 (移除 Emoji 避免 Ubuntu Tkinter 崩潰)
btn_help = tk.Button(root, text="使用教學", font=("Arial", 9, "underline"), fg="blue", cursor="hand2", relief="flat", command=open_tutorial)
btn_help.place(relx=1.0, rely=0.0, anchor="ne")

# 標題標籤 (移除 Emoji，更改為 Arial 字體)
title_label = tk.Label(root, text="CMS Setup Tool\n for NCUE", font=("Arial", 18, "bold"))
title_label.pack(pady=(0, 20))

# --- 區塊 1：系統指令 ---
frame_sys = tk.LabelFrame(root, text=" 系統管理 (Shell Scripts) ", font=("Arial", 12), padx=10, pady=10)
frame_sys.pack(fill="x", pady=10)

btn_setup = tk.Button(frame_sys, text="快速安裝所需環境\n(安裝完才能使用)", height=3,  fg="red",command=run_setup)
btn_setup.pack(fill="x", pady=5)

# 保留單一個紅色粗體的重置按鈕，避免重複定義
btn_reset = tk.Button(frame_sys, text="初始化並建立全新CMS\n(含contest*1、task*5、user*90)", height=3, font=("Arial", 10), command=run_reset_and_run)
btn_reset.pack(fill="x", pady=5)


# --- 區塊 2：Python 自動化腳本 ---
frame_py = tk.LabelFrame(root, text=" 任務自動化 (Python Scripts) ", font=("Arial", 12), padx=10, pady=10)
frame_py.pack(fill="x", pady=10)

btn_add = tk.Button(frame_py, text="新增 contest、task", height=3, command=lambda: run_python_script("AddContestTask.py"))
btn_add.pack(fill="x", pady=5)

btn_config = tk.Button(frame_py, text="配置 task 設定", height=3, command=lambda: run_python_script("AutoConfig.py"))
btn_config.pack(fill="x", pady=5)

btn_auto = tk.Button(frame_py, text="新增並配置\n(上面兩個按鈕的綜合版)", height=3, bg="#d9edf7", command=lambda: run_python_script("Auto.py"))
btn_auto.pack(fill="x", pady=5)

version_label = tk.Label(root, text="v2026.03.15", font=("Helvetica", 8), fg="gray")
version_label.place(relx=0.98, rely=0.98, anchor="se")
# ==========================================
# 啟動介面
# ==========================================
root.mainloop()