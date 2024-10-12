from typing import List, Dict
from aiohttp import web

from openapi_server.models.erreur import Erreur
from openapi_server import util


async def get_liste_noire(request: web.Request, keyid, get_liste_noire) -> web.Response:
    """Retourne le liste noire

    Retourne un fichier csv zippé contenant la liste noire

    :param keyid: Clé API
    :type keyid: str
    :param get_liste_noire: Doit valoir \&quot;1\&quot;
    :type get_liste_noire: str

    """
    return web.Response(status=200)
