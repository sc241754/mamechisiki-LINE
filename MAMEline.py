import tkinter as tk
import random

# ランダムに返信するための豆知識リスト
facts = [
    "クマは冬眠中にほとんど水分を摂取しません。体内の脂肪をエネルギー源にして生きています。",
    "カンガルーは後ろに進むことができません。",
    "ハチの羽音の速度は約200回/秒で、これがハチの飛行音の原因です。",
    "人間の鼻は最大で50,000種類の匂いを識別できると言われています。",
    "イルカは眠るとき、片方の脳を休めるため、半分ずつ交互に眠ります。"
]

# ユーザーの入力メッセージとランダムな豆知識をトーク画面に表示する関数
def send_message():
    user_message = user_input.get()
    if user_message:  # ユーザーがメッセージを入力していた場合
        # トーク履歴にユーザーのメッセージを追加 (右側、背景ライトグリーン)
        chat_box.config(state=tk.NORMAL)  # 変更可能にする
        chat_box.insert(tk.END, "\nあなた: " + user_message)
        chat_box.tag_add("user", chat_box.index("end-1c linestart"), chat_box.index("end-1c"))
        chat_box.tag_config("user", background="#90EE90")  # ユーザーのメッセージはライトグリーン
        chat_box.config(state=tk.DISABLED)  # 再度変更不可にする
        
        user_input.delete(0, tk.END)  # 入力欄をクリア
        
        # ランダムな豆知識を生成
        reply_message = random.choice(facts)
        
        # トーク履歴にAIの返信を追加 (左側、背景白)
        chat_box.config(state=tk.NORMAL)
        chat_box.insert(tk.END, "\nAI: " + reply_message)
        chat_box.tag_add("ai", chat_box.index("end-1c linestart"), chat_box.index("end-1c"))
        chat_box.tag_config("ai", background="white")  # AIのメッセージは白背景
        chat_box.config(state=tk.DISABLED)  # 変更不可にする
        
        chat_box.yview(tk.END)  # 新しいメッセージが表示されるようにスクロール

# GUIの設定
root = tk.Tk()
root.title("AIとのトーク画面")  # ウィンドウのタイトル

# スマートフォンサイズに合わせた画面比率 (例: 9:16の比率)
root.geometry("375x667")  # 一般的なスマホの画面サイズに近い

# バナー (常に画面の上部に固定)
banner = tk.Frame(root, bg="#ADD8E6", height=50)
banner.pack(fill="x", side="top")

# バナー内に「AI」というテキストを表示
banner_label = tk.Label(banner, text="AI豆知識", font=("Helvetica", 18, "bold"), bg="#ADD8E6", fg="black")
banner_label.pack(side="top", padx=10, pady=10)

# メッセージ表示用のテキストボックス (背景色をライトブルーに設定)
chat_box_frame = tk.Frame(root)  # チャットボックスを包むフレーム
chat_box_frame.pack(padx=10, pady=10, fill="both", expand=True)

chat_box = tk.Text(chat_box_frame, state=tk.DISABLED, width=40, height=20, wrap=tk.WORD, font=("Helvetica", 12), bg="#ADD8E6", padx=10, pady=5)
chat_box.pack(fill="both", expand=True)

# メッセージ入力用のエントリーフィールド
user_input = tk.Entry(root, width=40, font=("Helvetica", 12))
user_input.pack(padx=10, pady=5)

# メッセージ送信ボタン
send_button = tk.Button(root, text="送信", width=10, command=send_message, font=("Helvetica", 12))
send_button.pack(pady=5)

# GUIのループを開始
root.mainloop()
