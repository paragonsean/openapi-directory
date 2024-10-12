from typing import List, Dict
from aiohttp import web

from openapi_server.models.erreur import Erreur
from openapi_server.models.hlr_reponse import HLRReponse
from openapi_server.models.hl_rrequest import HLRrequest
from openapi_server import util


async def get_hlr(request: web.Request, body) -> web.Response:
    """Vérifier la validité d&#39;un numéro

    Réalise un lookup HLR sur les numéros  

    :param body: 
    :type body: dict | bytes

    """
    body = HLRrequest.from_dict(body)
    return web.Response(status=200)
