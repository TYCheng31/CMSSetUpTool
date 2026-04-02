import tkinter as tk
from tkinter import messagebox
import subprocess
import os
import webbrowser
import importlib
import re

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

def run_reset_and_run():
    run_in_terminal("chmod +x reset_and_run.sh && ./reset_and_run.sh", "🔥 終極重置與建置 (reset_and_run.sh)")

def run_python_script(script_name):
    # 自動啟動虛擬環境並執行指定的 Python 腳本
    cmd = f"source tool_env/bin/activate && python {script_name}"
    run_in_terminal(cmd, f"🚀 執行 {script_name}")

def open_tutorial():
    url = "https://hackmd.io/@OgocyKRSRuKEbEqdS0BoKg/Sku88wjsbl" 
    webbrowser.open(url)

# ==========================================
# 動態設定檔編輯器 (不寫死變數)
# ==========================================
def open_config_editor():
    # 嘗試重新載入 config 確保抓到最新值
    try:
        import config
        importlib.reload(config)
    except Exception as e:
        messagebox.showerror("錯誤", f"無法讀取 config.py:\n{e}")
        return

    editor = tk.Toplevel(root)
    editor.title("⚙️ 設定 config.py")
    editor.geometry("450x600")
    editor.configure(padx=10, pady=10)

    # 動態過濾出 config 模組中所有「大寫且不以底線開頭」的常數變數
    config_vars = {k: v for k, v in vars(config).items() if k.isupper() and not k.startswith('_')}
    vars_dict = {}

    # 建立可滾動的框架 (避免變數太多時超出視窗)
    container = tk.Frame(editor)
    container.pack(fill="both", expand=True)

    canvas = tk.Canvas(container)
    scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)

    scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # 動態生成介面欄位
    row = 0
    for key, val in config_vars.items():
        tk.Label(scrollable_frame, text=f"{key}:", font=("Arial", 10)).grid(row=row, column=0, sticky="w", pady=8, padx=5)

        if isinstance(val, bool): # 布林值 -> 核取方塊
            var = tk.BooleanVar(value=val)
            tk.Checkbutton(scrollable_frame, variable=var).grid(row=row, column=1, sticky="w", padx=5)
        elif isinstance(val, list): # 列表 -> 轉為逗號分隔字串
            var = tk.StringVar(value=",".join(str(x) for x in val))
            tk.Entry(scrollable_frame, textvariable=var, width=28, font=("Arial", 10)).grid(row=row, column=1, sticky="w", padx=5)
        else: # 字串或數字 -> 一般輸入框
            var = tk.StringVar(value=str(val))
            tk.Entry(scrollable_frame, textvariable=var, width=28, font=("Arial", 10)).grid(row=row, column=1, sticky="w", padx=5)

        # 記錄變數物件與它的原始型態，存檔時會用到
        vars_dict[key] = (var, type(val))
        row += 1

    # 儲存並寫入檔案
    def save_and_close():
        try:
            with open("config.py", "r", encoding="utf-8") as f:
                content = f.read()

            # 遍歷剛剛記錄的所有變數，動態覆寫
            for key, (tk_var, val_type) in vars_dict.items():
                if val_type == bool:
                    bool_val = "True" if tk_var.get() else "False"
                    content = re.sub(rf'^({key}\s*=\s*)(True|False)', rf'\g<1>{bool_val}', content, flags=re.MULTILINE)
                
                elif val_type == list:
                    items = [t.strip() for t in tk_var.get().split(",") if t.strip()]
                    list_formatted = '["' + '", "'.join(items) + '"]'
                    content = re.sub(rf'^({key}\s*=\s*)\[.*?\]', rf'\g<1>{list_formatted}', content, flags=re.MULTILINE)
                
                else:
                    # 假設 config.py 中的字串都是被單引號或雙引號包住的
                    new_val = tk_var.get()
                    content = re.sub(rf'^({key}\s*=\s*)["\'].*?["\']', rf'\g<1>"{new_val}"', content, flags=re.MULTILINE)

            with open("config.py", "w", encoding="utf-8") as f:
                f.write(content)

            messagebox.showinfo("儲存成功", "設定檔已成功更新！\n下次執行自動化腳本時將套用新設定。")
            editor.destroy()
        except Exception as e:
            messagebox.showerror("儲存錯誤", f"寫入 config.py 時發生錯誤:\n{e}")

    # 儲存按鈕放在底部
    btn_save = tk.Button(editor, text="💾 儲存並關閉", bg="#5cb85c", fg="black", font=("Arial", 12, "bold"), command=save_and_close)
    btn_save.pack(fill="x", pady=10, padx=10)


# ==========================================
# 建立主視窗介面
# ==========================================
root = tk.Tk()
root.title("CMS 全自動化控制面板")
root.geometry("400x620") 
root.configure(padx=20, pady=20)

btn_help = tk.Button(root, text="使用教學", font=("Arial", 9, "underline"), fg="blue", cursor="hand2", relief="flat", command=open_tutorial)
btn_help.place(relx=1.0, rely=0.0, anchor="ne")

title_label = tk.Label(root, text="CMS Setup Tool\n for NCUE", font=("Arial", 18, "bold"))
title_label.pack(pady=(0, 20))

# user config
frame_config = tk.LabelFrame(root, text=" 參數設定", font=("Arial", 12), padx=10, pady=10)
frame_config.pack(fill="x", pady=5)

btn_edit_config = tk.Button(frame_config, text="參數設定\n(帳號、題目、限制時間等)", height=3, command=open_config_editor)
btn_edit_config.pack(fill="x", pady=5)

# cms init
frame_init = tk.LabelFrame(root, text=" 系統初始化", font=("Arial", 12), padx=10, pady=10)
frame_init.pack(fill="x", pady=5)

btn_reset = tk.Button(frame_init, text="初始化\n建立全新CMS(含contest*1、task*5、user*90)", height=3, font=("Arial", 10), command=run_reset_and_run)
btn_reset.pack(fill="x", pady=5)

# auto config
frame_py = tk.LabelFrame(root, text=" 自動化設置", font=("Arial", 12), padx=10, pady=10)
frame_py.pack(fill="x", pady=5)

btn_add = tk.Button(frame_py, text="自動新增 contest、task", height=3, command=lambda: run_python_script("AddContestTask.py"))
btn_add.pack(fill="x", pady=5)

btn_config = tk.Button(frame_py, text="自動配置 task 設定", height=3, command=lambda: run_python_script("AutoConfig.py"))
btn_config.pack(fill="x", pady=5)

version_label = tk.Label(root, text="v2026.04.02", font=("Helvetica", 8), fg="gray")
version_label.place(relx=0.98, rely=0.98, anchor="se")

root.mainloop()