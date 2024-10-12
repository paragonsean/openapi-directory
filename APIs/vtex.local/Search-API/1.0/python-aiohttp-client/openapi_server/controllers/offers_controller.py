from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_catalog_system_pub_products_offers_product_id_get200_response_inner import ApiCatalogSystemPubProductsOffersProductIdGet200ResponseInner
from openapi_server import util


async def api_catalog_system_pub_products_offers_product_id_get(request: web.Request, accept, content_type, product_id) -> web.Response:
    """Search Product offers

    Retrieves existing offers of a specific product.

    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param product_id: Product unique number identifier.
    :type product_id: str

    """
    return web.Response(status=200)


async def api_catalog_system_pub_products_offers_product_id_sku_sku_id_get(request: web.Request, accept, content_type, product_id, sku_id) -> web.Response:
    """Search SKU offers

    Retrieves existing offers of a specific SKU.

    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param product_id: Product unique number identifier.
    :type product_id: str
    :param sku_id: Product unique number identifier.
    :type sku_id: str

    """
    return web.Response(status=200)
