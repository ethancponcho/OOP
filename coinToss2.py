import CoinClass as c

def show_coin_status(coin_obj):
    print(f"This side of the coin is up: {coin_obj.get_sideup()}")
    
def flip(coin_obj):
    coin_obj.toss()
    



mycoin = c.Coin()

#mycoin = 'Coin' Does not work - string objects do not have 
show_coin_status(mycoin)
flip(mycoin)
show_coin_status(mycoin)