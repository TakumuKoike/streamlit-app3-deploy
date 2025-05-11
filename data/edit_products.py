import pandas as pd
import random

# CSVファイルを読み込む
df = pd.read_csv("products.csv", encoding="cp932")
# df = pd.read_csv("products.csv") #このように書いてしまうと文字コードが違ったときにエラーになる

# 列「stock_status」にランダムで「あり」または「なし」を入れる
df["stock_status"] = [random.choice(["あり", "残りわずか","なし"]) for _ in range(len(df))]

# 新しいCSVとして保存（上書きも可）
df.to_csv("products.csv", index=False, encoding="cp932")
# df.to_csv("products.csv", index=False) #このように書いてしまうと文字化けした形で保存されてしまうことがある