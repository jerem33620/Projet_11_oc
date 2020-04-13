import requests

    
def get_json(category):
    """ Cette méthode produit la requête, 
        soumet une requête à la bibliothéque
        et retourne un json avec les valeurs rendues
    """

    base_url = 'https://fr.openfoodfacts.org/cgi/search.pl'

    params = {
        "action": "process",
        "tagtype_0": "categories",
        "tag_contains_0": "contains",
        "tag_0": category,
        "json": 1,
        "page_size": 500,
    }

    response = requests.get(base_url, params=params)
    products = []
    if response.status_code == 200:
        products = response.json()["products"]

    return products
