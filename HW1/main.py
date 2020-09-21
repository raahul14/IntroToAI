import math


def calculate_change(total, amount):
    currency = [50, 20, 10, 5, 2, 1, 0.25, 0.10, 0.05, 0.01]
    labels = ['$50 bills', '$20 bills', '$10 bills', '$5 bills', '$2 bills', '$1 bills', 'quarters', 'dimes', 'nickels',
              'pennies']
    count = [0] * len(currency)
    print("Total: $", total)
    print("Paid: $", amount)
    change = round(amount - total, 2)
    print("Change: $", change)

    for i, a in enumerate(currency):
        if change > 0:
            amt = math.floor(change / a)
            if amt > 0:
                count[i] = amt
                change = change - amt * a

    for count, label in zip(count, labels):
        if count > 0:
            print(count, 'x', label)


def run():
    status = True
    while status:
        total = float(input("Enter total: "))
        if total < 0:
            print('Negative input not allowed.')
            status = False
            break
        amount = float(input("Enter amount: "))
        if amount < 0:
            print('Negative input not allowed.')
            status = False
            break
        if amount > total:
            calculate_change(total, amount)
        else:
            print('Not enough money. No change.')


if __name__ == '__main__':
    run()