from typing import List, Dict
from aiohttp import web

from openapi_server.models.attribute_trait import AttributeTrait
from openapi_server.models.items_attribute_trait import ItemsAttributeTrait
from openapi_server import util


async def attribute_trait_get(request: web.Request, name, selected_fields=None) -> web.Response:
    """Retrieve an attribute trait.

    

    :param name: The name or abbreviation of the attribute trait.
    :type name: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str

    """
    return web.Response(status=200)


async def attribute_trait_get_by_category(request: web.Request, category, selected_fields=None) -> web.Response:
    """Retrieve all attribute traits of the specified category/categories.

    

    :param category: The category of the attribute traits. Multiple categories may be specified with multiple instances of the parameter. If the parameter is not specified, or if its value is \&quot;all\&quot;, then all attribute traits of all categories will be returned.
    :type category: List[str]
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str

    """
    return web.Response(status=200)
