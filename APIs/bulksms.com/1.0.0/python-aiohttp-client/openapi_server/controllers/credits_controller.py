from typing import List, Dict
from aiohttp import web

from openapi_server.models.transfer_entry import TransferEntry
from openapi_server import util


async def credit_transfer_post(request: web.Request, body) -> web.Response:
    """Transfer credits to another account

    Before you can use the transfer credits endpoint, the _credit-transfer facility_ must be activated for your account.  You can request activation from &#x60;support@bulksms.com&#x60;.   The recipient must be an enabled account that uses the same currency as your account. 

    :param body: Contains details of the transfer request. 
    :type body: dict | bytes

    """
    body = TransferEntry.from_dict(body)
    return web.Response(status=200)
