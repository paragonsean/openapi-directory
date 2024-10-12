from typing import List, Dict
from aiohttp import web

from openapi_server.models.erreur import Erreur
from openapi_server.models.listenoire_reponse import LISTENOIREReponse
from openapi_server import util


async def set_liste_noire(request: web.Request, keyid, setliste_noire, num) -> web.Response:
    """Ajoute un numero en liste noire

    Ajoute un numero en liste noire. Une fois ajouté, les requêtes d&#39;envoi de SMS marketing vers ce numéro seront refusées.

    :param keyid: Clé API
    :type keyid: str
    :param setliste_noire: Doit valoir \&quot;1\&quot;
    :type setliste_noire: str
    :param num: numéro de mobile à insérer en liste noire
    :type num: str

    """
    return web.Response(status=200)
