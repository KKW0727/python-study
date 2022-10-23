#より複雑なデータ型を扱う
#リスト型

# scores = [10, 20, 30, 40, 50] #10, 20, 30などの個々のデータを要素と呼び
#要素は必ずしも同じデータ型である必要はなくて、ここに文字列型や、真偽値などを混ぜてもok
#でもリストは似たようなデータを大量に処理するときによく使われる

# print(scores) #10,20,30,40,50
# scores[1] = 100 # 20を100に変える
# print(scores) #10,100,30,40,50 / 20が100に置き換わってる

# print(scores[0]) #10



#リストに要素を追加
#appendメソッド
#scores = [10, 20, 30, 20, 40]
#scores.append(60) #末尾に一つの要素を追加
#print(scores) #[10, 20, 30, 20, 40, 60]


#末尾に複数の要素を追加
#extendメソッド
# scores.extend([70,80,90])

#extend() は + の演算子で書き換えることもできる
#scores += [70,80,90]　/ scores.extend([70,80,90])と同じ意味
# print(scores) #[10, 20, 30, 20, 40, 60, 70, 80, 90]

#リストでは、+だけでなく*の演算子も使うことができる
#scores *= 3
# print(scores) #要素を 3 回繰り返したリストに書き換えてくれる


#途中に要素を追加
#insertメソッド
# ages = [10, 20, 30, 40]
# ages.insert(2,25) ##インデックスが 2の要素の前に 15を入れてね、という意味
# print(ages) #[10, 20, 25, 30, 40]　/ インデックス2は30だから30の前に入る



#リストから要素を削除する
#scores = [10, 20, 30, 20, 40]
#clear()を使う
#scores.clear() #[] / すべての要素を削除して、空にする

#値を指定して削除したい場合
#scores.remove(20)
# 20 の値が複数あった場合、最初の 1 つだけが削除される

#pop()を使う
#poped_item = scores.pop(2) #インデックスを指定して、要素を削除
#poped_item = scores.pop()#pop()の引数を省略すれば、末尾の要素を指定したことになる。

#del()を使う
#del scores[2] / scores.pop(2)と同じ意味
#でも、削除した要素を取得することができない

#pop()は削除した要素を返してくれる。
#print(poped_item) # 30 / インデックスが 2 であった 30 の要素が削除される

#print(scores)



#リストのデータを集計してみる
# scores = [10, 20, 30, 20, 40]
# # len()は他のデータ型でも使えるので、メソッドではなくて関数の書き方
# print(len(scores)) #5 /要素数
# print(min(scores)) #10 /最小値(さいしょうち)
# print(max(scores)) #40 /最大値(さいだいち)
# print(sum(scores)) #120 / 合計

#特定の値がリストの中にいくつあるかを調べる方法
#countメソッドを使う
# print(scores.count(20)) #2

# #特定の値がどのインデックスの位置にあるかを調べる方法
# #indexメソッドを使う
# print(scores.index(20)) #1

# #特定の値がそのリストに存在するかを調べる方法
# #inを使う
# print(30 in scores) #True / inは真偽値を返す
# print(90 in scores) #False



 #リストの要素を並び替える
scores = [10, 20, 30, 20, 40]

##要素の並び順を逆にしてくれる。
#scores.reverse() / 破壊的(元データを直接変更する)

#scores.sort() #値の小さい順に並び替えてくれる。

#値が大きい順に並び替えたい場合
#scores.sort(reverse=True) # sort()に引数を与える


#元データを残しておきたい場合
#元データはそのまま、要素を並び替えた結果を新しいリストとして返してくれるバージョンもある
scores_sorted = sorted(scores, reverse=True) ##非破壊的(元データを破壊しない処理)
print(scores) #[10, 20, 30, 20, 40] / 元データはそのまま
print(scores_sorted)



#スライス記法を使ってみる
#nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#num[3:6] #3~5 / インデックス3から始まって、 6 以降を除外したこの範囲を選択することになる。

#この範囲に対してリストを代入することで、値を書き換えることができる
#nums[3:6] = [100,110,111] #[0, 1, 2, 100, 110, 111, 6, 7, 8, 9]
#nums[4:4]=[3.5] #[0, 1, 2, 3, 3.5, 4, 5, 6, 7, 8, 9]

#nums[:3] =[] #最初からはじまって 3以降を除外した範囲を空にする
#[3, 4, 5, 6, 7, 8, 9]
#nums[3:] = [] #インデックスが 3から最後までを空にする
#[0, 1, 2]

#print(nums)


#スライス記法でリストを切り出す
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#sliced_list = nums[2:5]
#print(sliced_list) #[2, 3, 4]
#選択された要素を持つ新しいリストを作って返してくれる

#sliced_list = nums[1:9:3]
#インデックスが1から始まって9以降を除外したこの範囲において、みっつごとという意味になる
#print(sliced_list) #[1, 4, 7]

#sliced_list = nums[8:2:-2]
#8から始まって2以降を除外したこの範囲において、逆向きに2個づつ
#print(sliced_list) #[8, 6, 4]

sliced_list = nums[::-1] #非破壊的
#元リストを変更せずに要素を逆にしたリストを取得できる
#最後から最初までという意味になって、ちょうどこのリストを逆にしたリスト
#print(sliced_list) #[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]



#リストとループを組み合わせる
# prices = [100,200,300,400,500]

# for price in prices:
#     print(price * 1.3)
    
# #インデックスを合わせて取得する
# for index, price in enumerate(prices):
#     print(f"{index}: {price * 1.3:.2f}")



#リスト内包表記を使ってみる
# prices = [100, 200, 150, 200, 100]

# #税込価格を要素とする新しいリストを作る
# #tax = []
# # for price in prices:
# #     tax.append(price * 1.3)
# # print(tax)

# #もっと簡単に書ける方法
# #実は短い記法が用意されている
# tax = [price * 1.3 for price in prices]
# #こういった書き方はリスト内包表記と呼ばれている
# print(tax)




#リスト内包表記とifを組み合わせる
# if を加えることで、特定の要素だけを含めたり、特定の要素だけを除外することができる。
prices = [100, 200, 150, 200, 100]
#tax =[]
# for price in prices:
#     if price != 200:
#         tax.append(price * 1.3)
# print(tax)

#remove()を使ってもいいけど、最初に見つかったものしか削除してくれないから、いろいろ面倒!。
#そこでループ処理と条件分岐を組み合わせる
tax = [price * 1.3 for price in prices if price != 200]
print(tax)



#タプル(tuple)
#複数の値をまとめたデータ型
#in, len(), index(),count() -> 使える
#append(), insert(), pop() ->使えない(要素を変更することはできない)
#タプルはいったん生成されたら、この中の要素を変更することができない(リストと違う点)

#aimyon = ("西宮市", 27, 161)
# aimyon = "西宮市", 27, 161
# print(aimyon)

# #タプルの各要素はインデックスでアクセスできる
# print(aimyon[0])

# #どうしてもタプルの要素を変更したくなった場合、リストに変換してしまえばOK 
# aimyon = list(aimyon)
# print(aimyon)

# #変更後にタプルに戻したかったら
# aimyon = tuple(aimyon)
# print(aimyon)



# タプルをアンパックする
aimyon = "西宮市", 27, 161

#birthplace, age, height = aimyon

#実際使うのは出身地の情報だけだった場合
#アンパックに限らず、Pythonでは使う予定のない変数には慣習的に （アンダースコア）一文字が使われる。
#あとから使わないよと言う意図を伝えることができる
# birthplace, _, _ = aimyon

# print(birthplace)
# print(age)
# print(height) 


#連続した要素は *(アスタリスク）を付けた変数でまとめて取り出すことができる
# birthplace, *ageHeight = aimyon
# print(birthplace) #西宮市
# print(ageHeight) #[27, 161] / タプルではなくてリストになる

#出身地は使うけど、年齢も身長も後から使わない時
birthplace, *_ = aimyon
print(birthplace) #西宮市

