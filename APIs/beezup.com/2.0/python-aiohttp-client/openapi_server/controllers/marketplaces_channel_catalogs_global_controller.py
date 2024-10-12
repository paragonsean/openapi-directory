from typing import List, Dict
from aiohttp import web

from openapi_server.models.marketplace_channel_catalog_list import MarketplaceChannelCatalogList
from openapi_server import util


async def get_marketplace_channel_catalogs(request: web.Request, store_id=None) -> web.Response:
    """Get your marketplace channel catalog list

    

    :param store_id: The StoreId to filter by
    :type store_id: str

    """
    return web.Response(status=200)
