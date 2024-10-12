from typing import List, Dict
from aiohttp import web

from openapi_server.models.accounts_v1_auth_token_promotion import AccountsV1AuthTokenPromotion
from openapi_server import util


async def update_auth_token_promotion(request: web.Request, ) -> web.Response:
    """update_auth_token_promotion

    Promote the secondary Auth Token to primary. After promoting the new token, all requests to Twilio using your old primary Auth Token will result in an error.


    """
    return web.Response(status=200)
