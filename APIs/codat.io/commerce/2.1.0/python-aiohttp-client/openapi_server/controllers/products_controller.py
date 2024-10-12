from typing import List, Dict
from aiohttp import web

from openapi_server.models.product_categories import ProductCategories
from openapi_server.models.products import Products
from openapi_server import util


async def list_product_categories(request: web.Request, page, page_size=None, query=None, order_by=None) -> web.Response:
    """List product categories

    Product categories are used to classify a group of products together, either by type (eg \&quot;Furniture\&quot;), or sometimes by tax profile.

    :param page: Page number. [Read more](https://docs.codat.io/using-the-api/paging).
    :type page: int
    :param page_size: Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging).
    :type page_size: int
    :param query: Codat query string. [Read more](https://docs.codat.io/using-the-api/querying).
    :type query: str
    :param order_by: Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results).
    :type order_by: str

    """
    return web.Response(status=200)


async def list_products(request: web.Request, page, page_size=None, query=None, order_by=None) -> web.Response:
    """List products

    The Products data type provides the company&#39;s product inventory, and includes the price and quantity of all products, and product variants, available for sale.

    :param page: Page number. [Read more](https://docs.codat.io/using-the-api/paging).
    :type page: int
    :param page_size: Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging).
    :type page_size: int
    :param query: Codat query string. [Read more](https://docs.codat.io/using-the-api/querying).
    :type query: str
    :param order_by: Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results).
    :type order_by: str

    """
    return web.Response(status=200)
