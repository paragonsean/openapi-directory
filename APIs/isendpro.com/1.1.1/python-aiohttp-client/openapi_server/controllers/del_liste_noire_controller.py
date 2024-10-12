from typing import List, Dict
from aiohttp import web

from openapi_server.models.erreur import Erreur
from openapi_server.models.listenoire_reponse import LISTENOIREReponse
from openapi_server import util


async def del_liste_noire(request: web.Request, keyid, del_liste_noire, num) -> web.Response:
    """Ajoute un numero en liste noire

    Supprime un numero en liste noire

    :param keyid: Clé API
    :type keyid: str
    :param del_liste_noire: Doit valoir \&quot;1\&quot;
    :type del_liste_noire: str
    :param num: numéro de mobile à supprimer
    :type num: str

    """
    return web.Response(status=200)
