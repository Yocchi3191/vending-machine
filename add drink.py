# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 19:19:58 2022

@author: USER
"""
drink = {}
def addDrink():
    """
    商品追加関数. 別ファイルの vending machine.pyと一緒に使用するとかを想定

    Returns
    -------
    None.

    """
    name = input("追加したい飲料の名前を入力してね >")
    price = input("値段はいくらにする？ >")
    stock = input("いくつ追加したい？ >")
    drink[name] = {
        'price': int(price), 'srock': int(stock)
    }