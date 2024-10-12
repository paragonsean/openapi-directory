from typing import List, Dict
from aiohttp import web

from openapi_server.models.gallery_item import GalleryItem
from openapi_server.models.gallery_item_list import GalleryItemList
from openapi_server.models.gallery_item_uri_payload import GalleryItemUriPayload
from openapi_server import util


async def gallery_items_create(request: web.Request, subscription_id, api_version, gallery_item_uri_payload) -> web.Response:
    """Uploads a provider gallery item to the storage.

    

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param gallery_item_uri_payload: The URI to the gallery item JSON file.
    :type gallery_item_uri_payload: dict | bytes

    """
    gallery_item_uri_payload = GalleryItemUriPayload.from_dict(gallery_item_uri_payload)
    return web.Response(status=200)


async def gallery_items_delete(request: web.Request, subscription_id, gallery_item_name, api_version) -> web.Response:
    """Delete a specific gallery item.

    

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param gallery_item_name: Identity of the gallery item. Includes publisher name, item name, and may include version separated by period character.
    :type gallery_item_name: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def gallery_items_get(request: web.Request, subscription_id, gallery_item_name, api_version) -> web.Response:
    """Get a specific gallery item.

    

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param gallery_item_name: Identity of the gallery item. Includes publisher name, item name, and may include version separated by period character.
    :type gallery_item_name: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def gallery_items_list(request: web.Request, subscription_id, api_version) -> web.Response:
    """Lists gallery items.

    

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)
