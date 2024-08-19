from typing import List, Dict
from aiohttp import web

from openapi_server.models.product import Product
from openapi_server.models.product_patch import ProductPatch
from openapi_server.models.product_post import ProductPost
from openapi_server import util


async def create_product(request: web.Request, authorization, product) -> web.Response:
    """Create a new product in eCommerce system.With the exception of the &#39;id&#39; field, the required fields indicated in the &#39;Product&#39; model are those required to create a new product

    

    :param authorization: The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39;
    :type authorization: str
    :param product: The product object to be created
    :type product: dict | bytes

    """
    product = ProductPost.from_dict(product)
    return web.Response(status=200)


async def delete_product_by_id(request: web.Request, authorization, id) -> web.Response:
    """Delete a product associated with a given ID from your eCommerce system. Specifying a product associated with a given ID that does not exist will result in an error message

    

    :param authorization: The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39;
    :type authorization: str
    :param id: The ID of the product to delete from the eCommerce system
    :type id: str

    """
    return web.Response(status=200)


async def get_product_by_id(request: web.Request, authorization, id) -> web.Response:
    """Retrieve a product associated with a given ID from the eCommerce system. Specifying a product with an ID that does not exist will result in an error response

    

    :param authorization: The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39;
    :type authorization: str
    :param id: The ID of the product to retrieve from the eCommerce system
    :type id: str

    """
    return web.Response(status=200)


async def get_products(request: web.Request, authorization, where=None, page_size=None, next_page=None, fields=None) -> web.Response:
    """Find products in the eCommerce system, using the provided CEQL search expression. The search expression in CEQL is the WHERE clause in a typical SQL query, but without the WHERE keyword.  If no search expression is provided, all records will be retrieved

    

    :param authorization: The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39;
    :type authorization: str
    :param where: The CEQL search expression, or the where clause, without the WHERE keyword, in a typical SQL query (i.e. field&#x3D;&#39;value&#39;). &lt;p&gt;Supported search terms: category, hidden_products. All other search criteria are ignored
    :type where: str
    :param page_size: The number of results to fetch in a given page. When this parameter is omitted, a maximum of 200 results are returned
    :type page_size: int
    :param next_page: The next page cursor, taken from the response header: &#x60;elements-next-page-token&#x60;
    :type next_page: str
    :param fields: The fields to return on the response. Can be a single field or a comma-separated list of fields
    :type fields: str

    """
    return web.Response(status=200)


async def update_product_by_id(request: web.Request, authorization, id, product) -> web.Response:
    """Update a product associated with a given ID in the eCommerce system. The update API uses the PATCH HTTP verb, so only those fields provided in the product object will be updated, and those fields not provided will be left alone. Updating a product with a specified ID that does not exist will result in an error response. &lt;p&gt;&lt;strong&gt;Update supports the following fields: sku, quantity, trackQuantity, quantityDelta, warningLimit, name, price, weight, tangible, enabled, fixedShippingRateOnly, fixedShippingRate, description, wholesalePrices, compareAtPrice, productClassId&lt;/strong&gt;

    

    :param authorization: The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39;
    :type authorization: str
    :param id: The ID of the product to update in the eCommerce system
    :type id: str
    :param product: The product object, with those fields that are to be updated
    :type product: dict | bytes

    """
    product = ProductPatch.from_dict(product)
    return web.Response(status=200)
