from typing import List, Dict
from aiohttp import web

from openapi_server.models.deed_application import DeedApplication
from openapi_server.models.error import Error
from openapi_server import util


async def add_deed(request: web.Request, body) -> web.Response:
    """Deed

    The post Deed endpoint creates a new deed based on the JSON provided.  The reponse will return a URL that can retrieve the created deed.   &gt; REQUIRED: Land Registry system requests Conveyancer to confirm that the Borrowers identity has been established in accordance with Section 111 of the Network Access Agreement.

    :param body: 
    :type body: dict | bytes

    """
    body = DeedApplication.from_dict(body)
    return web.Response(status=200)
