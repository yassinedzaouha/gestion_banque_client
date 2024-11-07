import csv 
import random

def login(role):
    id = input("\n\n \t\t--------> donner votr numero :  ")
    mp = input("\n\n \t\t--------> donner vote mot de passe :  ")
    test = False
    for i in role:
        if i["user"] == id and i["Mpass"] == mp:
            print("\n \t\t##########--------> Vous êtes connecté <--------##########")
            menu_agent()
            test = True
            break
    if test == False:
        print("\n \t\t--------> votr num ou le mot de passe est incorrect")
        choix_role()

def ListAgent():
    fichier = open("agent.csv", "r")
    read = csv.DictReader(fichier , delimiter = ";")
    agent= [row for row in read] 
    fichier.close()
    return agent

def ListClients():
    fichier = open("client.csv", "r")
    read = csv.DictReader(fichier , delimiter = ";")
    client = [row for row in read] 
    fichier.close()
    return client

def ajouterClient():
    fichier = open("nb_client.txt", "r")
    id = int(fichier.read()) + 1
    fichier.close()
    fichier = open("nb_client.txt", "w")
    fichier.write(str(id))
    fichier.close()
    Mpass = "MPC" + str(id)
    n_com = str(id) + str(random.randint(1,99))
    solde  = -1
    while solde < 0 :
        solde = float(input("\n\n \t\t--------> donner le solde initial (positif) :  "))
    fichier = open("client.csv", "a")
    ecrivainCSV = csv.writer(fichier, delimiter = ";")
    ecrivainCSV.writerow([id , Mpass , n_com , solde ]) 
    fichier.close()
    print("\n \t\t##########--------> Client a été ajouté <--------##########")
    menu_agent()

def SupprimerClient():
    clients = ListClients()
    for i in clients:
        print(i)
    c_num = input("\n\n \t\t--------> Donner le numéro du client à supprimer :   ")
    test = 5
    while test != "oui" and test !="OUI" and test !="yes" and test !="YES" and test !="non" and test !="NON" and test !="no" and test !="NO":
        test = input("\n\n \t\t--------> confermer la suppression de votre compte oui / non :   ")
    if test == "oui" or test == "OUI" or test == "yes" or test == "YES" :
        fichier = open("client.csv", "w")
        modifierCSV = csv.DictWriter(fichier, delimiter = ";" , fieldnames = clients[0].keys())
        modifierCSV.writeheader()
        suppr = False
        for i in clients:
            if i["c_num"] != c_num:
                modifierCSV.writerow(i)
            else :
                print(f"\n \t\t##########--------> Client {c_num} supprimé <--------##########")
                suppr = True
        fichier.close()
        if suppr == False:
            print(f"\n \t\t--------> Aucun client trouvé avec le numéro {c_num}.")
    else :
        print("\n \t\t--------> la suppression est annuler")
    menu_agent()

def SaveClients(clients):
    fichier = open("client.csv", "w")
    save_news = csv.DictWriter(fichier, delimiter = ";" , fieldnames = clients[0].keys())
    save_news.writeheader()
    for i in clients:
        save_news.writerow(i)
    fichier.close()

def modifierMP(id):
    novou_Mpass = input("\n\n \t\t--------> donner la nouvelle mot de passe :   ")
    clients = ListClients()
    for i in clients:
        if i["c_num"] == id:
            i["Mpass"] = novou_Mpass
            print("\n \t\t##########--------> le mot de pass a change <--------##########")
    SaveClients(clients)
    menu_client()

def afficherSolde(id):
    clients = ListClients()
    for i in clients:
        if i["c_num"] == id:
            print(f"\n \t\t##########--------> le solde disponible est : {i["solde"]} <--------##########")
    menu_client()

def DéposerSolde(id):
    solde_depos = -5
    while solde_depos <= 0:
        solde_depos = float(input("\n\n \t\t--------> Entrez le mantant que vous souhaitez augmenter (positif) :   "))
    clients = ListClients()
    for i in clients:
        if i["c_num"] == id:
            i["solde"] = float(i["solde"]) + solde_depos
            print("\n \t\t##########--------> le mantant a été déposer <--------##########")
    SaveClients(clients)
    menu_client()

def RetirerSolde(id):
    solde_retir = -5
    while solde_retir <= 0:
        solde_retir = float(input("\n\n \t\t--------> Entrez le mantant que vous voulez retirer (positif) :   "))
    clients = ListClients()
    test = False
    for i in clients:
        if i["c_num"] == id and float(i["solde"]) >= solde_retir:
            i["solde"] = float(i["solde"]) - solde_retir
            test = True
            print("\n \t\t##########--------> le mantant a été Retier <--------##########")
            break
    if test == False :
        print("\n \t\t--------> Erreur! ,le mantant plus que le solde disponible")
    SaveClients(clients)
    menu_client()

def menu_agent():
    print("\t\t\t\t\t  **************** liste de services: ********************")
    print("\t\t\t\t\t  -------------------------------------------------------")
    print("\t\t\t\t\t | 1 --> Ajouter un Compte                               |")
    print("\t\t\t\t\t | 2 --> Supprimer un Compte                             |")
    print("\t\t\t\t\t | 3 --> Afichier clients                                |")
    print("\t\t\t\t\t | 4 --> Quitter                                         |")
    print("\t\t\t\t\t  -------------------------------------------------------")
    num_serv = input("\n\n \t\t--------> entrez le numero de service  :    ")
    match num_serv:
        case "1" :
            ajouterClient()
        case "2" :
            SupprimerClient()
        case "3" :
            choix_role()
        case _:
            print("\n \t\t--------> Errur!, Entrez un nombre onter 1 et 3 :   ")
            menu_agent()

def menu_client():
    print("\t\t\t\t\t  **************** liste de services: ********************")
    print("\t\t\t\t\t  --------------------------------------------------------")
    print("\t\t\t\t\t | 1 --> Modifier votre mot de passe                      |")
    print("\t\t\t\t\t | 2 --> Afficher votre solde                             |")
    print("\t\t\t\t\t | 3 --> Déposer une somme d’argent                       |")
    print("\t\t\t\t\t | 4 --> Retirer une somme d’argent                       |")
    print("\t\t\t\t\t | 5 --> Quitter                                          |")
    print("\t\t\t\t\t  --------------------------------------------------------")
    num_serv = input("\n\n \t\t--------> entrez le numero de service  :    ")
    match num_serv:
        case "1" : 
            modifierMP(id)
        case "2" :
            afficherSolde(id)
        case "3" :
            DéposerSolde(id)
        case "4" :
            RetirerSolde(id)
        case "5" :
            choix_role()
        case _:
            print("\n \t\t--------> Errur!, Entrez un nombre onter 1 et 5 :   ")
            menu_client()

def Quitter():
    print("\n \t\t##########--------> merci pour votre visite <--------##########")
    exit()

def choix_role():
    print("\t\t\t\t\t  **************** choisier ton role: ********************")
    print("\t\t\t\t\t  -------------------------------------------------------")
    print("\t\t\t\t\t | 1 --> Agent                                            |")
    print("\t\t\t\t\t | 2 --> Client                                           |")
    print("\t\t\t\t\t | 3 --> Quitter                                          |")
    print("\t\t\t\t\t  -------------------------------------------------------")
    role_user = input("\n\n \t\t--------> entrez le numero de ton role  :    ")
    match role_user:
        case "1" :
            role = ListAgent()
            login(role)
        case "2" :
            role = ListClients()
            login(role)
        case "3" :
            Quitter()
        case _:
            print("\n \t\t--------> Errur!, Entrez un nombre onter 1 et 3 :   ")
            choix_role()

choix_role()
