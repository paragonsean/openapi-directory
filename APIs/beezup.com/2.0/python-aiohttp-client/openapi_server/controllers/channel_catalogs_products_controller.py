from typing import List, Dict
from aiohttp import web

from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.beez_up_common_link3 import BeezUPCommonLink3
from openapi_server.models.channel_catalog_product_by_channel_catalog_request import ChannelCatalogProductByChannelCatalogRequest
from openapi_server.models.channel_catalog_product_by_channel_catalog_response import ChannelCatalogProductByChannelCatalogResponse
from openapi_server.models.channel_catalog_product_info import ChannelCatalogProductInfo
from openapi_server.models.channel_catalog_product_info_list import ChannelCatalogProductInfoList
from openapi_server.models.channel_catalog_products_counters import ChannelCatalogProductsCounters
from openapi_server.models.get_channel_catalog_product_info_list_request import GetChannelCatalogProductInfoListRequest
from openapi_server import util


async def export_channel_catalog_product_info_list(request: web.Request, channel_catalog_id, format, body) -> web.Response:
    """Export channel catalog product information list

    

    :param channel_catalog_id: The channel catalog identifier
    :type channel_catalog_id: str
    :param format: The file type of the exportation
    :type format: str
    :param body: The channel catalog product list filter
    :type body: dict | bytes

    """
    body = GetChannelCatalogProductInfoListRequest.from_dict(body)
    return web.Response(status=200)


async def get_channel_catalog_product_by_channel_catalog(request: web.Request, body) -> web.Response:
    """Get channel catalog products related to these channel catalogs

    

    :param body: 
    :type body: dict | bytes

    """
    body = ChannelCatalogProductByChannelCatalogRequest.from_dict(body)
    return web.Response(status=200)


async def get_channel_catalog_product_info(request: web.Request, channel_catalog_id, product_id) -> web.Response:
    """Get channel catalog product information

    

    :param channel_catalog_id: The channel catalog identifier
    :type channel_catalog_id: str
    :param product_id: The product identifier
    :type product_id: str

    """
    return web.Response(status=200)


async def get_channel_catalog_product_info_list(request: web.Request, channel_catalog_id, body) -> web.Response:
    """Get channel catalog product information list

    

    :param channel_catalog_id: The channel catalog identifier
    :type channel_catalog_id: str
    :param body: The channel catalog product list filter
    :type body: dict | bytes

    """
    body = GetChannelCatalogProductInfoListRequest.from_dict(body)
    return web.Response(status=200)


async def get_channel_catalog_products_counters(request: web.Request, channel_catalog_id) -> web.Response:
    """Get channel catalog products&#39; counters

    

    :param channel_catalog_id: The channel catalog identifier
    :type channel_catalog_id: str

    """
    return web.Response(status=200)
