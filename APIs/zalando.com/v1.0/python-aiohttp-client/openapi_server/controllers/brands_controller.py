from typing import List, Dict
from aiohttp import web

from openapi_server.models.brand import Brand
from openapi_server.models.brands import Brands
from openapi_server.models.error_message import ErrorMessage
from openapi_server import util


async def brands_get(request: web.Request, key=None, name=None, brand_family_name=None, brand_family_key=None, page=None, page_size=None, accept_language=None, fields=None) -> web.Response:
    """Shop Brands

    Zalando API Brands Schema

    :param key: Request Brand by key
    :type key: List[str]
    :param name: Request Brand by name
    :type name: List[str]
    :param brand_family_name: Request Brand by brandFamilyName
    :type brand_family_name: List[str]
    :param brand_family_key: Request Brand by brandFamilyKey
    :type brand_family_key: List[str]
    :param page: to request with required page number or pagination
    :type page: str
    :param page_size: to request with required page size in a page
    :type page_size: str
    :param accept_language: Specify which Shop to use.  A standard &#x60;Accept-Language&#x60; header which specifies the shop that should be used. E.g. &#x60;de-DE&#x60; will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and &#x60;de-AT&#x60; will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries.
    :type accept_language: str
    :param fields: Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted
    :type fields: List[str]

    """
    return web.Response(status=200)


async def brands_key_get(request: web.Request, key, accept_language=None, fields=None) -> web.Response:
    """Get Single Brand by Key

    Zalando API Brand Schema

    :param key: To get unique Brand by key.
    :type key: str
    :param accept_language: Specify which Shop to use.  A standard &#x60;Accept-Language&#x60; header which specifies the shop that should be used. E.g. &#x60;de-DE&#x60; will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and &#x60;de-AT&#x60; will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries.
    :type accept_language: str
    :param fields: Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted
    :type fields: List[str]

    """
    return web.Response(status=200)
