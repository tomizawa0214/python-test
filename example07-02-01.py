# coding:utf-8
import tkinter as tk

# ウィンドウを描く
root = tk.Tk()
root.geometry("600x400")

# Canvasを置く
canvas =tk.Canvas(root, width=600, height=400, bg="white")
canvas.place(x=0, y=0)

# 円を描く
canvas.create_oval(300 - 20, 200 - 20, 300 + 20, 200 + 20)

root.mainloop()
