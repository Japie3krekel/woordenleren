import random

i = 0
gebruiktewoordenlijst = 'placeholder.txt'
wordlist = []
wordcount = 0
print('welke woordenlijst wil je gebruiken?')
gebruiktewoordenlijst = input() + '.txt'
with open (gebruiktewoordenlijst, 'rt') as woordenlijst:
    for woord in woordenlijst:
        woord = woord[:-1]
        wordcount = wordcount + 1
        wordlist.append(woord)
    wordcount = wordcount/2
    print('Deze woordenlijst bestaat uit:', wordcount, 'woorden')
    print('Laten we beginnen met het afnemen van de woorden.')
    while i != wordcount:
        huidigwoord = random.randrange(0, wordcount, 1) * 2
        print('wat betekent:' ,wordlist[huidigwoord], '?')
        antwoord = str(input())
        if antwoord == (str(wordlist[huidigwoord + 1])):
            print('dat is correct')
            del wordlist[huidigwoord];
            del wordlist[huidigwoord];
            wordcount = wordcount - 1
        else:
            print('sorry dat antwoord is niet correct')
            print('het juiste antwoord was:', wordlist[huidigwoord + 1])
            onterechtfout = input('vind je dat je antwoord toch correct is typ dan wel druk anders op enter.', ) 
            if onterechtfout == 'wel':
                del wordlist[huidigwoord];
                del wordlist[huidigwoord];
                wordcount = wordcount - 1
            else:
                print('fout')
    else:
        print('goed gedaan je hebt ze nu allemaal goed')
