def greetBirthday():
    birthdays = {"alice": "1st of april"}

    while True:
        print('What is your name?')
        name = input()
        if name == '':
            break
        if name.lower() in birthdays:
            print(birthdays[name] + " is the birthday of " + name)
        else:
            print('No information registered for this person birthday')
            print('What is their birthday')
            bday = input()
            birthdays[name] = bday
            print('birthdays database updated')


greetBirthday()
