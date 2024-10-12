from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_products_response import GetProductsResponse
from openapi_server.models.get_products_status_selling import GetProductsStatusSelling
from openapi_server.models.get_seller_products_status import GetSellerProductsStatus
from openapi_server.models.product import Product
from openapi_server.models.product_status_update import ProductStatusUpdate
from openapi_server.models.product_stock import ProductStock
from openapi_server.models.product_update import ProductUpdate
from openapi_server.models.seller_item_prices import SellerItemPrices
from openapi_server import util


async def product_sku_seller_id_put(request: web.Request, authorization, sku_seller_id, body) -> web.Response:
    """Update product details

    Update a single product information such as name, brand, attribute, dimension, etc. Please note that data from your request will be merged with existing data. This allows you to easliy update only certain fields without the need to re-inform the other unchanged fields. For example in order to update just the field &#x60;title&#x60; simply send just this field with new information, remaining fields will not be changed. In order to erase an item the field must be informed as its default value, for example in order to erase the &#x60;videos&#x60; field must be sent as videos:[]. The &#x60;skuSellerId&#x60; field is always mandatory in the path and in the product json Object.

    :param authorization: Authorization token. The Authorization token can be found in your Admin console.
    :type authorization: str
    :param sku_seller_id: Unique Product Id (SKU) in the seller system that will be updated.
    :type sku_seller_id: str
    :param body: New product information.
    :type body: dict | bytes

    """
    body = ProductUpdate.from_dict(body)
    return web.Response(status=200)


async def products_get(request: web.Request, authorization, offset=None, limit=None) -> web.Response:
    """Returns a list of products loaded into BrandLovers Marketplace

    Get a list of my products loaded into the Marketplace. This dosen&#39;t means that products are eligible for sale, just that they are loaded in the database.

    :param authorization: Authorization token. The Authorization token can be found in your Admin console.
    :type authorization: str
    :param offset: Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with &#x60;limit&#x60; to paginate across the results.
    :type offset: int
    :param limit: Number of items to retun. Defaults to 100. Max alowed is 200. Use this conjuction with &#x60;offset&#x60; to paginate across the results.
    :type limit: int

    """
    return web.Response(status=200)


async def products_post(request: web.Request, authorization, products) -> web.Response:
    """Allows new products from the seller to be loaded into the marketplace

    This enpoint to creates new products in the Marketplace using &#x60;skuSellerId&#x60; as a primary key. This enpoint expects a json document with array of products. The server will load each product as an individual item that can be manipulated using your own &#x60;skuSellerId&#x60;. All requests to This endpoint are idenpontent with respect of the &#x60;skuSellerId&#x60;, this means that once a &#x60;skuSellerId&#x60; is created it cannot be re-created using this tool. In order to update use the PUT method with the correct &#x60;skuSellerId&#x60;. You can also use the POST /product to create a single product per request

    :param authorization: Authorization token. The Authorization token can be found in your Admin console.
    :type authorization: str
    :param products: JSON with a list of new products to be updloaded to the platform
    :type products: list | bytes

    """
    products = [Product.from_dict(d) for d in products]
    return web.Response(status=200)


async def products_prices_put(request: web.Request, authorization, body) -> web.Response:
    """Allows bulk update of product prices.

    Allows bulk update of product prices. This endpoint expects a json document with an array of products with the &#x60;skuSellerId&#x60; and the new price. Server will process each new product update individually and will ackwlodge as much updates as possible, even if a single product update fails. After this request you can query product final status with GET /product/status

    :param authorization: Authorization token. The Authorization token can be found in your Admin console.
    :type authorization: str
    :param body: Data for bulk product price update
    :type body: list | bytes

    """
    body = [SellerItemPrices.from_dict(d) for d in body]
    return web.Response(status=200)


async def products_status_get(request: web.Request, authorization, offset=None, limit=None) -> web.Response:
    """Returns seller products status in the marketplace

    Returns a list with seller products status. Please note that this endpoint will not return all details of each product, just the skuSellerId and status. Also please note that this endpoint will return 250 products per call. For full details of a given procuct use GET /product/{skuSellerId}

    :param authorization: Authorization token. The Authorization token can be found in your Admin console.
    :type authorization: str
    :param offset: Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with &#x60;limit&#x60; to paginate across the results.
    :type offset: int
    :param limit: Number of items to return in this query. Defaults to 250. Maximum 1000. Use this conjuction with &#x60;offset&#x60; to paginate across the results.
    :type limit: int

    """
    return web.Response(status=200)


async def products_status_put(request: web.Request, authorization, body) -> web.Response:
    """Bulk enable/disable products in the marketplace

    Bulk enable/disable products in the marketplace. This endpoint requires an array of objects with the seller SKU &#x60;skuSellerId&#x60; and boolean value that defines if the product is enabled or not for sale. This endpoint can be used to set a single product or many products.

    :param authorization: Authorization token. The Authorization token can be found in your Admin console.
    :type authorization: str
    :param body: List of seller products with new status information
    :type body: list | bytes

    """
    body = [ProductStatusUpdate.from_dict(d) for d in body]
    return web.Response(status=200)


async def products_status_selling_get(request: web.Request, authorization, offset=None, limit=None) -> web.Response:
    """Returns products that are successfully listed for sale.

    Returns products that are successfully listed for sale.

    :param authorization: Authorization token. The Authorization token can be found in your Admin console.
    :type authorization: str
    :param offset: Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with &#x60;limit&#x60; to paginate across the results.
    :type offset: int
    :param limit: Number or items to return when executing query. Defaults to 10. Use this conjuction with &#x60;offset&#x60; to paginate across the results.
    :type limit: int

    """
    return web.Response(status=200)


async def products_stocks_put(request: web.Request, authorization, body) -> web.Response:
    """Bulk product stock update

    Bulk product stock update. This endpoint expect a array of products &#x60;skuSellerId&#x60; with new inventory data

    :param authorization: Authorization token. The Authorization token can be found in your Admin console.
    :type authorization: str
    :param body: Array of product SKUs.
    :type body: list | bytes

    """
    body = [ProductStock.from_dict(d) for d in body]
    return web.Response(status=200)
