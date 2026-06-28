import pyperclip as pc

mode = "Fancy"

scramble = pc.paste().split()
scrambleAsDebugString = pc.paste()

inverse = []

for i in scramble:
    if i[-1] == "2":
        inverse.append(i)
    elif i[-1] == "'":
        inverse.append(i[0])
    else:
        inverse.append(i[0] + "'")

inverse.reverse()

str = ""

for i in inverse:
    str += i + " "

str.rstrip(" ")
if mode == "Fancy":
    print("Den omvendte blanding er: " + str)
    pc.copy(str)
    print("Blandingen er blevet kopieret til dit clipboard.")
    print("Tryk Enter for at lukke programmet.")
    print("Tryk mellemrum og derefter Enter for at kopiere start-tekst til FMC noter.")

x = " "

if mode == "Fancy":
    x = input("Skriv x og tryk Enter for at gendanne dit gamle clipboard: ")
    if x.lower() == "x":
        pc.copy(scrambleAsDebugString)
if x == " ":
    notes = "Scramble: "
    notes += scrambleAsDebugString
    notes += "\n\n"
    notes += "Inverse: "
    notes += str
    pc.copy(notes)