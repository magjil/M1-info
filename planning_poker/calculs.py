# Retourne le choix ayant toutes les voix,
# ou None s'il n'y en a aucun

def unanimite (dicoChoix):

    choixVote = False
    elu = None

    for choix, nbVoix in dicoChoix.items ():

        if nbVoix > 0:
            # 2 choix distincts ont été votés
            if choixVote:
                return None

            choixVote = True
            elu = choix

    return elu


# Retourne le choix le plus voté d'un dictionnaire non vide,
# ou None s'il n'y a aucun vote

def majoriteRelative (dicoChoix):

    plusVote = 0

    for choix, nbVoix in dicoChoix.items ():

        if plusVote < nbVoix:
            plusVote = nbVoix
            elu = choix

    if plusVote == 0:
        elu = None

    return elu


# Retourne la priorité médiane parmi les votes,
# ou None s'il n'y a aucun vote

def mediane (dicoPriorites):

    nbVoixTotal = sum (dicoPriorites.values ())
    if nbVoixTotal == 0:
        return None
        
    nbVoixRestant = 0

    for priorite, nbVoix in dicoChoix.items ():
        nbVoixRestant += nbVoix

        # Médiane atteinte
        if 2 * nbVoixRestant > nbVoixTotal:
            elue = priorite

    return elue


# Retourne la priorité moyenne parmi les votes,
# ou None s'il n'y a aucun vote

def moyenne (dicoPriorites):

    nbVoixTotal = sum (dicoPriorites.values ())
    if nbVoixTotal == 0:
        return None

    valeur = 0

    for priorite, nbVoix in dicoChoix.items ():
        valeur += priorite * nbVoix

    return round (valeur / nbVoixTotal)
