from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.offer import Offer
from openapi_server.models.offer_list_response import OfferListResponse
from openapi_server.models.private_store_list import PrivateStoreList
from openapi_server.models.private_store_properties import PrivateStoreProperties
from openapi_server import util


async def private_store_create_or_update(request: web.Request, private_store_id, api_version, payload=None) -> web.Response:
    """private_store_create_or_update

    Changes private store properties

    :param private_store_id: The store ID - must use the tenant ID
    :type private_store_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str
    :param payload: 
    :type payload: dict | bytes

    """
    payload = PrivateStoreProperties.from_dict(payload)
    return web.Response(status=200)


async def private_store_delete(request: web.Request, private_store_id, api_version) -> web.Response:
    """private_store_delete

    Deletes the private store. All that is not saved will be lost.

    :param private_store_id: The store ID - must use the tenant ID
    :type private_store_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def private_store_get(request: web.Request, private_store_id, api_version) -> web.Response:
    """private_store_get

    Get information about the private store

    :param private_store_id: The store ID - must use the tenant ID
    :type private_store_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def private_store_list(request: web.Request, api_version) -> web.Response:
    """private_store_list

    Gets the list of available private stores

    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def private_store_offer_create_or_update(request: web.Request, offer_id, private_store_id, api_version, payload=None) -> web.Response:
    """private_store_offer_create_or_update

    Update or add an offer to the default collection of the private store.

    :param offer_id: The offer ID to update or delete
    :type offer_id: str
    :param private_store_id: The store ID - must use the tenant ID
    :type private_store_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str
    :param payload: 
    :type payload: dict | bytes

    """
    payload = Offer.from_dict(payload)
    return web.Response(status=200)


async def private_store_offer_delete(request: web.Request, offer_id, private_store_id, api_version) -> web.Response:
    """private_store_offer_delete

    Deletes an offer from the given private store.

    :param offer_id: The offer ID to update or delete
    :type offer_id: str
    :param private_store_id: The store ID - must use the tenant ID
    :type private_store_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def private_store_offer_get(request: web.Request, offer_id, private_store_id, api_version) -> web.Response:
    """private_store_offer_get

    Gets information about a specific offer.

    :param offer_id: The offer ID to update or delete
    :type offer_id: str
    :param private_store_id: The store ID - must use the tenant ID
    :type private_store_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def private_store_offers_list(request: web.Request, private_store_id, api_version) -> web.Response:
    """private_store_offers_list

    Get a list of all private offers in the given private store

    :param private_store_id: The store ID - must use the tenant ID
    :type private_store_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)
