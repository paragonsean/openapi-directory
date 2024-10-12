from typing import List, Dict
from aiohttp import web

from openapi_server.models.comptage_reponse import ComptageReponse
from openapi_server.models.comptage_request import ComptageRequest
from openapi_server.models.erreur import Erreur
from openapi_server import util


async def comptage(request: web.Request, body) -> web.Response:
    """Compter le nombre de caractère 

    Compte le nombre de SMS necessaire à un envoi

    :param body: sms request
    :type body: dict | bytes

    """
    body = ComptageRequest.from_dict(body)
    return web.Response(status=200)
