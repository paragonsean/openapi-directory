from typing import List, Dict
from aiohttp import web

from openapi_server.models.credit_response import CreditResponse
from openapi_server.models.erreur import Erreur
from openapi_server import util


async def get_credit(request: web.Request, keyid, credit) -> web.Response:
    """Interrogation credit

    Retourne le credit existant associe au compte. 

    :param keyid: Clé API
    :type keyid: str
    :param credit: Type de reponse demandée, 1 pour euro, 2 pour euro + estimation quantité
    :type credit: str

    """
    return web.Response(status=200)
