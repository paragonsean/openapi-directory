from typing import List, Dict
from aiohttp import web

from openapi_server.models.facet import Facet
from openapi_server import util


async def get_endpoint_summary_0(request: web.Request, db, top=None, category=None) -> web.Response:
    """Search endpoint summary

    Returns endpoint summary

    :param db: Database ID
    :type db: str
    :param top: Top endpoint category
    :type top: str
    :param category: Endpoint category (The value in the protocol.category.code field)
    :type category: str

    """
    return web.Response(status=200)
