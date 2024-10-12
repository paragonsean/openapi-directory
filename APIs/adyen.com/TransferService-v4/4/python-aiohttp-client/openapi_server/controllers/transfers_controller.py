from typing import List, Dict
from aiohttp import web

from openapi_server.models.rest_service_error import RestServiceError
from openapi_server.models.return_transfer_request import ReturnTransferRequest
from openapi_server.models.return_transfer_response import ReturnTransferResponse
from openapi_server.models.service_error import ServiceError
from openapi_server.models.transfer import Transfer
from openapi_server.models.transfer_info import TransferInfo
from openapi_server import util


async def post_transfers(request: web.Request, www_authenticate=None, body=None) -> web.Response:
    """Transfer funds

    &gt;Versions 1 and 2 of the Transfers API are deprecated. If you are just starting your implementation, use the latest version.  Starts a request to transfer funds to [balance accounts](https://docs.adyen.com/api-explorer/#/balanceplatform/latest/post/balanceAccounts), [transfer instruments](https://docs.adyen.com/api-explorer/#/legalentity/latest/post/transferInstruments), or third-party bank accounts. Adyen sends the outcome of the transfer request through webhooks.  To use this endpoint, you need an additional role for your API credential and transfers must be enabled for the source balance account. Your Adyen contact will set these up for you.

    :param www_authenticate: Header for authenticating through SCA
    :type www_authenticate: str
    :param body: 
    :type body: dict | bytes

    """
    body = TransferInfo.from_dict(body)
    return web.Response(status=200)


async def post_transfers_transfer_id_returns(request: web.Request, transfer_id, body=None) -> web.Response:
    """Return a transfer

    Returns previously transferred funds without creating a new &#x60;transferId&#x60;.

    :param transfer_id: The unique identifier of the transfer to be returned.
    :type transfer_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ReturnTransferRequest.from_dict(body)
    return web.Response(status=200)
