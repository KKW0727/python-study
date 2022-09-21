#数値

#print(10)   #命令の区切りは ; ですが、文末では省略することができるから、通常はつけない。
            #　　#（パウンド記号） とするとそこから行末までが実行時に無視される。
#print(-100) 
#print(10_000_000); #少し見にくいから 3桁ごとに区切る
                   #結果 10000000  /  _は無視されて値に影響を与えない
#print(1.23)
#print(1.23e4) #12300 / 1.23に4乘（じょう）をかけたもの
#print(1.23e-4) #0.000123 / 1.23に-4乘（じょう）をかけたもの

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

number = int(input("number?"));
RATE = 1.5

#inputで受け取る値は必ず文字列になるからここでエラーが発生！
print(type(number));

#値のあとの : のあとにオプションを並べることができる
print(f"2019: {number * RATE:,.1f}")
print(f"2020: {number * RATE * RATE:,.2f}")
print(f"2021: {number * RATE * RATE * RATE:,.3f}")

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

japaneseScore = int(input("japaneseScore?"))
koreanScore = int(input("koreanScore?"))
if japaneseScore <= 0 and koreanScore <= 0:
    print("ERROR")
elif japaneseScore >= 80 or koreanScore >= 80:
    print("合格")
else:
    print("NG")
    print("不合格")

