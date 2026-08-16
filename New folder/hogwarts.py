
hp_characters = {'Harry':{'Last Name': 'Weasley', 'WandType': 'Holly Wood'}}

# print(hp_characters['Harry']['Last Name'])

hp_characters['Harry']['Last Name'] = 'Potter'
# print(hp_characters['Harry']['Last Name'])

hp_characters['Hermione'] = {'Last Name': 'Granger', 'WandType': 'Vine Wood'}

# print()
# print()
# print()

# for dude in hp_characters:

#     print(hp_characters[dude])


hp_characters['Ron'] = {'Last Name': 'Weasley', 'WandType': 'Crimson Wood'}

for name, info in hp_characters.items(): 

    print(name)
    for type, dude in info.items(): 
        print('{} : {}'.format(type, dude))



    

    



            



    



    

    
    