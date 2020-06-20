from newspaper import Article

urls_bfm = [
    'https://www.bfmtv.com/sante/coronavirus-trois-nouveaux-clusters-identifies-en-normandie_AV-202006200060.html',
    'https://www.bfmtv.com/sante/coronavirus-une-surmortalite-de-89-enregistree-en-ile-de-france_AD-202006200067.html',
    'https://www.bfmtv.com/sante/coronavirus-novartis-arrete-son-etude-sur-l-hydroxychloroquine-faute-de-participants_AD-202006200069.html',
    'https://www.bfmtv.com/sante/val-d-oise-l-apparition-de-27-cas-de-coronavirus-inquiete-a-sarcelles_AV-202006190082.html',
    'https://www.bfmtv.com/sante/coronavirus-dix-agents-contamines-au-chu-de-lille-les-syndicats-s-alarment_AV-202006190170.html',
    'https://www.bfmtv.com/economie/des-masques-made-in-france-pour-mieux-se-proteger-contre-le-coronavirus_AN-202006200111.html',
    'https://www.bfmtv.com/international/amerique-latine/bresil/bresil-plus-d-un-million-de-contaminations-au-coronavirus_AD-202006200027.html',
    'https://rmcsport.bfmtv.com/plus-de-sports/coronavirus-sports-collectifs-autorises-retour-du-public-les-annonces-de-matignon-1936409.html',
    'https://www.bfmtv.com/sante/coronavirus-14-deces-en-24h-la-baisse-en-reanimation-se-poursuit_AD-202006190234.html',
]

urls_20minutes = [
    'https://www.20minutes.fr/societe/2803615-20200620-coronavirus-bouches-rhone-contaminations-covid-19-ralentissent-chez-saisonniers',
    'https://www.20minutes.fr/sante/2778455-20200514-deconfinement-deuxieme-vague-inevitable-forcement-liee-covid',
    'https://www.20minutes.fr/societe/2803363-20200619-coronavirus-carcassonne-atteint-covid-ex-patient-reanimation-fait-don-neuf-respirateurs-hopital',
    'https://www.20minutes.fr/sante/2787559-20200527-coronavirus-persistance-symptomes-rechute-certains-patients-covid-fin',
    'https://www.20minutes.fr/sante/2801671-20200617-coronavirus-sait-dexamethasone-ameliore-survie-patients',
    'https://www.20minutes.fr/monde/2801127-20200616-coronavirus-elles-vont-pub-feter-deconfinement-16-amies-positives-covid-19-floride',
    'https://www.20minutes.fr/economie/2803463-20200619-coronavirus-faillites-liees-crise-toucheront-aussi-entreprises-bonne-sante-alerte-ofce',
    'https://www.20minutes.fr/sante/2803403-20200619-coronavirus-nombre-clusters-progresse-france-signe-reprise-epidemie',
    'https://www.20minutes.fr/monde/2801419-20200617-coronavirus-direct-pekin-lance-grande-vague-depistages-eviter-deuxieme-vague',
    'https://www.20minutes.fr/sante/2801671-20200617-coronavirus-sait-dexamethasone-ameliore-survie-patients',
]

urls_cnews = [
    'https://www.cnews.fr/france/2020-06-20/16-deces-en-24h-la-baisse-en-reanimation-continue-970049',
    'https://www.cnews.fr/monde/2020-06-20/nombre-de-morts-du-covid-19-contaminations-et-guerisons-le-bilan-de-la-pandemie',
    'https://www.cnews.fr/sport/2020-06-20/deconfinement-les-sports-collectifs-peuvent-reprendre-lundi-969947',
    'https://www.cnews.fr/videos/france/2020-06-20/covid-19-hausse-des-foyers-de-contaminations-969881',
    'https://www.cnews.fr/monde/2020-06-20/coronavirus-le-bresil-franchi-la-barre-du-million-de-cas-969866',
    'https://www.cnews.fr/france/2020-06-20/deconfinement-les-cinemas-et-casinos-rouvrent-ce-lundi-les-stades-le-11-juillet',
    'https://www.cnews.fr/france/2020-06-18/nombre-de-personnes-en-reanimation-nombre-de-deces-lhopital-regions-touchees-le',
    'https://www.cnews.fr/monde/2020-06-19/il-pourrait-ne-pas-y-avoir-dimmunite-contre-le-covid-19-selon-une-etude-969752',
    'https://www.cnews.fr/monde/2020-06-19/coronavirus-la-mort-dun-patient-diffusee-en-direct-la-television-bolivienne-969800',
]

urls_ouest_france = [
    'https://www.ouest-france.fr/sante/virus/coronavirus/une-facture-d-un-million-de-dollars-pour-un-survivant-du-covid-19-6868100',
    'https://www.ouest-france.fr/sante/virus/coronavirus/carcassonne-il-fait-don-de-neuf-respirateurs-au-service-de-reanimation-qui-l-sauve-du-covid-6876686',
    'https://www.ouest-france.fr/monde/bresil/le-chef-indigene-paiakan-grand-defenseur-de-la-foret-amazonienne-est-mort-du-covid-19-6873541'
    'https://www.ouest-france.fr/ile-de-france/sarcelles-95200/covid-19-sarcelles-les-tests-positifs-sont-pres-de-quatre-fois-superieurs-ceux-realises-en-ile-de-6873343',
    'https://www.ouest-france.fr/normandie/covid-19-de-nouveaux-clusters-identifies-en-normandie-le-seuil-d-alerte-depasse-6875653',
    'https://www.ouest-france.fr/pays-de-la-loire/nantes-44000/post-covid-nantes-les-artistes-reveillent-la-place-royale-6876674',
    'https://voilesetvoiliers.ouest-france.fr/croisiere/grande-croisiere/covid-19-bloquee-sur-son-voilier-aux-iles-caiman-une-canadienne-prepare-son-accouchement-e2e9d4c6-856c-11ea-9736-75ed782b32c8',
    'https://www.ouest-france.fr/sante/virus/coronavirus/privees-de-prime-covid-les-federations-de-l-aide-domicile-crient-l-injustice-6870763',
]

urls_dauphine = [
    'https://www.ledauphine.com/sante/2020/06/19/vaucluse-coronavirus-carpentras-un-cas-de-covid-19-detecte-au-college-alphonse-daudet-l-etablissement-ferme-lundi',
    'https://www.ledauphine.com/sante/2020/06/19/haute-savoie-coronavirus-actu-annecy-covid-19-la-fin-du-plan-blanc-a-l-hopital-d-annecy',
    'https://www.ledauphine.com/sante/2020/06/19/montelimar-suspicion-de-covid-19-pour-trois-collegiens-d-alain-borne',
    'https://www.ledauphine.com/sante/2020/06/18/ardeche-vaucluse-aubenas-valence-cluster-ardechois-38-personnes-testees-positives-au-covid-19',
    'https://www.ledauphine.com/faits-divers-justice/2020/06/20/sallanches-des-soignants-manifestent-pour-leurs-homologues-morts-du-covid-19',
    'https://www.ledauphine.com/sante/2020/06/20/six-organisateurs-du-meeting-de-trump-testes-positifs-au-coronavirus',
    'https://www.ledauphine.com/sante/2020/06/20/en-france-les-cinemas-et-casinos-rouvrent-lundi-les-stades-le-11-juillet',
    'https://www.ledauphine.com/magazine-automobile/2020/06/20/attention-au-gel-hydroalcoolique-il-est-dangereux-pour-votre-voiture',
    'https://www.ledauphine.com/sante/2020/06/15/un-collegien-de-6e-teste-positif-au-covid-19',
]

urls_lemonde = [
    'https://www.lemonde.fr/international/article/2020/06/20/coronavirus-le-bresil-depasse-le-million-de-cas-l-europe-les-2-5-millions-tandis-que-trump-defie-l-epidemie_6043594_3210.html',
    'https://www.lemonde.fr/planete/article/2020/06/20/covid-19-le-virus-circule-toujours-en-france-mais-reste-contenu_6043533_3244.html',
    'https://www.lemonde.fr/international/video/2020/06/20/le-bresil-a-longtemps-ete-efficace-contre-les-epidemies-jusqu-au-coronavirus_6043586_3210.html',
    'https://www.lemonde.fr/planete/article/2020/06/20/matignon-autorise-la-pratique-des-sports-collectifs-et-la-reouverture-des-casinos-des-lundi-celle-des-stades-a-partir-du-11-juillet_6043524_3244.html',
    'https://www.lemonde.fr/les-decodeurs/article/2020/06/19/coronavirus-combien-de-tests-pcr-pratiques-et-de-personnes-infectees-dans-votre-departement_6043484_4355770.html',
    'https://www.lemonde.fr/afrique/article/2020/06/19/en-pleine-pandemie-de-coronavirus-l-afrique-de-l-est-retient-son-souffle-avant-une-nouvelle-vague-de-criquets_6043391_3212.html',
    'https://www.lemonde.fr/international/article/2020/06/19/les-dirigeants-des-vingt-sept-prets-a-negocier-d-arrache-pied-le-plan-de-relance-post-covid_6043513_3210.html',
    'https://www.lemonde.fr/societe/article/2020/06/19/covid-19-des-pratiques-d-enfermement-illegales-dans-un-hopital-psychiatrique_6043411_3224.html',
]

urls_figaro = [
    'https://www.lefigaro.fr/sciences/covid-19-le-nombre-de-clusters-progresse-en-france-20200620',
    'https://www.lefigaro.fr/flash-eco/coronavirus-reouverture-des-cinemas-centres-de-vacances-casinos-et-salles-de-jeux-20200620',
    'https://www.lefigaro.fr/sciences/coronavirus-14-morts-en-24h-la-situation-se-degrade-en-normandie-20200619',
    'https://www.lefigaro.fr/sciences/coronavirus-situation-sous-controle-a-pekin-prison-au-chili-pour-non-respect-du-confinement-20200619',
    'https://www.lefigaro.fr/sciences/covid-19-novartis-arrete-son-etude-sur-l-hydroxychloroquine-faute-de-participants-20200620',
    'https://www.lefigaro.fr/flash-actu/coronavirus-didier-raoult-se-contredit-et-evoque-desormais-une-deuxieme-vague-epidemique-20200619',
    'https://www.lefigaro.fr/sciences/coronavirus-28-morts-en-24-heures-acceleration-du-virus-en-normandie-20200618',
    'https://www.lefigaro.fr/flash-actu/coronavirus-plus-de-2-000-morts-en-colombie-20200620',
]

urls_echos = [
    'https://www.lesechos.fr/industrie-services/services-conseils/coronavirus-la-vive-inquietude-du-monde-de-la-nuit-1217111',
    'https://www.lesechos.fr/sport/omnisport/virus-reouverture-des-stades-le-11-juillet-avec-5000-spectateurs-maximum-1217052',
    'https://www.lesechos.fr/monde/enjeux-internationaux/en-direct-le-20-juin-coronavirus-la-situation-en-france-et-dans-le-monde-1217039',
    'https://www.lesechos.fr/pme-regions/ile-de-france/universite-paris-saclay-un-fonds-de-recherches-sur-lepidemie-covid-19-1216959',
    'https://www.lesechos.fr/industrie-services/automobile/coronavirus-bmw-supprime-6000-postes-et-rompt-avec-daimler-1216933',
]

urls_lacroix = [
    'https://www.la-croix.com/Monde/Covid-19-lOMS-appelle-monde-prudence-2020-06-20-1201100880',
    'https://www.la-croix.com/Monde/Europe/Europe-quarante-jours-adopter-plan-relance-lUE-2020-06-20-1201100878',
    'https://www.la-croix.com/Religion/Catholicisme/Pape/Lhommage-pape-personnel-medical-Lombardie-2020-06-20-1201100888',
    'https://www.la-croix.com/France/Deconfinement-sports-collectifs-seront-autorises-lundi-2020-06-20-1201100891',
    'https://www.la-croix.com/Culture/Musique/Fete-musique-concerts-seront-ils-autorises-2020-06-20-1201100881',
    'https://www.la-croix.com/Economie/France/Defaillances-dentreprises-Covid-19-nexplique-pas-tout-2020-06-20-1201100853',
    'https://www.la-croix.com/JournalV2/Bettina-LavilleLEurope-est-elle-devenue-verte-2020-06-20-1101100801',
]

URLS = {'bfm': urls_bfm,
        '20minutes': urls_20minutes,
        'cnews': urls_cnews,
        'ouest-france': urls_ouest_france,
        'ledauphine': urls_dauphine,
        'lemonde': urls_lemonde,
        'lefigaro': urls_figaro,
        'lesechos': urls_echos,
        'lacroix': urls_lacroix}

