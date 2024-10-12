from typing import List, Dict
from aiohttp import web

from openapi_server.models.delete_account202_response import DeleteAccount202Response
from openapi_server.models.get_validity200_response import GetValidity200Response
from openapi_server import util


async def get_validity(request: web.Request, ) -> web.Response:
    """Validate API key

    Endpoint used to test the validity and some basic information about a specific API Key.


    """
    return web.Response(status=200)
