from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_timezone_code_get_collection200_response import ApiTimezoneCodeGetCollection200Response
from openapi_server.models.timezone_code_get import TimezoneCodeGet
from openapi_server.models.timezone_code_jsonld_get import TimezoneCodeJsonldGet
from openapi_server import util


async def api_timezone_code_get_collection(request: web.Request, page=None, properties=None) -> web.Response:
    """Retrieves the collection of TimezoneCode resources.

    Retrieves the collection of TimezoneCode resources.

    :param page: The collection page number
    :type page: int
    :param properties: Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]&#x3D;{propertyName}&amp;properties[]&#x3D;{anotherPropertyName}&amp;properties[{nestedPropertyParent}][]&#x3D;{nestedProperty}
    :type properties: List[str]

    """
    return web.Response(status=200)


async def api_timezone_code_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TimezoneCode resource.

    Retrieves a TimezoneCode resource.

    :param id: TimezoneCode identifier
    :type id: str

    """
    return web.Response(status=200)
