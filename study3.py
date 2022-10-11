#より複雑なデータ型を扱う
#リスト型

scores = [10, 20, 30, 40, 50] #10, 20, 30などの個々のデータを要素と呼び
#要素は必ずしも同じデータ型である必要はなくて、ここに文字列型や、真偽値などを混ぜてもok
#でもリストは似たようなデータを大量に処理するときによく使われる

print(scores) #10,20,30,40,50
scores[1] = 100 # 20を100に変える
print(scores) #10,100,30,40,50 / 20が100に置き換わってる

print(scores[0]) #10