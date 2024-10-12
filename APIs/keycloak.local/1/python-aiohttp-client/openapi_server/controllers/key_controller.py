from typing import List, Dict
from aiohttp import web

from openapi_server.models.keys_metadata_representation import KeysMetadataRepresentation
from openapi_server import util


async def realm_keys_get(request: web.Request, realm) -> web.Response:
    """realm_keys_get

    

    :param realm: realm name (not id!)
    :type realm: str

    """
    return web.Response(status=200)
