# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 17:39:15 2022

@author: Ryozo Nakamura
このプログラムは、在庫も初期化されるので、在庫がない場合の挙動がみたければdrink_listのstockを書き換えてください
"""
drink = ['coke', 'coffee', 'energy']
drink_list = {
    drink[0]: {'price': 100, 'stock': 10},
    drink[1]: {'price': 120, 'stock': 5},
    drink[2]: {'price': 200, 'stock': 20}
}
change_stock = {1000: 10,
                5000: 10,
                100: 10,
                500: 10,
                100: 10,
                50: 10,
                10: 10,
                5: 10,
                1: 10}


def changeCalculation(insert, price):
    """
    おつり計算用関数

    Parameters
    ----------
    insert : int
        投入された金額.
    price : int
        該当商品の値段.

    Returns
    -------
    None.

    """
    # おつりを格納する変数
    change = insert - price
    # 各硬貨・紙幣を何枚返すのか記録しておく辞書
    change_list = {10000: 0,
                   5000: 0,
                   1000: 0,
                   500: 0,
                   100: 0,
                   50: 0,
                   10: 0,
                   5: 0,
                   1: 0}
    # 1万円から順に出ていく紙幣・硬貨の枚数を計算していく
    for i in [10000, 5000, 1000, 500, 100, 50, 10, 5, 1]:
        if change >= i:
            change_list[i] = int(change / i)
            change = change % i
            change_stock[i] = change_stock[i] - change_list[i]
    print("¥ " + str(change) + " ﾉ ｵｶｴｼﾃﾞｽ")


def drinkOrder(name):
    """
    注文を聞く関数

    Parameters
    ----------
    name : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    # もし注文された商品が商品リストにあれば支払いに進む. なければ無いといって終了
    if name in drink_list:
        # 在庫があるか確認.
        if drink_list[name]['stock'] > 0:
            print(name + " ﾊ ¥" + str(drink_list[name]['price']) + " ﾃﾞｽ")
            insert = int(input("いくら支払いますか? >"))
            # 金額と投入金が等しい場合. おつり計算無し
            if insert == drink_list[name]['price']:
                print("ﾏｲﾄﾞｱﾘ")
                # 在庫数を1減らす
                drink_list[name]['stock'] = drink_list[name]['stock'] - 1
            # 投入金 > 金額. changeCalculationでおつり計算
            elif insert > drink_list[name]['price']:
                print("ﾏｲﾄﾞｱﾘ")
                drink_list[name]['stock'] = drink_list[name]['stock'] - 1
                changeCalculation(insert, drink_list[name]['price'])
            else:
                print("\nﾏﾈｰ ｶﾞ ﾀﾘﾅｲ ﾝﾀﾞｹﾄﾞ")
        else:
            print("\nｺﾞﾒﾝ ｲﾏ ｼﾅｷﾞﾚ ﾅﾝﾀﾞ")

    else:
        print("\nｿﾝﾅﾓﾝ ｳﾁﾆﾊ ﾈｴﾖ")
        print("ｲﾏ ｳﾁﾆ ｱﾙﾉﾊ")
        for i in drink:
            if drink_list[i]['stock'] > 0:
                print(i)
        print("\nﾉ " + str(len(drink)) + " ｺ ﾀﾞﾖ")


print("ｲﾗｯｼｬｲﾏｾ")
print("ｺﾞﾁｭｳﾓﾝﾊ\nﾒﾆｭｰﾊｺﾁﾗﾃﾞｽ\n")
for i in drink:
    print(str(i) + " ¥" + str(drink_list[i]['price']) + "  ﾉｺﾘ: " + str(drink_list[i]['stock']) + " ｺ")
drinkOrder(input(">"))
