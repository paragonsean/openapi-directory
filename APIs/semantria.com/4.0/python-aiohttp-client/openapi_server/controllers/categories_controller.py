from typing import List, Dict
from aiohttp import web

from openapi_server.models.category_response_version import CategoryResponseVersion
from openapi_server import util


async def add_categories(request: web.Request, content_type, categories, config_id=None) -> web.Response:
    """Add user categories

    This method adds user categories on Semantria side.

    :param content_type: 
    :type content_type: str
    :param categories: List of parametrized JSON or XML objects.
    :type categories: 
    :param config_id: Identifier of configuration user categories linked to.
    :type config_id: str

    """
    return web.Response(status=200)


async def delete_categories(request: web.Request, content_type, category_ids, config_id=None) -> web.Response:
    """Remove user categories

    This method removes certain user categories by their IDs on Semantria side.

    :param content_type: 
    :type content_type: str
    :param category_ids: List of user category identifiers.
    :type category_ids: List[str]
    :param config_id: Identifier of configuration user categories linked to.
    :type config_id: str

    """
    return web.Response(status=200)


async def get_categories(request: web.Request, content_type, config_id=None) -> web.Response:
    """Retrieve user categories

    This method retrieves list of user categories available on Semantria side.

    :param content_type: 
    :type content_type: str
    :param config_id: Identifier of configuration user categories linked to.
    :type config_id: str

    """
    return web.Response(status=200)


async def update_categories(request: web.Request, content_type, categories, config_id=None) -> web.Response:
    """Updates user categories

    This method updates user categories by unique IDs on Semantria side.

    :param content_type: 
    :type content_type: str
    :param categories: List of parametrized JSON or XML objects.
    :type categories: 
    :param config_id: Identifier of configuration user categories linked to.
    :type config_id: str

    """
    return web.Response(status=200)
