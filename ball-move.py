 # ブロック崩し
 from tkinter import *

 # ボールを表す辞書型データ --- (*1)
 ball = {
            "dirx": 15, # X方向のボールの速さ
            "diry": -15,  # Y方向のボールの速さ
            "x": 350, # ボールの位置
            "y": 300,
            "w": 10, # ボールの幅
           }

 # ウィンドウの作成 --- (*2)
 win = Tk()
 cv = Canvas(win, width = 600, height = 400)
 cv.pack()

 # 画面を描画する --- (*3)
 def draw_objects():
     cv.delete('all') # 既存の描画を破棄
     # ボールを描画
     cv.create_oval(
         ball["x"] - ball["w"], ball["y"] - ball["w"],
         ball["x"] + ball["w"], ball["y"] + ball["w"],
         fill="green")

 # ボールの移動 --- (*4)
 def move_ball():
     # 仮の変数に移動後の値を記録
     bx = ball["x"] + ball["dirx"]
     by = ball["y"] + ball["diry"]
     # 上左右の壁に当たった？
     if bx < 0 or bx > 600: ball["dirx"] *= -1
     if by < 0 or by > 400: ball["diry"] *= -1
     # 移動内容を反映
     if 0 <= bx <= 600: ball["x"] = bx
     if 0 <= by <= 400: ball["y"] = by

 # ゲームループ --- (*5)
 def game_loop():
     draw_objects()
     move_ball()
     win.after(50, game_loop)

 game_loop()
 win.mainloop() # ゲームウィンドウを表示


  blocks = [] # ブロックを管理する配列
 # ... 省略 ...
 # ブロックを配置する
 for iy in range(0, 5):
     for ix in range(0, 8):
         color = "red"
         if (iy + ix) % 2 == 1: color = "blue"
         x1 = 4 + ix * block_size["x"]
         x2 = x1 + block_size["x"]
         y1 = 4 + iy * block_size["y"]
         y2 = y1 + block_size["y"]
         blocks.append([x1, y1, x2, y2, color])

 # ブロックを一つずつ描画
 for w in blocks:
     x1, y1, x2, y2, c = w
     cv.create_rectangle(x1, y1, x2, y2, fill=c, width=0)