import string

def SimaToPigLatin(szoveg):
    szavak=szoveg.split(" ")
    nstr=""
    for szo in szavak:
        if szo[len(szo)-1] in string.punctuation:
            nstr += szo[1:-1]+szo[0]+"ay"+szo[len(szo)-1]+" "
        else:
            nstr += szo[1:] + szo[0] + "ay"+" "
    nstr=nstr.lower()
    return nstr[0].upper()+nstr[1:-1]

def PigLatinToSima(szoveg):
    szavak=szoveg.split(" ")
    nstr=""
    for szo in szavak:
        if szo[len(szo)-1] in string.punctuation:
            nstr += szo[len(szo) - 4] + szo[:-4] + szo[len(szo) - 1]+" "
        else:
            nstr += szo[len(szo) - 3] + szo[:-3] + " "
    nstr=nstr.lower()
    return nstr[0].upper()+nstr[1:-1]

# szoveg=input("Irj valamit:")
#
# x=SimaToPigLatin(szoveg)
# print(x)
#
# y=PigLatinToSima(x)
# print(y)