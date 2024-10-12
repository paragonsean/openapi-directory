from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_ping_method_code_get_collection200_response import ApiPingMethodCodeGetCollection200Response
from openapi_server.models.ping_method_code_get import PingMethodCodeGet
from openapi_server.models.ping_method_code_jsonld_get import PingMethodCodeJsonldGet
from openapi_server import util


async def api_ping_method_code_get_collection(request: web.Request, page=None, properties=None) -> web.Response:
    """Retrieves the collection of PingMethodCode resources.

    Retrieves the collection of PingMethodCode resources.

    :param page: The collection page number
    :type page: int
    :param properties: Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]&#x3D;{propertyName}&amp;properties[]&#x3D;{anotherPropertyName}&amp;properties[{nestedPropertyParent}][]&#x3D;{nestedProperty}
    :type properties: List[str]

    """
    return web.Response(status=200)


async def api_ping_method_code_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a PingMethodCode resource.

    Retrieves a PingMethodCode resource.

    :param id: PingMethodCode identifier
    :type id: str

    """
    return web.Response(status=200)
