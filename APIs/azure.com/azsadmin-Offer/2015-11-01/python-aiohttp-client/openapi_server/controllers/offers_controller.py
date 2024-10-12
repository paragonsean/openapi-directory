from typing import List, Dict
from aiohttp import web

from openapi_server.models.offer_list import OfferList
from openapi_server import util


async def offers_list(request: web.Request, api_version) -> web.Response:
    """offers_list

    Get the list of public offers for the root provider.

    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)
