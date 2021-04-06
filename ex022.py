name = input('Digite seu nome completo: ').strip()
print(f'Seu nome em letras maiusculas fica {name.upper()}')
print(f'Seu nome em letras minusculas fica {name.lower()}')
firstName = name.split(' ')

name = name.replace(' ','')
print(f'Seu nome completo tem {len(name)} letras')
print(f'Seu primeiro nome é {firstName[0]} e tem {len(firstName[0])} letras')

