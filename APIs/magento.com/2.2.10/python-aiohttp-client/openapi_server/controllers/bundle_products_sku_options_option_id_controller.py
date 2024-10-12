from typing import List, Dict
from aiohttp import web

from openapi_server.models.bundle_data_option_interface import BundleDataOptionInterface
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def bundle_product_option_repository_v1_delete_by_id_delete(request: web.Request, sku, option_id) -> web.Response:
    """bundle-products/{sku}/options/{optionId}

    Remove bundle option

    :param sku: 
    :type sku: str
    :param option_id: 
    :type option_id: int

    """
    return web.Response(status=200)


async def bundle_product_option_repository_v1_get_get(request: web.Request, sku, option_id) -> web.Response:
    """bundle-products/{sku}/options/{optionId}

    Get option for bundle product

    :param sku: 
    :type sku: str
    :param option_id: 
    :type option_id: int

    """
    return web.Response(status=200)
