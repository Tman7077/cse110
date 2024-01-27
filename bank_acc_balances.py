accs, bals = [], []
print('Enter the names and balances of bank accounts (type "quit" - no quotes - when done)')
acc = input("What is the name of this account? ")
while acc.lower() != "quit":
     bal = float(input("What is the balance? $"))
     accs.append(acc.title())
     bals.append(bal)
     acc = input("What is the name of this account? ")
print()
print("Account Information:")
total = 0
for i in range(len(accs)):
     print(f'{accs[i]} - ${bals[i]:.2f}')
     total += bals[i]
print(f'Total: ${total}')
print(f'Average: ${total / len(accs)}')