# Pythonの辞書の機能を使用したシンプルなメモ帳。
# コマンドで操作する

# 準備
import re
import sys
import math
import os
from YNchecker import YNchecker
from str2list import string_to_list
def callMemo(title):
    print(f"タイトル: {title}")
    print(f"内容: {memo[title]}")
    return

# 開始
print("シンプルなメモ帳\n(c)2021 AlpacaPonyTree All Rights Reserved.")
print("※helpコマンドでマニュアルが表示されます。")
print("※全て小文字で入力してください。")
# メモの中身を空にする
memo = {}

# メイン処理
while True:
    command = input(">> ")
    if command == "exit" or command == "quit":
        #プログラムを終了
        sys.exit()
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
        print("save: メモ帳を保存")
        print("load: メモ帳を読み込む")
        print("erasure: 全てのメモを削除")
        print("cls: 画面をきれいにする")
        print("edit: メモを編集する")
    elif command == "preview":
        i = 1
        for sentence in memo:
            print(f"{i},")
            callMemo(sentence)
            i += 1
        print("表示されているのが以上です。")
    elif re.match(r"preview .+", command):
        callMemo(command.replace("preview ", ""))
    elif command == "remove":
        try:
            title = input("タイトルを入力してください。")
            callMemo(title)
            a = YNchecker("このメモを削除します。よろしいですか？(Y/N)")
            if a:
                memo.pop(title)
                print("削除しました。")
            else:
                print("取り消しました。")
        except KeyError:
            print("Error: 入力されたタイトルのメモが存在しません。")

    elif command == "save":
        a = YNchecker("メモを保存します。よろしいですか？(Y/N)\n※過去のデータは上書きされます。")
        if a:
            memo_data = open("memo_data/data.txt", "w")
            datas = ""
            for title in memo:
                datas += f"{title},{memo[title]},"
            memo_data.write(datas)
            memo_data.close()
            print("保存しました。")
        else:
            print("キャンセルしました。")

    elif command == "load":
        a = YNchecker("メモを読み込みます。よろしいですか？(Y/N)\n※現在のデータは上書きされます。")
        if a:
            memo_data = open("memo_data/data.txt")
            load_data_str = memo_data.read()
            load_data = string_to_list(load_data_str)
            memo = {}
            i = 0
            while i < len(load_data):
                memo[load_data[i]] = load_data[i + 1]
                i += 2

            memo_data.close()
            print("読み込みました。")
        else:
            print("キャンセルしました。")
    elif command == "erasure":
        a = YNchecker("全てのメモを削除します。よろしいですか？(Y/N)")
        if a:
            memo = {}
            print("削除しました。")
        else:
            print("キャンセルしました。")
    elif command == "cls":
        os.system("cls")
    elif command == "edit":
        try:
            title = input("編集するメモのタイトルを入力: ")
            callMemo(title)
            sentence = input("編集する内容を入力: ")
            print("編集内容:",memo[title],"=>",sentence)
            if YNchecker("この内容でよろしいですか？(Y/N)"):
                memo[title] = sentence
                print("編集しました。")
            else:
                print("キャンセルしました。")
        except KeyError:
            print("Error: 入力されたタイトルのメモが存在しません。")


    else:
        print("Error: 存在しないコマンドか、表記が間違っています。")
