#Control flow & iteration

#if
age = int(input('enter your age: '))

money_unit = 'tomans'

if age <= 5:
    ticket_price = 8000
elif age <= 10:
    ticket_price = 10000
else:
    ticket_price = 20000

print(' you should pay {:0.1f} {}'.format(ticket_price, money_unit))


#while 
max_inp_frm_per_sec = 5
counter = 0

while counter < max_inp_frm_per_sec:
    print(counter)
    counter += 1
else:
    print('loop finished!')

