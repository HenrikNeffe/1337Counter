
DennisCounter = 0
HenrikCounter = 0
JulienCounter = 0
OleCounter = 0
with open('Chat.txt',encoding="utf8") as f:
    contents = f.readlines()
    #print(contents)

for line in contents:
    print(line)

    if "13:37" in line and "1337" in line and "Gülli" in line: #Dennis Counter
        DennisCounter += 1

    if "13:37" in line and "1337" in line and "Henrik" in line: #Henrik Counter
        HenrikCounter += 1

    if "13:37" in line and "1337" in line and "Der Oberaal ALLA" in line: #Julien Counter
        JulienCounter += 1

    if "13:37" in line and "1337" in line and "Ole Mc Oleson" in line: #Ole Counter
        OleCounter += 1
        
print("Dennis:",DennisCounter)
print("Henrik:",HenrikCounter)
print("Julien:",JulienCounter)
print("Ole:",OleCounter)