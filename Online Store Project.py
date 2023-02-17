print("""-----------------------WELCOME TO MELIZZA STORES--------------------""")
print("\n")

import pandas as pw
pgoods = [
    {'Product': 'Fanta', 'Unit Price': 150, 'Quantity': 20},
    {'Product': 'Gin', 'Unit Price': 150, 'Quantity': 30},
    {'Product': 'Hennessy', 'Unit Price': 2300, 'Quantity': 13},
    {'Product': 'Ginger', 'Unit Price': 150, 'Quantity': 20},
    {'Product': 'Cocacola', 'Unit Price': 150, 'Quantity': 30},
    {'Product': 'Paper', 'Unit Price': 2300, 'Quantity': 24},
    {'Product': 'Flower', 'Unit Price': 150, 'Quantity': 20},
    {'Product': 'Milo', 'Unit Price': 200, 'Quantity': 30},
    {'Product': 'Bournvita', 'Unit Price': 150, 'Quantity': 20},
    {'Product': 'Skirt', 'Unit Price': 500, 'Quantity': 30},
    {'Product': 'Short', 'Unit Price': 2300, 'Quantity': 56},
    {'Product': 'Chocolate', 'Unit Price': 150, 'Quantity': 20},
    {'Product': 'Biro', 'Unit Price': 150, 'Quantity': 30},
    {'Product': 'Shirt', 'Unit Price': 2300, 'Quantity': 40},
    {'Product': 'Apple', 'Unit Price': 150, 'Quantity': 20},
    {'Product': 'Pawpaw', 'Unit Price': 500, 'Quantity': 30},
    {'Product': 'Tangerine', 'Unit Price': 400, 'Quantity': 84},
    {'Product': 'Onion', 'Unit Price': 150, 'Quantity': 20},
    {'Product': 'Garlic', 'Unit Price': 150, 'Quantity': 30},
    {'Product': 'Maggi', 'Unit Price': 2300, 'Quantity': 132},
    {'Product': 'Pepper', 'Unit Price': 400, 'Quantity': 20},
    {'Product': 'Knorr', 'Unit Price': 150, 'Quantity': 30},
    {'Product': 'Tapiko', 'Unit Price': 2300, 'Quantity': 235},
    {'Product': 'Tomato', 'Unit Price': 150, 'Quantity': 20},
    {'Product': 'Hollandia', 'Unit Price': 2500, 'Quantity': 30},
    {'Product': 'Chivita', 'Unit Price': 2300, 'Quantity': 124},
    {'Product': 'Rice', 'Unit Price': 1500, 'Quantity': 30},
    {'Product': 'Noodles', 'Unit Price': 3500, 'Quantity': 41},
    {'Product': 'Groundnut Oil', 'Unit Price': 2500, 'Quantity': 30},
    {'Product': 'Spaghetti', 'Unit Price': 450, 'Quantity': 50},
    {'Product': 'Beans', 'Unit Price': 500, 'Quantity': 60}
]
x = []
y = []
z = []




name = input('Enter your name: ').title()
while not name.isalpha():
    print("Please enter only alphabetical characters for your name.\n")
    name = input('Enter your name: ').title()
print(f'\nWelcome {name}')


def first_case():
    print('****** Melizza Store ******\n')
    print('1. Purchase Menu\n2. Logout')
    print('**********')
    q = input('>> ')
    while not q.isdigit() or int(q) != 2 and int(q) != 1:
        q = input('>> ')
    else:
        if int(q) == 1:
            print(f'Welcome {name}, Please place your order.\n')
            u_item()
            tot()
        else:
            print(f'Thank you for shopping with us {name}, Please come again.')
            exit()



def display():
    pd = []
    pd1 = []
    pd2 = []
    for i in pgoods:
        pd.append(i['Product'])
        pd1.append(i['Unit Price'])
        pd2.append(i['Quantity'])
    pdgoods = pw.DataFrame(
        {
            'Products': pd,
            'Price (NGN)': pd1,
            'Qty': pd2,
        }
    )
    pdgoods.index = pdgoods.index + 1
    print(pdgoods)

# ensures the input is a digit
def qty_chk(q):
    while not q.isdigit():
        q = input('Enter a number: ')
    else:
        return q


def u_item():
    zx = True
    while zx:
        display()    # Display the list of items in tabular form
        d = input('Product? \n>> ')
        d = d.title() # To return input as a title case.
        for i in pgoods:
            if d.title() == i.get('Product'):
                print(f"Here is the product and unit price\n"
                      f"Product: {d.title()}\n"
                      f"Price: {i.get('Unit Price')}"
                      f"\nQuantity: {i.get('Quantity')}\n")
                print('\nEnter the quantity that you want')
                q = input('Qty: ')
                qty_chk(q)    # Prompts the user to enter a number
                ''' line 83 checks if the user item quantity is less than 0
                    and if it greater than or equal to the user quantity input
                '''
                while i.get('Quantity') != 0 and i.get('Quantity') >= int(q):
                    print('Do you want to buy? \n(Y) YES          (N) NO')
                    w = input('>> ').upper()
                    if w == 'Y' or w == 'yes'.upper():
                        print('-----ACCEPTED-----\n')
                        a = i.get('Quantity') - int(q)
                        i['Quantity'] = a
                        x.append(i.get('Product'))
                        y.append(i.get('Unit Price'))
                        z.append(int(q))
                        print(f"The quantity of {i.get('Product')} has been reduced to {a}")
                        i.update({'Quantity': a})
                        print('Do you want to stop purchasing? \n(Y) Yes          (N) No')
                        e = input('>> ').upper()
                        if e == 'Y' or e == 'yes'.upper():
                            print('Purchase ended, Thank you for shopping with Melizza!')
                            zx = False

                    break
                else:
                    if i.get('Quantity') == 0:
                        print('\nOops, we are out of stock\n')
                        print('Please press 1 for Purchase menu or 2 to Logout')
                        return first_case()

                    elif int(q) > i.get('Quantity'):
                        print('\nItem(s) requested is more than quantity in inventory, '
                              'Please check available quantity.\n')
                        print('Please press 1 for Purchase menu or 2 to Logout')
                        return display()

                    zx = True



'''
    line 103 checks if user item quantity is 0
    line 106 checks if user quantity is greater than the user item quantity
'''
def tot():
    item = []
    price = []
    qty = []
    cost = []
    for i in x:
        item.append(i)
    for j in y:
        price.append(j)
    for k in z:
        qty.append(k)
    for k in range(len(y)):
        r = int(y[k]) * int(z[k])
        cost.append(r)
    txyz = sum(cost)
    td = pw.DataFrame(
        {
            'Item Bought': item,
            'Price (NGN)': price,
            'Qty': qty,
            'Cost (NGN)': cost,
        }
    )
    td.index = td.index + 1
    print(td)
    print(f'Total Cost of items (NGN): {txyz} ')

    if txyz >= 5000:
        c = (txyz * 12) / 100
        print(f'CONGRATULATIONS! YOU HAVE A DISCOUNT.\nTotal items is worth N5,000 or more, 12% discount applied {c}\n'
              f'Amount to pay (NGN): {txyz - c}\n')
        print(first_case())
    elif txyz in range(3500, 4999):
        b = (txyz * 10) / 100
        print(f'CONGRATULATIONS! YOU HAVE A DISCOUNT.\nTotal items is worth N3,500 or more , 10% discount applied {b}\n'
              f'Amount to pay (NGN): {txyz - b}\n')
        print(first_case())
    elif txyz in range(2000, 3499):
        v = (txyz * 5) / 100
        print(f'CONGRATULATIONS! YOU HAVE A DISCOUNT.\nTotal Cost is between 2000 and 3500, 5% discount applied {v}\n'
              f'Amount to pay (NGN): {txyz - v}\n')
        print(first_case())
    else:
        print(f'No discount, pay (NGN): {txyz}\n')
        print(first_case())

    td.to_csv('useritem.csv')
    # td.remove('useritem.csv')
first_case()
