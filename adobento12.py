import tkinter as tk
from tkinter import messagebox
import math

class AdventCalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("12月のアドベントカレンダー")
        
        # 背景色をライトグリーンに設定
        self.root.configure(bg="#b0e57c")
        
        # 各日のメッセージ（12月1日から25日まで）
        self.messages = {
            1: "今日は12月1日！クリスマスまであと24日ですね。",
            2: "12月2日、寒い季節がやってきました。",
            3: "12月3日、今日も素晴らしい一日が始まります。",
            4: "12月4日、今年のクリスマスはどう過ごしますか？",
            5: "12月5日、忙しい毎日が続きますが頑張りましょう。",
            6: "12月6日、冬の風景が素敵ですね。",
            7: "12月7日、もうすぐクリスマスパーティーですね。",
            8: "12月8日、ホットチョコレートを飲みたくなる季節。",
            9: "12月9日、雪が降るといいなぁ。",
            10: "12月10日、あと15日でクリスマス！",
            11: "12月11日、クリスマス準備が進んでいますか？",
            12: "12月12日、今年はどんなプレゼントを選びますか？",
            13: "12月13日、気温がどんどん下がってきました。",
            14: "12月14日、クリスマスソングが流れ始めました。",
            15: "12月15日、クリスマスの計画を立てよう。",
            16: "12月16日、冬休みまであと少し！",
            17: "12月17日、今年も素晴らしい思い出を作りましょう。",
            18: "12月18日、クリスマスツリーを飾りつけしましたか？",
            19: "12月19日、プレゼント選びに迷っていますか？",
            20: "12月20日、今年のクリスマスは特別な日。",
            21: "12月21日、冬至が近づいています。",
            22: "12月22日、クリスマスが待ちきれませんね。",
            23: "12月23日、家族や友達と一緒に過ごしましょう。",
            24: "12月24日、クリスマスイブ、素敵な夜になりますように。",
            25: "12月25日、メリークリスマス！素晴らしい一日を！"
        }
        
        # 日付に対応するボタンを保存する辞書
        self.buttons = {}
        
        # 既に開封された日（ボタンの状態を管理）
        self.opened_days = set()
        
        # キャンバスを作成（リースとタイトルを描くため）
        self.canvas = tk.Canvas(self.root, width=400, height=400, bg="#b0e57c", bd=0, highlightthickness=0)
        self.canvas.pack()
        
        # タイトル「12月アドベントカレンダー」を表示
        self.canvas.create_text(200, 35, text="12月アドベントカレンダー", font=("Arial", 18, "bold"), fill="green")
        
        # リースの形でボタンを配置
        self.create_wreath_layout()

    def create_wreath_layout(self):
        # リースの形でボタンを配置
        num_buttons = 25  # 25個のボタン（1日〜25日）
        radius = 150  # リースの半径
        center_x = 200  # キャンバスの中央X座標
        center_y = 200  # キャンバスの中央Y座標
        
        # ボタンを円形に配置
        for day in range(1, num_buttons + 1):
            # 角度を計算（360°を25等分）
            angle = math.radians(360 * (day - 1) / num_buttons)
            x = center_x + radius * math.cos(angle)
            y = center_y + radius * math.sin(angle)
            
            # ボタンを作成
            button = tk.Button(self.root, text=str(day), width=5, height=2,
                               command=lambda day=day: self.open_window(day))
            button.place(x=x, y=y)
            self.buttons[day] = button

    def open_window(self, day):
        if day not in self.opened_days:
            # 開封した日としてマーク
            self.opened_days.add(day)
            self.buttons[day].config(state="disabled")
            
            # メッセージを表示
            messagebox.showinfo(f"{day}日目", self.messages[day])
        else:
            messagebox.showwarning("既に開封済み", f"{day}日目は既に開封済みです。")

# メイン処理
if __name__ == "__main__":
    root = tk.Tk()
    app = AdventCalendarApp(root)
    root.geometry("400x400")  # ウィンドウサイズを指定
    root.mainloop()