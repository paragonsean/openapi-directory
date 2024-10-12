from typing import List, Dict
from aiohttp import web

from openapi_server.models.composite_token import CompositeToken
from openapi_server.models.digital_wallet_validation import DigitalWalletValidation
from openapi_server.models.error import Error
from openapi_server.models.invalid_error import InvalidError
from openapi_server import util


async def get_token(request: web.Request, token, organization_id=None) -> web.Response:
    """Retrieve a token

    Retrieve a token with specified identifier string. 

    :param token: The token identifier string.
    :type token: str
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_token_collection(request: web.Request, organization_id=None, limit=None, offset=None) -> web.Response:
    """Retrieve a list of tokens

    Retrieve a list of tokens. 

    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str
    :param limit: The collection items limit.
    :type limit: int
    :param offset: The collection items offset.
    :type offset: int

    """
    return web.Response(status=200)


async def post_digital_wallet_validation(request: web.Request, body) -> web.Response:
    """Validate a digital wallet session

    [FramePay](https://docs.rebilly.com/docs/developer-docs/framepay/) is the recommended way to use when validating a digital wallet session. 

    :param body: Digital wallet validation request.
    :type body: dict | bytes

    """
    body = DigitalWalletValidation.from_dict(body)
    return web.Response(status=200)


async def post_token(request: web.Request, body, organization_id=None) -> web.Response:
    """Create a payment token

    [FramePay](https://docs.rebilly.com/docs/developer-docs/framepay/) is the recommended way to create a payment token because it minimizes PCI DSS compliance.  Once a payment token is created, it can only be used once.  A payment token expires upon first use or within 30 minutes of the token creation (whichever comes first). 

    :param body: PaymentToken resource.
    :type body: dict | bytes
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    body = CompositeToken.from_dict(body)
    return web.Response(status=200)
