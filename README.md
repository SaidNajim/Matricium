# Matricium
Un outil puissant de calcul matriciel
<p class="has-line-data" data-line-start="0" data-line-end="13">Objectifs :<br>
o   La conception d’une structure permettant une écriture intuitive des matrices.<br>
o   La création d’une grande variété de méthodes agissant sur une ou plusieurs matrices (Scaling)(2)<br>
o   Conception d’une interface d’utilisateur facile à l’utilisation, en se basant sur l’expérience de plusieurs testeurs et disponible sur toutes les plateformes.<br>
Implémentation :<br>
L’écriture d’une matrice :<br>
Le premier problème qui s’est posé est la manière de l’insertion d’une matrice dans un code python<br>
   La solution a été inspirée d’une vidéo de « Python Arabic Community » qui s’intitule « Algorithmes 5 | Structures de données : exemples et application »<br>
L’entrée d’une matrice par un utilisateur est réglée par :<br>
   La création d’une fonction dédiée s’appelant « create_matrice »(3) demandant les paramètres nécessaires (le nom de la matrice, le nombre de lignes/colonnes et les coefficients de chaque ligne séparés par des espaces), puis la création d’un objet selon les paramètres entrés (La nomination de l’objet est réalisée par la fonction ‘‘globals( )’’) et enfin l’ajout du nom de la matrice à la base de données contenant les noms des matrices actives.<br>
Les opérations sur les matrices :<br>
   L’accès aux coefficients d’une matrice est réalisé par une boucle sur les lignes de la matrice puis une autre boucle sur les éléments de chaque ligne, afin de traiter ces coefficients selon l’opération et les stocker dans un objet temporaire susceptible d’être enregistré, crée par la fonction « create_temp_object ».<br>
   Le traitement sur les coefficients est purement tiré de formules mathématiques citées dans le cours de notre Professeur de Maths M.Abdelali Dreif.<br>
téléchargement:<br>
-- Pour télécharger notre programme :<br>
Cliquez sur "Code"<br>
Download ZIP<br>
Bon Usage !!!<br>
L'équipe de matricium <3</p>
