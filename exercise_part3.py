one_to_hundered = range(1, 101)
for num in one_to_hundered:
    if num % 3 == 0 and num % 5 == 0:
        print('BitMaker')
    elif num % 3 == 0:
        print('Bit')
    elif num % 5 == 0:
        print('Maker')
    else:
        print(num)


print('How many pizzas do you want to order?')
quantity = int(input())
for pizza in range(1,quantity + 1):
    print(f'How many toppings for piiza {pizza}?')
    toppings = float(input('$ '))
    print(f'You have ordered a pizza with {toppings} toppings.')


