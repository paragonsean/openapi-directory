from typing import List, Dict
from aiohttp import web

from openapi_server.models.catalog_data_product_interface import CatalogDataProductInterface
from openapi_server.models.configurable_product_configurable_product_management_v1_generate_variation_put_request import ConfigurableProductConfigurableProductManagementV1GenerateVariationPutRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def configurable_product_configurable_product_management_v1_generate_variation_put(request: web.Request, body=None) -> web.Response:
    """configurable-products/variation

    Generate variation based on same product

    :param body: 
    :type body: dict | bytes

    """
    body = ConfigurableProductConfigurableProductManagementV1GenerateVariationPutRequest.from_dict(body)
    return web.Response(status=200)
