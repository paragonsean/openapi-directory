from typing import List, Dict
from aiohttp import web

from openapi_server.models.token_request import TokenRequest
from openapi_server.models.token_response import TokenResponse
from openapi_server import util


async def scripts_tokenization_tokens_post(request: web.Request, token_request=None) -> web.Response:
    """Tokenize credit card

    NOTE that the full URL for this API call is https://www.beanstream.com/scripts/tokenization/tokens. Turn a credit card into a token using this service. This helps lessen your PCI scope by not passing the credit card information to your server. Instead you turn the card number into a token in the client app, then send the token to the server. When you send the token to Beanstream to make a payment, Beanstream then looks up the card number from that token and makes the payment. Tokens can also be used to create payment profiles.

    :param token_request: 
    :type token_request: dict | bytes

    """
    token_request = TokenRequest.from_dict(token_request)
    return web.Response(status=200)
