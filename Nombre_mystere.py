from random import randint

number = randint(0, 100)
try_to_find = 5

print("Bienvenue sur le jeu du nombre mystère !")
while try_to_find > 0:
    print(f"Il te reste {try_to_find} essais")
    reply = input("Le nombre est : ")
    if not reply.isdigit():
        while reply.isdigit() == False:
            print("Ce n'est pas un chiffre")
            reply = input("Le nombre est : ")
    if not reply == number:
        try_to_find = try_to_find - 1
        if try_to_find == 0:
            print(f"Le nombre étais {number}")
        if int(reply) > number:
            print("Le nombre mystère est plus petit")
        elif int(reply) < number:
            print("Le nombre mystère est plus grand")
        elif int(reply) == number:
            print(f"Bravo ! Tu à gagné il te reste encore {try_to_find} essaie")
            break

