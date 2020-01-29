def vow(name):
    vowels='aAEeIioOuU'
    for i in name:
        if i in vowels and i.lower() not in total_vowels:
            total_vowels.append(i.lower())
name=(input('Enter Your name:'))
count=0
total_vowels=[]
main_vowels='aeiuo'
vow(name)
for i in total_vowels:
    count+=1
total_vowels.sort()
print(f'Your name contains {count} types of vowels and here are they {total_vowels}')
