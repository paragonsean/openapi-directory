from typing import List, Dict
from aiohttp import web

from openapi_server.models.clear_address import ClearAddress
from openapi_server.models.clear_address_request import ClearAddressRequest
from openapi_server.models.send_ethereum import SendEthereum
from openapi_server.models.send_ethereum_request import SendEthereumRequest
from openapi_server.models.send_token import SendToken
from openapi_server.models.send_token_request import SendTokenRequest
from openapi_server import util


async def clear_address(request: web.Request, authorization, body) -> web.Response:
    """clearAddress

    Sends all available ethereum funds of an address to a specified receiver address.

    :param authorization: API Key
    :type authorization: str
    :param body: 
    :type body: dict | bytes

    """
    body = ClearAddressRequest.from_dict(body)
    return web.Response(status=200)


async def send_ethereum(request: web.Request, authorization, body) -> web.Response:
    """sendEthereum

    Sends ethereum from an address controlled by the account to a specified receiver address.

    :param authorization: API Key
    :type authorization: str
    :param body: 
    :type body: dict | bytes

    """
    body = SendEthereumRequest.from_dict(body)
    return web.Response(status=200)


async def send_token(request: web.Request, authorization, body) -> web.Response:
    """sendToken

    Sends ERC20 tokens from an address controlled by the account to a specified receiver address. The token contract address is needed to specify the token. The use of the identifier parameter is recommend and awaits an unique string. Whenever a transaction is beeing sent, the identifier is checked and the transaction gets dropped if there is one with that identifier already.

    :param authorization: API Key
    :type authorization: str
    :param body: 
    :type body: dict | bytes

    """
    body = SendTokenRequest.from_dict(body)
    return web.Response(status=200)
