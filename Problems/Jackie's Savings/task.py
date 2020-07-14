def final_deposit_amount(*interest, amount=1000):
    for n in interest:
        amount = amount + amount * (n / 100)
    return round(amount, 2)
