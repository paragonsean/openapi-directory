from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_ontol_identifier_resource(request: web.Request, label) -> web.Response:
    """Fetches a map from CURIEs/IDs to labels

    

    :param label: List of labels
    :type label: List[str]

    """
    return web.Response(status=200)


async def post_ontol_identifier_resource(request: web.Request, label) -> web.Response:
    """Fetches a map from CURIEs/IDs to labels

    Takes &#39;label&#39; list argument either as a querystring argument or as a key in the POST body when content-type is application/json.

    :param label: List of labels
    :type label: List[str]

    """
    return web.Response(status=200)
