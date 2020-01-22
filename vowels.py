name=list(input('Enter Your name:'))
count=0
total_vowels=[]
main_vowels=['a','e','i','o','u']
vowels=['a','A','e','E','i','I','O','o','U','u']
for i in name:
    if i in vowels and i.lower() not in total_vowels:
        total_vowels.append(i.lower())
    else:
        print('Your name does not contain any vowels.Really?')
for i in total_vowels:
    count+=1
if len(total_vowels)==len(main_vowels):
    print(f'Your name containts all types of vowels {main_vowels}')
else:
    total_vowels.sort()
    print(f'Your name contains {count} types of vowels and here are they {total_vowels}')
