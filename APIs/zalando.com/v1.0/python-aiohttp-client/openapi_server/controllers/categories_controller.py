from typing import List, Dict
from aiohttp import web

from openapi_server.models.categories import Categories
from openapi_server.models.category import Category
from openapi_server.models.error_message import ErrorMessage
from openapi_server import util


async def categories_get(request: web.Request, name=None, type=None, outlet=None, hidden=None, target_group=None, key=None, parent_key=None, child_key=None, suggested_filter=None, page=None, page_size=None, accept_language=None, fields=None) -> web.Response:
    """Shop Categories

    Zalando API Categories Schema

    :param name: Request Categories by names
    :type name: List[str]
    :param type: Request Categories by type
    :type type: str
    :param outlet: Request Categories by outlet
    :type outlet: str
    :param hidden: Request Categories by hidden
    :type hidden: str
    :param target_group: Request Categories by target group
    :type target_group: str
    :param key: Request Categories by keys
    :type key: List[str]
    :param parent_key: Request Categories by parent keys
    :type parent_key: List[str]
    :param child_key: Request Categories by child keys
    :type child_key: List[str]
    :param suggested_filter: Request Categories by suggested filters
    :type suggested_filter: List[str]
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


async def categories_key_get(request: web.Request, key, accept_language=None, fields=None) -> web.Response:
    """Get Single Category by Key

    Zalando API Category Schema

    :param key: To get unique Category by key.
    :type key: List[str]
    :param accept_language: Specify which Shop to use.  A standard &#x60;Accept-Language&#x60; header which specifies the shop that should be used. E.g. &#x60;de-DE&#x60; will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and &#x60;de-AT&#x60; will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries.
    :type accept_language: str
    :param fields: Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted
    :type fields: List[str]

    """
    return web.Response(status=200)
