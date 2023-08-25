kuha = float(input("Kuika pitkä kuha on?: "))
if kuha<37:
    print("palauta kuha järveen, koska se on alle 37 cm")


hyttiluokka = (input("mikä hyttiluokka?: "))
if hyttiluokka == "LUX":
    print("Sinulla on parvekkeellinen hytti yläkannella.")
if hyttiluokka == "A":
    print("Sinulla on ikkunallinen hytti autokannen yläpuolella.")
if hyttiluokka == "B":
    print("Sinulla on ikkunaton hytti autokannen yläpuolella.")
if hyttiluokka == "C":
    print("Sinulla on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka")



