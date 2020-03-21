"""

Bonjour bienvenue sur mon programme pour calculer votre note en course de 3x500m selon votre temps total.

Le barème est celui l'Education Nationale (de l'année 2019).
La note de course est sur 14 points, puis il y à 4 points sur le respect du temps annoncé et 2 points sur l'échauffement.

"""


from datetime import timedelta

print()
print("Si tu veux plus d'informations sur le bareme, le voici: ")
print()
print("http://www.lycee-international.ac-versailles.fr/IMG/pdf/demi-fond-bacgt-n4-2019.pdf")
print()
print("Maintenant rentre tes temps de la manière dont on te le demande.")


try:
    td1 = timedelta(minutes=float(input("Nombre de Minutes du 1er temps: ")),
                    seconds=float(input("Nombre de Secondes du 1er temps: ")))
    td2 = timedelta(minutes=float(input("Nombre de Minutes du 2eme temps: ")),
                    seconds=float(input("Nombre de Secondes du 2eme temps: ")))
    td3 = timedelta(minutes=float(input("Nombre de Minutes du 3eme temps: ")),
                    seconds=float(input("Nombre de Secondes du 3eme temps: ")))

    tf = td1 + td2 + td3

    print()
    print()
    print('{} + {} + {} = {}'.format(td1, td2, td3, tf))
    print()

    sexe = str(input("Es-tu un Homme ou une Femme (écrit 'H' ou 'F') : "))

    print(sexe)
    print()

except ValueError or NameError:
    print()
    print("Erreur :")
    print("Aucun temps n'a été rentré ou alors il n'a pas été rentré correctement.")
    print("Relance le programme.")
    sexe = None
    tf = None

if sexe == "H":
    if tf <= timedelta(minutes=4, seconds=10):
        print("GG A TOI TU AS 14/14 !!")
    elif tf <= timedelta(minutes=4, seconds=15):
        print("Ta note sera de 13.3/14")
        print()
        print("La prochaine étape est à 4:10 pour une note de 14/14 !")
    elif tf <= timedelta(minutes=4, seconds=19):
        print("Ta note sera de 12.6/14")
        print()
        print("La prochaine étape est à 4:15 pour une note de 13.3/14")
    elif tf <= timedelta(minutes=4, seconds=24):
        print("Ta note sera de 11.9/14")
        print()
        print("La prochaine étape est à 4:19 pour une note de 12.6/14")
    elif tf <= timedelta(minutes=4, seconds=29):
        print("Ta note sera de 11.2/14")
        print()
        print("La prochaine étape est à 4:24 pour une note de 11.9/14")
    elif tf <= timedelta(minutes=4, seconds=34):
        print("Ta note sera de 10.5/14")
        print()
        print("La prochaine étape est à 4:29 pour une note de 11.2/14")
    elif tf <= timedelta(minutes=4, seconds=40):
        print("Ta note sera de 9.8/14")
        print()
        print("La prochaine étape est à 4:34 pour une note de 10.5/14")
    elif tf <= timedelta(minutes=4, seconds=48):
        print("Ta note sera de 9.1/14")
        print()
        print("La prochaine étape est à 4:40 pour une note de 9.8/14")
    elif tf <= timedelta(minutes=4, seconds=56):
        print("Ta note sera de 8.4/14")
        print()
        print("La prochaine étape est à 4:48 pour une note de 9.1/14")
    elif tf <= timedelta(minutes=5, seconds=5):
        print("Ta note sera de 7.7/14")
        print()
        print("La prochaine étape est à 4:56 pour une note de 8.4/14")
    elif tf <= timedelta(minutes=5, seconds=14):
        print("Ta note sera de 7/14")
        print()
        print("La prochaine étape est à 5:05 pour une note de 7.7/14")
    elif tf <= timedelta(minutes=5, seconds=24):
        print("Ta note sera de 6.3/14")
        print()
        print("La prochaine étape est à 5:14 pour une note de 7/14")
    elif tf <= timedelta(minutes=5, seconds=37):
        print("Ta note sera de 5.6/14")
        print()
        print("La prochaine étape est à 5:24 pour une note de 6.3/14")
    elif tf <= timedelta(minutes=5, seconds=53):
        print("Ta note sera de 4.9/14")
        print()
        print("La prochaine étape est à 5:37 pour une note de 5.6/14")
    elif tf <= timedelta(minutes=6, seconds=10):
        print("Ta note sera de 4.2/14")
        print()
        print("La prochaine étape est à 5:53 pour une note de 4.9/14")
    elif tf <= timedelta(minutes=6, seconds=28):
        print("Ta note sera de 3.5/14")
        print()
        print("La prochaine étape est à 6:10 pour une note de 4.2/14")
    elif tf <= timedelta(minutes=6, seconds=49):
        print("Ta note sera de 2.8/14")
        print()
        print("La prochaine étape est à 6:28 pour une note de 3.5/14")
    elif tf <= timedelta(minutes=7, seconds=11):
        print("Ta note sera de 2.1/14")
        print()
        print("La prochaine étape est à 6:49 pour une note de 2.8/14")
    elif tf <= timedelta(minutes=7, seconds=38):
        print("Ta note sera de 1.4/14")
        print()
        print("La prochaine étape est à 7:11 pour une note de 2.1/14")
    elif tf <= timedelta(minutes=8, seconds=5):
        print("Ta note sera de 0.7/14")
        print()
        print("La prochaine étape est à 7:38 pour une note de 1.4/14")
    elif tf > timedelta(minutes=8, seconds=5):
        print("Ta note sera de 0/14")
        print()
        print("La prochaine étape est à 8:05 pour une note de 0.7/14")

elif sexe == "F":
    if tf <= timedelta(minutes=5, seconds=30):
        print("GG A TOI TU AS 14/14 !!")
    elif tf <= timedelta(minutes=5, seconds=35):
        print("Ta note sera de 13.3/14")
        print()
        print("La prochaine étape est à 5:30 pour une note de 14/14 !")
    elif tf <= timedelta(minutes=5, seconds=41):
        print("Ta note sera de 12.6/14")
        print()
        print("La prochaine étape est à 5:35 pour une note de 13.3/14")
    elif tf <= timedelta(minutes=5, seconds=47):
        print("Ta note sera de 11.9/14")
        print()
        print("La prochaine étape est à 5:41 pour une note de 12.6/14")
    elif tf <= timedelta(minutes=5, seconds=55):
        print("Ta note sera de 11.2/14")
        print()
        print("La prochaine étape est à 5:47 pour une note de 11.9/14")
    elif tf <= timedelta(minutes=6, seconds=3):
        print("Ta note sera de 10.5/14")
        print()
        print("La prochaine étape est à 5:55 pour une note de 11.2/14")
    elif tf <= timedelta(minutes=6, seconds=17):
        print("Ta note sera de 9.8/14")
        print()
        print("La prochaine étape est à 6:03 pour une note de 10.5/14")
    elif tf <= timedelta(minutes=6, seconds=31):
        print("Ta note sera de 9.1/14")
        print()
        print("La prochaine étape est à 6:17 pour une note de 9.8/14")
    elif tf <= timedelta(minutes=6, seconds=47):
        print("Ta note sera de 8.4/14")
        print()
        print("La prochaine étape est à 6:31 pour une note de 9.1/14")
    elif tf <= timedelta(minutes=7, seconds=3):
        print("Ta note sera de 7.7/14")
        print()
        print("La prochaine étape est à 6:47 pour une note de 8.4/14")
    elif tf <= timedelta(minutes=7, seconds=20):
        print("Ta note sera de 7/14")
        print()
        print("La prochaine étape est à 7:03 pour une note de 7.7/14")
    elif tf <= timedelta(minutes=7, seconds=38):
        print("Ta note sera de 6.3/14")
        print()
        print("La prochaine étape est à 7:20 pour une note de 7/14")
    elif tf <= timedelta(minutes=7, seconds=56):
        print("Ta note sera de 5.6/14")
        print()
        print("La prochaine étape est à 7:38 pour une note de 6.3/14")
    elif tf <= timedelta(minutes=8, seconds=15):
        print("Ta note sera de 4.9/14")
        print()
        print("La prochaine étape est à 7:56 pour une note de 5.6/14")
    elif tf <= timedelta(minutes=8, seconds=37):
        print("Ta note sera de 4.2/14")
        print()
        print("La prochaine étape est à 8:15 pour une note de 4.9/14")
    elif tf <= timedelta(minutes=8, seconds=59):
        print("Ta note sera de 3.5/14")
        print()
        print("La prochaine étape est à 8:37 pour une note de 4.2/14")
    elif tf <= timedelta(minutes=9, seconds=24):
        print("Ta note sera de 2.8/14")
        print()
        print("La prochaine étape est à 8:59 pour une note de 3.5/14")
    elif tf <= timedelta(minutes=9, seconds=50):
        print("Ta note sera de 2.1/14")
        print()
        print("La prochaine étape est à 9:24 pour une note de 2.8/14")
    elif tf <= timedelta(minutes=10, seconds=20):
        print("Ta note sera de 1.4/14")
        print()
        print("La prochaine étape est à 9:50 pour une note de 2.1/14")
    elif tf <= timedelta(minutes=10, seconds=50):
        print("Ta note sera de 0.7/14")
        print()
        print("La prochaine étape est à 10:20 pour une note de 1.4/14")
    elif tf > timedelta(minutes=10, seconds=50):
        print("Ta note sera de 0/14")
        print()
        print("La prochaine étape est à 10:50 pour une note de 0.7/14")

else:
    if sexe == None:
        print()
    else:
        print("Erreur :")
        print("Tu n'a pas ou mal indiqué ton genre, rentre 'F' ou 'H'.")
        print("Relance le programme.")
