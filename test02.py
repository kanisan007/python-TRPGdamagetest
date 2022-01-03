import random

# ハウスルールの技能判定による追加ダメージを算出するテスト

def getadditionaldamage(dice: int, hantei: str) -> int:
    if hantei == 'miss':
        None

    elif hantei == 'normal':
        dicedata = str(dice)
        dicelist = (list(dicedata))
        return int(dicelist[0])

    elif hantei == 'hard':
        dicedata = str(dice)
        dicelist = (list(dicedata))
        return int(dicelist[0])*2

    elif hantei == 'ex':
        dicedata = str(dice)
        dicelist = (list(dicedata))
        if len(dicelist) == 2:
            return int(dicelist[0])
        elif len(dicelist) == 1:
            return 0

ginou = 50
ginouhard = 25
ginouex = 10
ginoudice = random.randint(1, 100)
hantei = None
print(ginoudice)

if ginoudice>=90:
    print('miss!当たらない!')

elif ginoudice>ginou:
    print('技能は失敗です')
    hantei = ''
    print('追加ダメージは0です。')

elif ginoudice>ginouhard:
    print('技能は成功した')
    hantei = 'normal'
    additionaldamage = getadditionaldamage(ginoudice, hantei)
    print(f'追加ダメージは{additionaldamage}')

elif ginoudice>ginouex:
    print('技能はハード成功した')
    hantei = 'hard'
    additionaldamage = getadditionaldamage(ginoudice, hantei)
    print(f'追加ダメージは{additionaldamage}')

elif ginoudice<=ginouex:
    print('技能はエクストリーム成功した')
    hantei = 'ex'
    additionaldamage = str(getadditionaldamage(ginoudice, hantei))+'+'+'2d10'
    print(f'追加ダメージは{additionaldamage}')



