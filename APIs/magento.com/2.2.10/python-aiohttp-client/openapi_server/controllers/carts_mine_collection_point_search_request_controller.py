from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.temando_shipping_collection_point_cart_collection_point_management_v1_save_search_request_put_request import TemandoShippingCollectionPointCartCollectionPointManagementV1SaveSearchRequestPutRequest
from openapi_server.models.temando_shipping_data_collection_point_search_request_interface import TemandoShippingDataCollectionPointSearchRequestInterface
from openapi_server import util


async def temando_shipping_collection_point_cart_collection_point_management_v1_delete_search_request_delete(request: web.Request, ) -> web.Response:
    """carts/mine/collection-point/search-request

    


    """
    return web.Response(status=200)


async def temando_shipping_collection_point_cart_collection_point_management_v1_save_search_request_put(request: web.Request, body=None) -> web.Response:
    """carts/mine/collection-point/search-request

    

    :param body: 
    :type body: dict | bytes

    """
    body = TemandoShippingCollectionPointCartCollectionPointManagementV1SaveSearchRequestPutRequest.from_dict(body)
    return web.Response(status=200)
