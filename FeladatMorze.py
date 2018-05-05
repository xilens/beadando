import string

Morze = {'A': '.-', 'B': '-...', 'C': '-.-.',
        'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..',
        'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-',
        'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',

        '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..',
        '9': '----.'
        }

def SimaToMorze(szoveg):
    morze=" "
    for betu in szoveg:
        if betu not in string.punctuation:
            if betu == " ":
                morze+="/ "
            else:
                morze+=Morze[betu.upper()]+" "
    return morze[:-1]

def MorzeToSima(morze):
    karakterek = morze.split(" ")
    newstr = ""
    for szo in karakterek:
        for betu, kod in Morze.items():
            if szo == "/":
                newstr += " "
                break
            elif szo == kod:
                newstr += betu
                break
    return newstr[0]+newstr[1:].lower()

# szoveg=input("Irj be valamit(szoveg):")
# x=SimaToMorze(szoveg)
# print(x)
#
# y=MorzeToSima(x)
# print(y)
