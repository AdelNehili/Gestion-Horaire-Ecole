L'idée de ce projet se base sur une représentation tourné vers le graphDB.
Pour faciliter l'accès/interprétation des données, une couche d'OO a été ajoutée.

Hypothèse de ce projet:
    -Chaque séance de cours est un acteur différent. (un cours a 10 séances de 2heures aura 10 acteurs)
    -Chaque acteur est lié dès qu'au moins un professeur/assistant/élève est partagé entre ces deux acteurs.
        -Ex: 10 séances de 2heures d'un cours se traduira par 10 acteurs tous liés entre eux car élèves/prof/assisstant en commun
    -L'heuristique de moindre couleur sera appliqué. Le but étant qu'un slote horaire corresponde à une couleur.
        Le but ici est d'avoir le moins de couleur possible tout en s'assurant qu'aucuns acteurs liés ne soient de
        la même couleur. Pour cela, il faudra commencer à donner des couleurs aux nodes aillant le plus de degrees.


Le but des classes.
    _MatrixMaster:
        Son but est de lire une matrice et de la traduire de manière cohérante dans le graphDB. Aussi, elle permet de
            traduire certaines informations de sorte à ce que networkx puisse travailler.

    _G_Manager:
        Son but est de create/update le graph et d'offrir un confort pour les accès aux attributs des nodes. Enfin,
            son rôle est aussi de créer une liste décroissante de nodes en fonction du degree qu'ils ont. Cette classe
            est donc centrale pour appliquer l'heuristique de moindre couleur (voir hypothèse)
