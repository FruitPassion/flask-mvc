
# Cette fonction permet de convertir un objet de type sqlalchemy.engine.row.Row en dictionnaire ou liste
# de dictionnaires
# Il peut etre utilisé dans le cas d'une requete qui retourne un seul ou plusieurs éléments
def convert_to_dict(elements):
    element_list = []
    if str(type(elements)) == "<class 'sqlalchemy.engine.row.Row'>":
        element_list = elements.__dict__
    else:
        try:
            for element in elements:
                element_list.append(element.__dict__)
        except:
            for element in elements:
                element_list.append(element._asdict())
    return element_list
