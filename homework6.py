my_dict = {'Irina': 1996, 'Maksim': 1984, 'Andrei': 1969}
print(my_dict)
print(my_dict['Maksim'])
my_dict['Maksim'] = 1986
my_dict.update({'Sasha': 1995,
                   'Alex': 1997})
del my_dict['Irina']
print(my_dict.get('Irina'))
print(my_dict)

my_set = {1, 2, 3, 2, 1, 1, 'Denis'}
print(my_set)
print(my_set.add(6))
print(my_set.add(7))
print(my_set.discard(1))
print(my_set)