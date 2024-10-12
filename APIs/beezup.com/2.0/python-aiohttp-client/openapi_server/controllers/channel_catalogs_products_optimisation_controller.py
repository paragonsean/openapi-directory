from typing import List, Dict
from aiohttp import web

from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server import util


async def disable_channel_catalog_product(request: web.Request, channel_catalog_id, product_id) -> web.Response:
    """Disable channel catalog product

    By default a all your catalog products are exposed to the channel. You can disable a product by using this operation. /!\\ In case of massive optimisation we recommand you to use the analytics api 

    :param channel_catalog_id: The channel catalog identifier
    :type channel_catalog_id: str
    :param product_id: The product identifier
    :type product_id: str

    """
    return web.Response(status=200)


async def reenable_channel_catalog_product(request: web.Request, channel_catalog_id, product_id) -> web.Response:
    """Reenable channel catalog product

    By default a all your catalog products are exposed to the channel. You can reenable a product by using this operation. /!\\ In case of massive optimisation we recommand you to use the analytics api 

    :param channel_catalog_id: The channel catalog identifier
    :type channel_catalog_id: str
    :param product_id: The product identifier
    :type product_id: str

    """
    return web.Response(status=200)
