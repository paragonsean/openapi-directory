from typing import List, Dict
from aiohttp import web

from openapi_server.models.category_jo import CategoryJO
from openapi_server.models.error_jo import ErrorJO
from openapi_server import util


async def get_category(request: web.Request, providernetwork_uid, category_uid, expand=None) -> web.Response:
    """Get a Category by UID

    Search for categorie.

    :param providernetwork_uid: Provider Network UID
    :type providernetwork_uid: str
    :param category_uid: 
    :type category_uid: str
    :param expand: 
    :type expand: str

    """
    return web.Response(status=200)


async def list_categories(request: web.Request, providernetwork_uid, expand=None) -> web.Response:
    """Lists all categories

    Search for categorie.

    :param providernetwork_uid: 
    :type providernetwork_uid: str
    :param expand: 
    :type expand: str

    """
    return web.Response(status=200)
