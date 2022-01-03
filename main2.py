from define import Feoexpectedvalue
from define import charactercheck
from define import expectedvalue
from define import printxlsx
from define import getpartyexpectedvalue
from define import Getenemydata
from define import fullexpectedvalue
from define import fullprintxlsx
from define import getfullexpectedvalue

Feoexpectedvalue('data.xlsx').feodmgprint()

print('FEO基礎ダメージの計算が完了しました')

# Feoexpectedvalue('data.xlsx').


checkedlist = charactercheck('data.xlsx')

for i in checkedlist:
    value = 0
    value = expectedvalue('data.xlsx', str(i))
    printxlsx('data.xlsx', value, str(i))

print('キャラクターごとの期待値計算と書き込み完了、パーティ火力の計算に入ります')

getpartyexpectedvalue('data.xlsx')

print('全工程が完了しました。')
