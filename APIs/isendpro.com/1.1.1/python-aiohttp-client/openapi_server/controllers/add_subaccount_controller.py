from typing import List, Dict
from aiohttp import web

from openapi_server.models.erreur import Erreur
from openapi_server.models.subaccount_add_request import SubaccountAddRequest
from openapi_server.models.subaccount_add_response import SubaccountAddResponse
from openapi_server import util


async def subaccount_add(request: web.Request, body) -> web.Response:
    """Ajoute un sous compte

    Ajoute un sous compte

    :param body: add sub account request
    :type body: dict | bytes

    """
    body = SubaccountAddRequest.from_dict(body)
    return web.Response(status=200)
