from typing import List, Dict
from aiohttp import web

from openapi_server.models.erreur import Erreur
from openapi_server.models.subaccount_request import SubaccountRequest
from openapi_server.models.subaccount_response import SubaccountResponse
from openapi_server import util


async def subaccount_edit(request: web.Request, body) -> web.Response:
    """Edit a subaccount

    Edit a subaccount

    :param body: edit sub account request
    :type body: dict | bytes

    """
    body = SubaccountRequest.from_dict(body)
    return web.Response(status=200)
