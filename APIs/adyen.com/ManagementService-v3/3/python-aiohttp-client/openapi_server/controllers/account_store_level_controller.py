from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_stores_response import ListStoresResponse
from openapi_server.models.rest_service_error import RestServiceError
from openapi_server.models.store import Store
from openapi_server.models.store_creation_request import StoreCreationRequest
from openapi_server.models.store_creation_with_merchant_code_request import StoreCreationWithMerchantCodeRequest
from openapi_server.models.update_store_request import UpdateStoreRequest
from openapi_server import util


async def get_merchants_merchant_id_stores(request: web.Request, merchant_id, page_number=None, page_size=None, reference=None) -> web.Response:
    """Get a list of stores

    Returns a list of stores for the merchant account identified in the path. The list is grouped into pages as defined by the query parameters.  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Stores read * Management API—Stores read and write

    :param merchant_id: The unique identifier of the merchant account.
    :type merchant_id: str
    :param page_number: The number of the page to fetch.
    :type page_number: int
    :param page_size: The number of items to have on a page, maximum 100. The default is 10 items on a page.
    :type page_size: int
    :param reference: The reference of the store.
    :type reference: str

    """
    return web.Response(status=200)


async def get_merchants_merchant_id_stores_store_id(request: web.Request, merchant_id, store_id) -> web.Response:
    """Get a store

    Returns the details of the store identified in the path.  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Stores read * Management API—Stores read and write

    :param merchant_id: The unique identifier of the merchant account.
    :type merchant_id: str
    :param store_id: The unique identifier of the store.
    :type store_id: str

    """
    return web.Response(status=200)


async def get_stores(request: web.Request, page_number=None, page_size=None, reference=None, merchant_id=None) -> web.Response:
    """Get a list of stores

    Returns a list of stores. The list is grouped into pages as defined by the query parameters.  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Stores read * Management API—Stores read and write

    :param page_number: The number of the page to fetch.
    :type page_number: int
    :param page_size: The number of items to have on a page, maximum 100. The default is 10 items on a page.
    :type page_size: int
    :param reference: The reference of the store.
    :type reference: str
    :param merchant_id: The unique identifier of the merchant account.
    :type merchant_id: str

    """
    return web.Response(status=200)


async def get_stores_store_id(request: web.Request, store_id) -> web.Response:
    """Get a store

    Returns the details of the store identified in the path.  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Stores read * Management API—Stores read and write

    :param store_id: The unique identifier of the store.
    :type store_id: str

    """
    return web.Response(status=200)


async def patch_merchants_merchant_id_stores_store_id(request: web.Request, merchant_id, store_id, body=None) -> web.Response:
    """Update a store

    Updates the store identified in the path. You can only update some store parameters.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Stores read and write

    :param merchant_id: The unique identifier of the merchant account.
    :type merchant_id: str
    :param store_id: The unique identifier of the store.
    :type store_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateStoreRequest.from_dict(body)
    return web.Response(status=200)


async def patch_stores_store_id(request: web.Request, store_id, body=None) -> web.Response:
    """Update a store

    Updates the store identified in the path. You can only update some store parameters.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Stores read and write

    :param store_id: The unique identifier of the store.
    :type store_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateStoreRequest.from_dict(body)
    return web.Response(status=200)


async def post_merchants_merchant_id_stores(request: web.Request, merchant_id, body=None) -> web.Response:
    """Create a store

    Creates a store for the merchant account identified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Stores read and write

    :param merchant_id: The unique identifier of the merchant account.
    :type merchant_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = StoreCreationRequest.from_dict(body)
    return web.Response(status=200)


async def post_stores(request: web.Request, body=None) -> web.Response:
    """Create a store

    Creates a store for the merchant account specified in the request.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Stores read and write

    :param body: 
    :type body: dict | bytes

    """
    body = StoreCreationWithMerchantCodeRequest.from_dict(body)
    return web.Response(status=200)
