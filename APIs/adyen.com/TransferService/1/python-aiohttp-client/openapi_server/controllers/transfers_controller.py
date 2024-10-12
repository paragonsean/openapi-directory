from typing import List, Dict
from aiohttp import web

from openapi_server.models.rest_service_error import RestServiceError
from openapi_server.models.service_error import ServiceError
from openapi_server.models.transfer_info_old import TransferInfoOld
from openapi_server.models.transfer_old import TransferOld
from openapi_server import util


async def post_transfers(request: web.Request, www_authenticate=None, body=None) -> web.Response:
    """Transfer funds

    &gt;Versions 1 and 2 of the Transfers API are deprecated. If you are just starting your implementation, use the latest version.  Starts a transfer request to move funds within your balance platform, or send funds to a [transfer instrument](https://docs.adyen.com/api-explorer/#/legalentity/v1/post/transferInstruments). Adyen sends the outcome of the transfer request through webhooks.  To use this endpoint, you need an additional role for your API credential and transfers must be enabled for the source balance account. Your Adyen contact will set these up for you.

    :param www_authenticate: Header for authenticating through SCA
    :type www_authenticate: str
    :param body: 
    :type body: dict | bytes

    """
    body = TransferInfoOld.from_dict(body)
    return web.Response(status=200)
