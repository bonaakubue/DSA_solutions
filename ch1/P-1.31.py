#Write a Python program that can "make change."" Your program should take two numbers 
# as input, one that is a monetary amount charged and the other that is a monetary 
# amount given. It should then return the number of each kind of bill and coin to give 
# back as change for the difference between the amount given and the amount charged. 
# The values assigned to the bills and coins can be based on the monetary system 
# of any current or former government. Try to design your program so that it returns 
# as few bills and coins as possible.

def make_change(charged, given):
    change = given - charged
    bills = {'$1':1, '$5':5, '$10':10, '$20':20, '$50':50, '$100':100}
    coins = {'1 cent': 1, '5 cents': 5, '25 cents':25, '50 cents':50}
    bill_change = int(change)
    coin_change = change - bill_change
    max_bill = max_coin = 1

    for bill in bills:

        
        if bill_change % bills.get(bill)>0 and bills.get(bill)!=1 and bills.get(bill) > max_bill:
            max_bill = bills.get(bill)
        elif bill_change % bills.get(bill)==0 and bills.get(bill) > max_bill:
            max_bill = bills.get(bill)

    for coin in coins:
        if coin_change % coins.get(coin)==0 and coins.get(coin) > max_coin:
            max_coin = coins.get(coin)

    result = f'your change is {bill_change//max_bill} ${max_bill} bills and {int(coin_change//max_coin)} {(max_coin)*100} cents coins'
    return result


result = make_change(35.5, 80)
print(result)