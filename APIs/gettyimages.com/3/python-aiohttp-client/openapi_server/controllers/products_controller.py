from typing import List, Dict
from aiohttp import web

from openapi_server.models.product_field_values import ProductFieldValues
from openapi_server.models.products_result import ProductsResult
from openapi_server import util


async def v3_products_get(request: web.Request, accept_language=None, fields=None) -> web.Response:
    """Get Products

    This endpoint returns all products available to the username used during authentication. As such, this endpoint requires the use of a fully authorized access_token. The product data can then be used as search filters, restricting results to images from a specific product.  You&#39;ll need an API key and access token to use this resource. 

    :param accept_language: Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
    :type accept_language: str
    :param fields: Comma separated list of fields. Allows product download requirements to be returned.
    :type fields: list | bytes

    """
    fields = [ProductFieldValues.from_dict(d) for d in fields]
    return web.Response(status=200)
