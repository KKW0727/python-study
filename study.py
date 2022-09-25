#数値

#print(10)   #命令の区切りは ; ですが、文末では省略することができるから、通常はつけない。
            #　　#（パウンド記号） とするとそこから行末までが実行時に無視される。
#print(-100) 
#print(10_000_000); #少し見にくいから 3桁ごとに区切る
                   #結果 10000000  /  _は無視されて値に影響を与えない
#print(1.23)
#print(1.23e4) #12300 / 1.23に4乘（じょう）をかけたもの
#print(1.23e-4) #0.000123 / 1.23に-4乘（じょう）をかけたもの

from tkinter.tix import InputOnly
from unittest import result


print(10 + 3) #13 / 足し算
print(10 * 5) #50 / 掛け算
print(10 - 4) #6 / 引き算
print(10 / 3) #3.33333... / 普通の割り算、　float
print(10 // 3) #3 / 商（しょう）、int
print(10 ** 7) #10000000 / べき乘
print(10 % 7) #3 / あまりを計算してくれる 

#変数
#number = 1000;
# = 代入演算子(だいにゅうえんざんし)
#RATE  = 1.2; #定数
#値を再代入しない変数はpythonでは慣習的に大文字にする。
#再代入してはいけない変数のことを定数と呼ぶ。
#print(number * RATE);

#ここで1000や1.2という値をリレラル（null値以外の値）と呼ぶ

#変数のルール
#1.a-z A-Z 0-9 _
#2.数字から始めてはいけない
#3.予約語は使ってはいけない
#4.大文字小文字は区別される

#number変数に違う値を再代入
#number = 2000;


#文字列
# print('I\'m in japan');
# print("I'm in japan");

#改行
print("I'm \nin \njapan");
print("""I'm 
in 
japan""");

#先頭を備えて書きたい場合
#文末に \ をつければその行の改行は無視される
print("""\
I'm 
in 
japan""");

#文字列 + 文字列
#print("masaki" " " "suda"); #masaki suda
#print("masaki" + " " + "suda"); #masaki suda
#print("@" * 10);

fname = "masaki"
lname = "suda"
# print("name: " +  fname + " "+ lname);


#文字列に値を埋め込む
age = 29
#print("I'm " + fname + " " + lname + ", " + str(age) + " years old!");
#見づらいからこういう場合はformat()という　命令が使える。

#format()命令
#format()命令を使うと埋め込まれるときに自動的に文字列型に変換されるから、こっちで strを使う必要はない！
#print("I'm {} {}, {} years old!".format(fname, lname, age));

#Pythonの 3.6から f文字列というもう少し短く書く記法も用意されている。
#最近だとほとんどの場合、f文字列を使う。
print(f"I'm {fname} {lname}, {age} years old!");



#ユーザーから入力を受け取る
#num = input("number?")
#print(num * 2) #2を入力した時は4じゃなくて22になる / 2を2回繰り返すという意味になる
#+、-、/、%はエラー発生　/ データ型を変換する必要がある
#inputで受け取る値は必ず文字列になるという仕様になっているから！
#だから必要に応じてデータ型を適宜変換する必要がある。

#整数
#print(int(num) * 2) #4

#浮動小数点数
#print(float(num) * 2)#4.0


#f文字列のオプションを使う

#number = int(input("number?"));
#RATE = 1.5

#inputで受け取る値は必ず文字列になるからここでエラーが発生！
#print(type(number));

#値のあとの : のあとにオプションを並べることができる
#print(f"2019: {number * RATE:,.1f}")
#print(f"2020: {number * RATE * RATE:,.2f}")
#print(f"2021: {number * RATE * RATE * RATE:,.3f}")

#条件分岐
#if...elif...else
#elif を使えば複数の条件で場合分けをすることができる
#Python では、字下げがあるかないかで全く違う意味になるので、注意!
#字下げに使う空白は何文字でもいいけど、 Pythonでは半角空白 4文字が使われることが多い

#比較演算子
# > >=
# < <=
# == !=

# 論理演算子
# and なおかつ
# or もしくは
# not ~ではない

#japaneseScore = int(input("japaneseScore?"))
#koreanScore = int(input("koreanScore?"))
# if japaneseScore <= 0 and koreanScore <= 0:
#     print("ERROR")
# elif japaneseScore >= 80 or koreanScore >= 80:
#     print("合格")
# else:
#     print("NG")
#     print("不合格")



#match
#python 3.10以降のみに対応
#複数の場合分けをする処理
#場合分けの条件が増えてくると、 elifよりすっきり書ける

# signal = input("signal color?")
# match signal:
#     case "red":
#         print("stop")
#     case "yellow": 
#         print("slow")
#     case "blue" | "green":
#         print("go!")
#     case _:
#         print("Invalid signal color...")


# if...else...を一行で書く
#書き方
#条件式が真のときに返す値 if 条件式 else 条件式が偽のときに返す値
input_num = int(input("数字を入力してください。"))

# result = "合格" if input_num >= 80 else "不合格"
# print(result)


#matchとifを組み合わせる
#case >= 90や　case input_num >= 90のように書くことができないからinput_numの値を何らかの変数で受ける
match input_num:
    case n if n < 0 or n > 100:
       print("invalid number")
    case n if n >= 90:
        print("A")
    case n if n >= 80:
        print("B")
    case n if n >= 70:
        print("C")
    case n if n >= 60:
        print("D")
    case _:
         print("不合格")


#反復処理
#for
for i in range(10): #0から9までの数列のようなものを生成してくれる
    print(f"{i} Hi python") #i -> 0,1,2,3,4,5,6,7,8,9 #生成された数字を一つずつiに代入しながら10回繰り返す
 
#好きな範囲を作ることもできる
for i in range(5,9): #5から8
    print(f"{i} hello python") #i -> 5,6,7,8
    
for i in range(1,10,3): #1から 10に満たない数値まで 3刻みで、という意味
    print(f"{i} good python!") #i -> 1, 4, 7
    
#逆順
for i in range(8,5,-1):
    print(f"{i} python") #8,7,6
#最後の数値にマイナス値を指定すると、逆順
# 8から 5まで 1つずつ逆順に進むけど、5は含まないから、 8, 7, 6 になる
        


#forの中でforを使う
for i in range(2,10):
    print(i)
    for j in range(1,9):
        print(f"{i} * {j} = {i * j}")


# 反復処理 while
#for文は回数が決まっている時に使う
#while文は回数が決まっていない時やすぐにはわからない時に使う
# command = int(input("1: あいみょん, 2:菅田将暉, 3:星野源"))
# select = int(input("1.生年月日, 2.出身, 0.終了"))

# while select != 0:　#一回も実行されない場合がある
#     if command == 1:
#         if select == 1:
#             print("1995年3月6日")
#         elif select == 2:
#             print("日本 兵庫県 西宮市")
#     if command == 2:
#         if select == 1:
#             print("1993年2月21日")
#         elif select == 2:
#              print("日本 大阪府 箕面市")
#     if command == 3:
#         if select == 1:
#             print("1981年1月28日")
#         elif select == 2:
#             print("日本 埼玉県 蕨市")
#     command = int(input("1: あいみょん, 2:菅田将暉, 3:星野源"))
#     select = int(input("1.生年月日, 2.出身, 0.終了"))


#　whileをシンプルに書く
# 常に条件が成立するwhileを使う

#command = None #まだ値が定まっていないという意味で、 Noneという特殊なキーワードを使う

while 1 == 1: #必ず一回は実行される 
    command = int(input("1. あいみょん, 2.菅田将暉, 3.星野源, 0.終了"))
    if command == 0:
        break
    select = int(input("1.生年月日, 2.出身"))
    
    if command == 1:
        if select == 1:
            print("1995年3月6日")
        elif select == 2:
            print("日本 兵庫県 西宮市")
    if command == 2:
        if select == 1:
            print("1993年2月21日")
        elif select == 2:
             print("日本 大阪府 箕面市")
    if command == 3:
        if select == 1:
            print("1981年1月28日")
        elif select == 2:
            print("日本 埼玉県 蕨市")