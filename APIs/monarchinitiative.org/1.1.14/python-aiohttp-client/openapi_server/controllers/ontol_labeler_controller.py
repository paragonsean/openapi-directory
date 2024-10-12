from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_ontol_labeler_resource(request: web.Request, id) -> web.Response:
    """Fetches a map from CURIEs/IDs to labels

    

    :param id: List of ids
    :type id: List[str]

    """
    return web.Response(status=200)
