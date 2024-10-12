from typing import List, Dict
from aiohttp import web

from openapi_server.models.erreur import Erreur
from openapi_server.models.repertoir_ecreatereponse import REPERTOIREcreatereponse
from openapi_server.models.repertoir_ecreaterequest import REPERTOIREcreaterequest
from openapi_server.models.repertoir_emodifreponse import REPERTOIREmodifreponse
from openapi_server.models.repertoir_emodifrequest import REPERTOIREmodifrequest
from openapi_server import util


async def repertoire(request: web.Request, body) -> web.Response:
    """Gestion repertoire (modification)

    Ajoute ou supprime une liste de numéros à un répertoire existant.

    :param body: Requête de creation repertoire
    :type body: dict | bytes

    """
    body = REPERTOIREmodifrequest.from_dict(body)
    return web.Response(status=200)


async def repertoire_crea(request: web.Request, body) -> web.Response:
    """Gestion repertoire (creation)

    Cree un nouveau répertoire et retourne son identifiant. Cet identifiant pourra être utilisé pour ajouter ou supprimer des numéros via l&#39;API.

    :param body: Creation repertoire
    :type body: dict | bytes

    """
    body = REPERTOIREcreaterequest.from_dict(body)
    return web.Response(status=200)
