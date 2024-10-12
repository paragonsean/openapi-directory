from typing import List, Dict
from aiohttp import web

from openapi_server.models.configurable_product_data_option_interface import ConfigurableProductDataOptionInterface
from openapi_server.models.configurable_product_option_repository_v1_save_post_request import ConfigurableProductOptionRepositoryV1SavePostRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def configurable_product_option_repository_v1_delete_by_id_delete(request: web.Request, sku, id) -> web.Response:
    """configurable-products/{sku}/options/{id}

    Remove option from configurable product

    :param sku: 
    :type sku: str
    :param id: 
    :type id: int

    """
    return web.Response(status=200)


async def configurable_product_option_repository_v1_get_get(request: web.Request, sku, id) -> web.Response:
    """configurable-products/{sku}/options/{id}

    Get option for configurable product

    :param sku: 
    :type sku: str
    :param id: 
    :type id: int

    """
    return web.Response(status=200)


async def configurable_product_option_repository_v1_save_put(request: web.Request, sku, id, body=None) -> web.Response:
    """configurable-products/{sku}/options/{id}

    Save option

    :param sku: 
    :type sku: str
    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ConfigurableProductOptionRepositoryV1SavePostRequest.from_dict(body)
    return web.Response(status=200)
