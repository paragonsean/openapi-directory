from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_administered_identities_me200_response import GetAdministeredIdentitiesMe200Response
from openapi_server import util


async def get_administered_identities_me_2(request: web.Request, ) -> web.Response:
    """Returns the identity of the current user.

    Returns the identity of the current user.


    """
    return web.Response(status=200)
