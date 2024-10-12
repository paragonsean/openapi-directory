from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.full_item import FullItem
from openapi_server.models.item import Item
from openapi_server.models.patch_inner import PatchInner
from openapi_server import util


async def create_vault_item(request: web.Request, vault_uuid, body=None) -> web.Response:
    """Create a new Item

    

    :param vault_uuid: The UUID of the Vault to create an Item in
    :type vault_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = FullItem.from_dict(body)
    return web.Response(status=200)


async def delete_vault_item(request: web.Request, vault_uuid, item_uuid) -> web.Response:
    """Delete an Item

    

    :param vault_uuid: The UUID of the Vault the item is in
    :type vault_uuid: str
    :param item_uuid: The UUID of the Item to update
    :type item_uuid: str

    """
    return web.Response(status=200)


async def get_vault_item_by_id(request: web.Request, vault_uuid, item_uuid) -> web.Response:
    """Get the details of an Item

    

    :param vault_uuid: The UUID of the Vault to fetch Item from
    :type vault_uuid: str
    :param item_uuid: The UUID of the Item to fetch
    :type item_uuid: str

    """
    return web.Response(status=200)


async def get_vault_items(request: web.Request, vault_uuid, filter=None) -> web.Response:
    """Get all items for inside a Vault

    

    :param vault_uuid: The UUID of the Vault to fetch Items from
    :type vault_uuid: str
    :param filter: Filter the Item collection based on Item name using SCIM eq filter
    :type filter: str

    """
    return web.Response(status=200)


async def patch_vault_item(request: web.Request, vault_uuid, item_uuid, body=None) -> web.Response:
    """Update a subset of Item attributes

    Applies a modified [RFC6902 JSON Patch](https://tools.ietf.org/html/rfc6902) document to an Item or ItemField. This endpoint only supports &#x60;add&#x60;, &#x60;remove&#x60; and &#x60;replace&#x60; operations.  When modifying a specific ItemField, the ItemField&#39;s ID in the &#x60;path&#x60; attribute of the operation object: &#x60;/fields/{fieldId}&#x60; 

    :param vault_uuid: The UUID of the Vault the item is in
    :type vault_uuid: str
    :param item_uuid: The UUID of the Item to update
    :type item_uuid: str
    :param body: 
    :type body: list | bytes

    """
    body = [PatchInner.from_dict(d) for d in body]
    return web.Response(status=200)


async def update_vault_item(request: web.Request, vault_uuid, item_uuid, body=None) -> web.Response:
    """Update an Item

    

    :param vault_uuid: The UUID of the Item&#39;s Vault
    :type vault_uuid: str
    :param item_uuid: The UUID of the Item to update
    :type item_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = FullItem.from_dict(body)
    return web.Response(status=200)
