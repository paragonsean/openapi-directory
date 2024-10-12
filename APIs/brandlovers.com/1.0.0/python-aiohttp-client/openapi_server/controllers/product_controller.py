from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_product import GetProduct
from openapi_server.models.product import Product
from openapi_server.models.product_price import ProductPrice
from openapi_server.models.seller_item_status import SellerItemStatus
from openapi_server.models.stock import Stock
from openapi_server import util


async def product_post(request: web.Request, authorization, product) -> web.Response:
    """Create a new product to the marketplace

    Use this enpoint to create a single new product to the Marketplace. This enpoint expects a json document with one product. If you whant to upload multiple products in a single API call use POST /products method. The server will load each product as an individual item that can be manipulated using your own &#x60;skuSellerId&#x60;. This system is idenpontent, this means that once a &#x60;skuSellerId&#x60; is created it cannot be re-created using this tool. In order to update, edit a product use the PUT method with the correct reference to your &#x60;skuSellerId&#x60;

    :param authorization: Authorization token. The Authorization token can be found in your Admin console.
    :type authorization: str
    :param product: New Produt that will be create
    :type product: dict | bytes

    """
    product = Product.from_dict(product)
    return web.Response(status=200)


async def product_sku_seller_id_get(request: web.Request, authorization, sku_seller_id) -> web.Response:
    """Returns details of a single product using the seller &#x60;skuSellerId&#x60;

    Returns detailed information of a single product with the seller &#x60;skuSellerId&#x60;. This service will return a json document with product detail, status, price, invetory among other infomarion availble in the Brand Lovers marketplace

    :param authorization: Authorization token. The Authorization token can be found in your Admin console.
    :type authorization: str
    :param sku_seller_id: SKU ID do Lojista.
    :type sku_seller_id: str

    """
    return web.Response(status=200)


async def product_sku_seller_id_prices_put(request: web.Request, authorization, sku_seller_id, body) -> web.Response:
    """Allows seller to update prices of a single SKU

    Allows seller to set the SKU prices (MSRP and/or offer price). All prices must be informed in cents. No commas or periods are accepeted. For example one dollar should be informed as 100. Same as $1,2345.67 must be informed solely as 1234567

    :param authorization: Authorization token. The Authorization token can be found in your Admin console.
    :type authorization: str
    :param sku_seller_id: Product SKU
    :type sku_seller_id: str
    :param body: JSON document with the SKU price
    :type body: dict | bytes

    """
    body = ProductPrice.from_dict(body)
    return web.Response(status=200)


async def product_sku_seller_id_status_put(request: web.Request, authorization, sku_seller_id, body) -> web.Response:
    """Enable/disable a single product in the Marketplace

    Update product status in the Marketplace. Set to &#x60;true&#x60; to enable, &#x60;false&#x60; to disable sale.

    :param authorization: Authorization token. The Authorization token can be found in your Admin console.
    :type authorization: str
    :param sku_seller_id: Unique Product Id (SKU) in the seller system
    :type sku_seller_id: str
    :param body: Seller SKU that will be enabled or disabled
    :type body: dict | bytes

    """
    body = SellerItemStatus.from_dict(body)
    return web.Response(status=200)


async def product_sku_seller_id_stock_put(request: web.Request, authorization, sku_seller_id, body) -> web.Response:
    """Update a single product stock

    Update a single product inventory information. Products with zero stock will not be eligible for sale.

    :param authorization: Authorization token. The Authorization token can be found in your Admin console.
    :type authorization: str
    :param sku_seller_id: Unique Product Id (SKU) in the seller system that will be updated
    :type sku_seller_id: str
    :param body: New product inventory information
    :type body: dict | bytes

    """
    body = Stock.from_dict(body)
    return web.Response(status=200)
