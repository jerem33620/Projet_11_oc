# Projet_11_oc

## Améliorez un projet existant en Python

“ô rage ! ô désespoir ! ô vieillesse ennemie ! N’ai-je donc tant vécu que pour cette infamie ?” vous exclamez-vous en découvrant dans votre boîte mail un message de votre dernier client, pourtant si content lors de la dernière mise en production.


## Liens:

- Lien Github: https://github.com/jerem33620/Projet_11_oc


## Fonctionnalités:

Basez-vous sur l’un des projets que vous avez déjà réalisés dans ce parcours de formation ou dans votre carrière. Choisissez une fonctionnalité à ajouter. Elle doit être assez importante pour justifier des tests fonctionnels. Votre mentor jouera le rôle du client. Jouez le jeu et communiquez avec lui de la même manière que vous le feriez avec un client : soignez votre présentation, l’endroit où se déroule votre session de mentorat et l’orthographe dans vos e-mails !

Quant aux tests, cassez-en un puis réparez-le en le refactorant. Je suis sûre que vous avez un test caché quelque part qui mérite une nouvelle jeunesse !


## Livrables:

- Code source modifié et hébergé sur Github. Il inclut les commits d’ajout de la nouvelle fonctionnalité et de correction des tests (soignez vos messages !).
- E-mails de réponse au client : première réponse prenant bien note de la menace en production, seconde réponse informant de la correction du bug et troisième réponse présentant votre nouveau travail (ajout de la fonctionnalité demandée).
- Document écrit expliquant votre démarche de création, les difficultés rencontrées et la manière dont vous les avez résolues. Le document doit être en format pdf et ne pas excéder 2 pages A4. Il peut être rédigé en anglais ou en français, au choix, mais prenez bien en considération que les fautes d’orthographe et de grammaire seront évaluées !


## Contraintes:

- Votre code est sur Github et comporte un historique de commits cohérent,
- Votre code est écrit en anglais : commentaires, variables, …
- Votre nouvelle fonctionnalité inclut des tests unitaires et fonctionnels. Vous pouvez coder en TDD si vous le souhaitez.


### Installer:

Pour installer et faire fonctionner mon projet vous aurez besoin de certains packages et vous aurez besoin de clonner mon projet de github sur votre machine avec git:

```
- $ git clone https://github.com/jerem33620/Projet_11_oc
```

Puis, pour les packages:

```
- $ python -m pip install pipenv
- $ python -m pipenv install --dev
```

Enfin pour rajouter les produits dans la DataBase:

```
- $ python manage.py openfood
```

## Tests:

Pour lancer votre tests vous devrez utiliser les lignes de code suivante:

```
- $ coverage run --source= manage.py test
- $ coverage report
```

ou sinon:

```
- $ python manage.py test
```

### Activer votre projet en local:

Il faudra lancer 2 commandes et vous aurez le projet d'activé.

```
- $ python -m pipenv shell

- $ python manage.py runserver
```
