from random import randint

health = 50
enemy_health = 50
number_of_bottle = 3

while health == 0 | enemy_health == 0:
    choice = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? : ")
    choice = int(choice)

    if not choice == 1 | 2:
        continue
    else:
        if choice == 1:
            attack = randint(5, 10)
            enemy_health -= attack

        else:
            number_of_bottle -= 1
            heal = randint(15, 50)
            heal += health

