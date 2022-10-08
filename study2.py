#関数
#書き方

def double(n):
    return n * 10

print(double(9)) # 90

def showName(n):
    print(f"{n} suda")

showName("masaki") #masaki suda

#return

#Pythonでは、関数でreturnを書かなかった場合、 Noneをreturn することになっている ex)return None
#関数にreturnがなかったら関数を呼び出してもNoneが返ってくる



#キーワード引数、位置引数

def greet(name,by): #name. byは仮引数と呼ぶ
    print(f"{by} said, hi {name}")
#どちらがどちらだったか分かりづらくなる場合もある
#その場合、実引数にキーワードを指定することができる

greet(name="aimyon", by="gen") #aimyon, genは実引数と呼ぶ
                               #by="gen" このような書き方をキーワード引数と呼ぶ
greet(name="kenji", by="suda") 
                               #この場合は順序で仮引数に渡されていくから位置が重要という意味で位置引数と呼ぶ
                               
#greet(name="kenji", "suda") エラー
#キーワード引数と位置引数を一緒に書くことはできない



#引数のデフォルト値を指定
#仮引数のデフォルト値

def show_time(h,m,s=0,ms=0): # sとmsを指定しなかったら0にする
    print(f"{h:02}:{m:02}:{s:02}.{ms:03}")
                            #２桁で表示して満たない場合、0で埋めたい場合は:02とする

show_time(11,12,0,111)
show_time(4,34,2,56)


#関数で処理をまとめる
#わかりやすい関数名で全体の処理をまとめて、コードの見通しをよくする
def show_baseballPlayer():
    print("鈴木一朗")
    print("大谷翔平")
    
def show_actor():
    print("綾野剛")
    print("高橋一生")
    
def show_singer():
    print("aimyon")
    print("星野源")
    
show_baseballPlayer()
show_actor()
show_singer()



#変数のスコープ
#変数の有効範囲のことを「スコープ」と呼ぶ
#関数の外では関数の中の変数については考えなくてもいいよという仕組みになっている。
#関数の中の変数（ローカル変数）は関数の外では使えない、関数の外の変数（グローバル変数）は関数の中で使える
def get_price(a, b):
    #a,b,total -> ローカル変数(関数定義内でしか有効ではない変数)
    return a + b

total = 50 #グローバル変数(グローバル変数のスコープはこのファイル全体)
print(get_price(300, 500)) #800
print(total) #50



#ローカル変数になる条件を確認
# def get_price(a, b):
#     if a + b >= 3000:
#             rate = 1.05
#     total = (a + b) * rate #ここでエラーが発生
#     return total

# rate = 1.1
# print(get_price(300, 700))

# 仮引数、値が代入された変数 → ローカル変数
# 値が代入されていない変数 → 外のスコープを探す
# でもここでのrateはローカル変数
# pythonでは条件分岐などは一切考慮せずに、関数定義内で変数に値を代入するコードさえあればローカル変数になるというルールがある！



#コードを読みやすくする
#上のrate変数エラーの解決策
#1.グローバル変数を使う
#シンプルで短いプログラムだったら、グローバルキーワードを使うことで引数を減らすことができるというメリットがある
#2.グローバル変数の値を実引数で渡す
#より複雑なプログラムでわかりやすいコードを書くためには外から引数で渡した方がいい
def get_price(a, b):
    #global rate / グローバルキーワード
    if a + b >= 3000:
        rate = 1.05
    total = (a + b) * rate
    return total

rate = 1.1 # 関数内でグローバルキーワードを使うとこのrateが使われる
print(get_price(300, 700, rate)) 
print(get_price(3000, 7000, rate)) #必要に応じて値を引数で渡す
print(rate) #get_price(3000, 7000)この作業が終わった後のrateには1.05が代入されている
#上のrateでは1.1だったのに急に1.05になると読みにくいコードになる
#関数の外ではローカル変数のrateに対して行った処理は無視されるから、値を引数で渡すとそのまま１.1が表示される
