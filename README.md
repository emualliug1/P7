# Projet 7
## AlgoInvest&Trade

### Objectif :
Étape 1 : Créer un algorithme brute force qui rechercher les meilleures actions dans un fichier csv de 20 actions.

Étape 2 : Créer un algorithme optimisé qui recherche les meilleures actions dans un fichier csv de 1000 actions.

Étape 3 : afficher le rendu des 2 algorithmes.

### Commencer :
Assurez-vous que python est installé sur votre machine :

    python -V

Vérifiez que vous disposez du module venv :
    
    python -m venv --help
  
Si Python n'est pas installé sur votre machine :
    
    https://www.python.org/downloads/
    
Si vous ne disposez pas du module virtual env:
    
    py -m pip install --user virtualenv
    

### Une fois Python installé :
   
 Ouvrir une invite de commande et utiliser la commande :`cd` pour aller dans le repertoire ou vous voulez copier le projet. 
    Vous pouvez aussi créer un nouveau repertoire avec la commande: `mkdir`
    Une fois dans le bon repertoire il vous suffit de taper: 
 
    git clone https://github.com/emualliug1/P7
    
Créer un environnement virtuel avec venv :`python -m venv ***nom de l'environnement***` : pour créer l'environnement virtuel --- exemple : 

    py -m venv env
    
Activez l'environnement virtuel : `***nom de l'environnement***/Scripts/activate.bat` --- exemple : 

    env/Scripts/activate.bat
    
Installez les packages avec pip: 

    pip install -r requirements.txt

Lancez le programme avec : 

    python main.py