from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.service_inventories_collection import ServiceInventoriesCollection
from openapi_server.models.service_inventory import ServiceInventory
from openapi_server.models.tag import Tag
from openapi_server.models.tags_collection import TagsCollection
from openapi_server import util


async def list_service_inventories(request: web.Request, limit=None, offset=None, filter=None, sort_by=None) -> web.Response:
    """List ServiceInventories

    Returns an array of ServiceInventory objects

    :param limit: The numbers of items to return per page.
    :type limit: int
    :param offset: The number of items to skip before starting to collect the result set.
    :type offset: int
    :param filter: Filter for querying collections.
    :type filter: dict | bytes
    :type filter: Dict[str, ]
    :param sort_by: The list of attribute and order to sort the result set by.
    :type sort_by: dict | bytes
    :type sort_by: Dict[str, ]

    """
    filter = .from_dict(filter)
    sort_by = .from_dict(sort_by)
    return web.Response(status=200)


async def list_service_inventory_tags(request: web.Request, id, limit=None, offset=None, filter=None, sort_by=None) -> web.Response:
    """List Tags for ServiceInventory

    Returns an array of Tag objects

    :param id: ID of the resource
    :type id: str
    :param limit: The numbers of items to return per page.
    :type limit: int
    :param offset: The number of items to skip before starting to collect the result set.
    :type offset: int
    :param filter: Filter for querying collections.
    :type filter: dict | bytes
    :type filter: Dict[str, ]
    :param sort_by: The list of attribute and order to sort the result set by.
    :type sort_by: dict | bytes
    :type sort_by: Dict[str, ]

    """
    filter = .from_dict(filter)
    sort_by = .from_dict(sort_by)
    return web.Response(status=200)


async def show_service_inventory(request: web.Request, id) -> web.Response:
    """Show an existing ServiceInventory

    Returns a ServiceInventory object

    :param id: ID of the resource
    :type id: str

    """
    return web.Response(status=200)


async def tag_service_inventory(request: web.Request, id, body) -> web.Response:
    """Tag a ServiceInventory

    Tags a ServiceInventory object

    :param id: ID of the resource
    :type id: str
    :param body: Tag attributes to add
    :type body: list | bytes

    """
    body = [Tag.from_dict(d) for d in body]
    return web.Response(status=200)


async def untag_service_inventory(request: web.Request, id, body) -> web.Response:
    """Untag a ServiceInventory

    Untags a ServiceInventory object

    :param id: ID of the resource
    :type id: str
    :param body: Tag attributes to removed
    :type body: list | bytes

    """
    body = [Tag.from_dict(d) for d in body]
    return web.Response(status=200)
