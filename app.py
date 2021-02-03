#Pythonの辞書の機能を使用したシンプルなメモ帳。
#コマンドで操作する
import re
print("シンプルなメモ帳\n(c)2021 AlpacaPonyTree All Rights Reserved.")
print("※helpコマンドでマニュアルが表示されます。")
print("※全て小文字で入力してください。")

memo = {}
while True:
    command = input(">> ")
    if command == "exit" or command == "quit":
        break
    elif command == "add":
        title = input("タイトルを記入してください。※一度記入すると変更できません。")
        sentence = input("内容を記入してください。")
        memo[title] = sentence
        print("記入しました。")
    elif command == "help":
        print("add: 新しいメモを追加")
        print("remove: メモを削除")
        print("exit, quit: メモ帳を終了")
        print("preview [タイトル]: メモを見る")
        print("※タイトルを入力しなかった場合、全てのメモが表示されます。")
    elif command == "preview":
        print(memo)
    elif re.match(r"preview .+", command):
        print(memo[command.replace("preview ", "")])
    elif command == "remove":
        title = input("タイトルを入力してください。")
        print(f"タイトル: {title}")
        print(f"内容: {memo[title]}")

    else:
        print("Error: 存在しないコマンドか、表記が間違っています。")
