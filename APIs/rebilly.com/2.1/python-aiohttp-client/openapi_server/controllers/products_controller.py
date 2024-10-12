from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.invalid_error import InvalidError
from openapi_server.models.product import Product
from openapi_server import util


async def delete_product(request: web.Request, id, organization_id=None) -> web.Response:
    """Delete a product

    Delete a product with predefined identifier string. 

    :param id: The resource identifier string.
    :type id: str
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_product(request: web.Request, id, organization_id=None) -> web.Response:
    """Retrieve a product

    Retrieve a product with specified identifier string. 

    :param id: The resource identifier string.
    :type id: str
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_product_collection(request: web.Request, organization_id=None, filter=None, sort=None, limit=None, offset=None, q=None) -> web.Response:
    """Retrieve a list of products

    Retrieve a list of products. 

    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str
    :param filter: The collection items filter requires a special format. Use \&quot;,\&quot; for multiple allowed values.  Use \&quot;;\&quot; for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format. 
    :type filter: str
    :param sort: The collection items sort field and order (prefix with \&quot;-\&quot; for descending sort).
    :type sort: List[str]
    :param limit: The collection items limit.
    :type limit: int
    :param offset: The collection items offset.
    :type offset: int
    :param q: The partial search of the text fields.
    :type q: str

    """
    return web.Response(status=200)


async def post_product(request: web.Request, body, organization_id=None) -> web.Response:
    """Create a Product

    Create a Product. 

    :param body: Product resource.
    :type body: dict | bytes
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    body = Product.from_dict(body)
    return web.Response(status=200)


async def put_product(request: web.Request, id, body, organization_id=None) -> web.Response:
    """Create a product with predefined ID

    Create a product with predefined identifier string. 

    :param id: The resource identifier string.
    :type id: str
    :param body: Product resource.
    :type body: dict | bytes
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    body = Product.from_dict(body)
    return web.Response(status=200)
