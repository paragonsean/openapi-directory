from typing import List, Dict
from aiohttp import web

from openapi_server.models.blacklist_item_response_version import BlacklistItemResponseVersion
from openapi_server import util


async def add_blacklist(request: web.Request, content_type, blacklisted_items, config_id=None) -> web.Response:
    """Add items to blacklist

    This method adds new unique items to the backlist on Semantria side.

    :param content_type: 
    :type content_type: str
    :param blacklisted_items: List of parametrized JSON or XML objects.
    :type blacklisted_items: 
    :param config_id: Identifier of configuration blacklist linked to.
    :type config_id: str

    """
    return web.Response(status=200)


async def delete_blacklist_items(request: web.Request, content_type, blacklisted_item_ids, config_id=None) -> web.Response:
    """Remove items from blacklist

    This method removes certain blacklisted items by their values on Semantria side.

    :param content_type: 
    :type content_type: str
    :param blacklisted_item_ids: List of unique blacklisted item identifiers (string).
    :type blacklisted_item_ids: List[str]
    :param config_id: Identifier of configuration blacklist items linked to.
    :type config_id: str

    """
    return web.Response(status=200)


async def get_blacklist(request: web.Request, content_type, config_id=None) -> web.Response:
    """Retrieve blacklisted items

    This method retrieves all backlisted items available on Semantria side.

    :param content_type: 
    :type content_type: str
    :param config_id: Identifier of configuration blacklist linked to.
    :type config_id: str

    """
    return web.Response(status=200)


async def update_blacklist(request: web.Request, content_type, blacklisted_items, config_id=None) -> web.Response:
    """Update items in blacklist

    This method updates existing items by unique IDs in the backlist on Semantria side.

    :param content_type: 
    :type content_type: str
    :param blacklisted_items: List of parametrized JSON or XML objects.
    :type blacklisted_items: 
    :param config_id: Identifier of configuration blacklist linked to.
    :type config_id: str

    """
    return web.Response(status=200)
