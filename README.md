# EDA-media-covid19
Analyse succinte des articles et réactions de la presse face aux Covid-19.

L'idée de ce projet est de réaliser une courte étude sur le contenu des articles de différents journaux traitant les sujets du Covid-19 en analysant les (sous-)thèmes 
et leur manière de l'aborder. Le but étant de pouvoir repérer :
* les journaux les plus pessimistes/optimistes, 
* les différentes thématiques abordées, 
* le style utilisé
* etc.

## Getting Started

### Data
L'analyse s'est basée sur 5 à 10 articles choisis pour chacun des 8 journaux (quotidiens) français préselectionnés. Ces données ont été scrapées depuis le web via <a href='https://newspaper.readthedocs.io/en/latest/'>newspaper3k</a>.
Les articles datent du 18 au 20 juin 2020. 

### Features
* Analyse de sentiments (positivité vs négativité),
* Subjectivité,
* Identification de thématiques (LDA),
* Nuages de mots, 
* Champs lexical (morbidité, santé...)
* Génération de texte, 
* etc.

## Dependencies

Les librairies utilisées :
* newspaper3k
* tensorflow
* pandas
* numpy
