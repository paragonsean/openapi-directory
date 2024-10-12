from typing import List, Dict
from aiohttp import web

from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.copy_optimisation_request import CopyOptimisationRequest
from openapi_server.models.copy_optimisation_response import CopyOptimisationResponse
from openapi_server.models.optimise_all_request import OptimiseAllRequest
from openapi_server.models.optimise_request import OptimiseRequest
from openapi_server import util


async def copy_optimisation(request: web.Request, store_id, body) -> web.Response:
    """Copy product optimisations between 2 channels

    

    :param store_id: Your store identifier
    :type store_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CopyOptimisationRequest.from_dict(body)
    return web.Response(status=200)


async def optimise(request: web.Request, store_id, action_name, body) -> web.Response:
    """Optimise products by page

    /!\\ WARNING /!\\ \\ Apply the operation on every product related to this request. \\ This operation is used at the bottom of the analytics page result. 

    :param store_id: Your store identifier
    :type store_id: str
    :param action_name: 
    :type action_name: str
    :param body: 
    :type body: dict | bytes

    """
    body = OptimiseRequest.from_dict(body)
    return web.Response(status=200)


async def optimise_all(request: web.Request, store_id, action_name, body) -> web.Response:
    """Optimise all products

    /!\\ WARNING /!\\ \\ Apply the operation on every product related to this request. \\ This operation is used at the bottom of the analytics page result. 

    :param store_id: Your store identifier
    :type store_id: str
    :param action_name: 
    :type action_name: str
    :param body: 
    :type body: dict | bytes

    """
    body = OptimiseAllRequest.from_dict(body)
    return web.Response(status=200)


async def optimise_by_category(request: web.Request, store_id, catalog_category_id, action_name, body=None) -> web.Response:
    """Optimise products by category

    /!\\ WARNING /!\\ \\ This operation will reenable or disable products&#39;s category for every channel indicated in the body. 

    :param store_id: Your store identifier
    :type store_id: str
    :param catalog_category_id: The category identifier concerned by this optimisation
    :type catalog_category_id: str
    :param action_name: 
    :type action_name: str
    :param body: The channel identifier list concerned by this optimisation
    :type body: List[str]

    """
    return web.Response(status=200)


async def optimise_by_channel(request: web.Request, store_id, channel_id, action_name) -> web.Response:
    """Optimise products by channel

    /!\\ WARNING /!\\ \\ Apply the operation on every product on this channel. 

    :param store_id: Your store identifier
    :type store_id: str
    :param channel_id: The channel identifier concerned by this optimisation
    :type channel_id: str
    :param action_name: 
    :type action_name: str

    """
    return web.Response(status=200)


async def optimise_by_product(request: web.Request, store_id, product_id, action_name, body=None) -> web.Response:
    """Optimise product

    /!\\ WARNING /!\\ \\ This operation will reenable or disable this product for every channel indicated in the body. 

    :param store_id: Your store identifier
    :type store_id: str
    :param product_id: The product identifier concerned by this optimisation
    :type product_id: str
    :param action_name: 
    :type action_name: str
    :param body: The channel identifier list concerned by this optimisation
    :type body: List[str]

    """
    return web.Response(status=200)
