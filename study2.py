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