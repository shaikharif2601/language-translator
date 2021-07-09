# How to run this program if you don't have PYTHON ?
# -> to run this program without pythons go to Google Collab and run this program
# -> but first type this command in the Google Collab (pip install textblob)
# -> and copy the whole program and paste it over there.

# Python program to translate languages
# import the required module to Translate languages

from textblob import TextBlob as t

# Calling the TextBlob method of the module which
# interact with translator api to translate
# the given input from the keyboard


print("*************************Welcome To Language Translator*********************")
translator = t(input("\t\tEnter Your Text :- "))

print("\n\t\tEnter 1 to translate in Hindi")
print("\n\t\tEnter 2 to translate in marathi")
print("\n\t\tEnter 3 to translate in Gujrati")
print("\n\t\tEnter 4 to translate in German")
print("\n\t\tEnter 5 to translate in Spanish")
print("\n\t\tEnter 6 to translate in Japanese")
print("\n\t\tEnter 7 to translate in Korean")
print("\n\t\tEnter 8 to translate in Arabic")
print("\n\t\tEnter 9 to translate in Greek")
print("\n\t\tEnter 10 to translate in English")
print("\n\t\tEnter 0 to exit")

#To Stop The Program Enter enter 0

while True:
    x = int(input("ENTER YOUR CHOICE"))
    try:
        if x == 1:
            print("\n\t\tTranslating.........")
            Transalte = translator.translate(to='hi')
            print(f'\n\t\t{Transalte}')
            print("Enter 0 if you want to exit tha program")
            print("\n\t\tEnter 1 to translate in hindi")
            print("\n\t\tEnter 2 to translate in marathi")
            print("\n\t\tEnter 3 to translate in gujrati")
            print("\n\t\tEnter 4 to translate in german")
            print("\n\t\tEnter 5 to translate in spanish")
            print("\n\t\tEnter 6 to translate in japanese")
            print("\n\t\tEnter 7 to translate in korean")
            print("\n\t\tEnter 8 to translate in Arabic")
            print("\n\t\tEnter 9 to translate in Greek")
            print("\n\t\tEnter 10 to translate in English")
        if x == 2:
            print("\n\t\tTranslating.........")
            Transalte = translator.translate(to='mr')
            print(f'\n\t\t{Transalte}')
            print("Enter 0 if you want to exit tha program")
            print("\n\t\tEnter 1 to translate in hindi")
            print("\n\t\tEnter 2 to translate in marathi")
            print("\n\t\tEnter 3 to translate in gujrati")
            print("\n\t\tEnter 4 to translate in german")
            print("\n\t\tEnter 5 to translate in spanish")
            print("\n\t\tEnter 6 to translate in japanese")
            print("\n\t\tEnter 7 to translate in korean")
            print("\n\t\tEnter 8 to translate in Arabic")
            print("\n\t\tEnter 9 to translate in Greek")
            print("\n\t\tEnter 10 to translate in English")
        if x == 3:
            print("\n\t\tTranslating.........")
            Transalte = translator.translate(to='gu')
            print(f'\n\t\t{Transalte}')
            print("Enter 0 if you want to exit tha program")
            print("\n\t\tEnter 1 to translate in hindi")
            print("\n\t\tEnter 2 to translate in marathi")
            print("\n\t\tEnter 3 to translate in gujrati")
            print("\n\t\tEnter 4 to translate in german")
            print("\n\t\tEnter 5 to translate in spanish")
            print("\n\t\tEnter 6 to translate in japanese")
            print("\n\t\tEnter 7 to translate in korean")
            print("\n\t\tEnter 8 to translate in Arabic")
            print("\n\t\tEnter 9 to translate in Greek")
            print("\n\t\tEnter 10 to translate in English")
        if x == 4:
            print("\n\t\tTranslating.........")
            Transalte = translator.translate(to='de')
            print(f'\n\t\t{Transalte}')
            print("Enter 0 if you want to exit tha program")
            print("\n\t\tEnter 1 to translate in hindi")
            print("\n\t\tEnter 2 to translate in marathi")
            print("\n\t\tEnter 3 to translate in gujrati")
            print("\n\t\tEnter 4 to translate in german")
            print("\n\t\tEnter 5 to translate in spanish")
            print("\n\t\tEnter 6 to translate in japanese")
            print("\n\t\tEnter 7 to translate in korean")
            print("\n\t\tEnter 8 to translate in Arabic")
            print("\n\t\tEnter 9 to translate in Greek")
            print("\n\t\tEnter 10 to translate in English")
        if x == 5:
            print("\n\t\tTranslating.........")
            Transalte = translator.translate(to='es')
            print(f'\n\t\t{Transalte}')
            print("Enter 0 if you want to exit tha program")
            print("\n\t\tEnter 1 to translate in hindi")
            print("\n\t\tEnter 2 to translate in marathi")
            print("\n\t\tEnter 3 to translate in gujrati")
            print("\n\t\tEnter 4 to translate in german")
            print("\n\t\tEnter 5 to translate in spanish")
            print("\n\t\tEnter 6 to translate in japanese")
            print("\n\t\tEnter 7 to translate in korean")
            print("\n\t\tEnter 8 to translate in Arabic")
            print("\n\t\tEnter 9 to translate in Greek")
            print("\n\t\tEnter 10 to translate in English")
        if x == 6:
            print("\n\t\tTranslating.........")
            Transalte = translator.translate(to='ja')
            print(f'\n\t\t{Transalte}')
            print("Enter 0 if you want to exit tha program")
            print("\n\t\tEnter 1 to translate in hindi")
            print("\n\t\tEnter 2 to translate in marathi")
            print("\n\t\tEnter 3 to translate in gujrati")
            print("\n\t\tEnter 4 to translate in german")
            print("\n\t\tEnter 5 to translate in spanish")
            print("\n\t\tEnter 6 to translate in japanese")
            print("\n\t\tEnter 7 to translate in korean")
            print("\n\t\tEnter 8 to translate in Arabic")
            print("\n\t\tEnter 9 to translate in Greek")
            print("\n\t\tEnter 10 to translate in English")
        if x == 7:
            print("\n\t\tTranslating.........")
            Transalte = translator.translate(to='ko')
            print(f'\n\t\t{Transalte}')
            print("Enter 0 if you want to exit tha program")
            print("\n\t\tEnter 1 to translate in hindi")
            print("\n\t\tEnter 2 to translate in marathi")
            print("\n\t\tEnter 3 to translate in gujrati")
            print("\n\t\tEnter 4 to translate in german")
            print("\n\t\tEnter 5 to translate in spanish")
            print("\n\t\tEnter 6 to translate in japanese")
            print("\n\t\tEnter 7 to translate in korean")
            print("\n\t\tEnter 8 to translate in Arabic")
            print("\n\t\tEnter 9 to translate in Greek")
            print("\n\t\tEnter 10 to translate in English")
        if x == 8:
            print("\n\t\tTranslating.........")
            Transalte = translator.translate(to='ar')
            print(f'\n\t\t{Transalte}')
            print("Enter 0 if you want to exit tha program")
            print("\n\t\tEnter 1 to translate in hindi")
            print("\n\t\tEnter 2 to translate in marathi")
            print("\n\t\tEnter 3 to translate in gujrati")
            print("\n\t\tEnter 4 to translate in german")
            print("\n\t\tEnter 5 to translate in spanish")
            print("\n\t\tEnter 6 to translate in japanese")
            print("\n\t\tEnter 7 to translate in korean")
            print("\n\t\tEnter 8 to translate in Arabic")
            print("\n\t\tEnter 9 to translate in Greek")
            print("\n\t\tEnter 10 to translate in English")
        if x == 9:
            print("\n\t\tTranslating.........")
            Transalte = translator.translate(to='el')
            print(f'\n\t\t{Transalte}')
            print("Enter 0 if you want to exit tha program")
            print("\n\t\tEnter 1 to translate in hindi")
            print("\n\t\tEnter 2 to translate in marathi")
            print("\n\t\tEnter 3 to translate in gujrati")
            print("\n\t\tEnter 4 to translate in german")
            print("\n\t\tEnter 5 to translate in spanish")
            print("\n\t\tEnter 6 to translate in japanese")
            print("\n\t\tEnter 7 to translate in korean")
            print("\n\t\tEnter 8 to translate in Arabic")
            print("\n\t\tEnter 9 to translate in Greek")
            print("\n\t\tEnter 10 to translate in English")
        if x == 10:
            print("\n\t\tTranslating.........")
            Transalte = translator.translate(to='en')
            print(f'\n\t\t{Transalte}')
            print("Enter 0 if you want to exit tha program")
            print("\n\t\tEnter 1 to translate in hindi")
            print("\n\t\tEnter 2 to translate in marathi")
            print("\n\t\tEnter 3 to translate in gujrati")
            print("\n\t\tEnter 4 to translate in german")
            print("\n\t\tEnter 5 to translate in spanish")
            print("\n\t\tEnter 6 to translate in japanese")
            print("\n\t\tEnter 7 to translate in korean")
            print("\n\t\tEnter 8 to translate in Arabic")
            print("\n\t\tEnter 9 to translate in Greek")
            print("\n\t\tEnter 10 to translate in English")
        if x == 0:
            break
    except Exception as ex:
        # Error happens when you try more than 10 to 20 input in a day
        # because the textblob API gives you only 1000 words per day.
        # if you reached the limit the program will break with
        # this Opss Something Error Happens message....
        # Thank you for using the program.
        print("\n\t\tOpss Something Error Happens")
        break