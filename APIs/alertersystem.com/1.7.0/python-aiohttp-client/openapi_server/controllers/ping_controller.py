from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_ping_get_collection200_response import ApiPingGetCollection200Response
from openapi_server.models.ping_get import PingGet
from openapi_server.models.ping_jsonld_get import PingJsonldGet
from openapi_server.models.ping_jsonld_post import PingJsonldPost
from openapi_server.models.ping_post import PingPost
from openapi_server import util


async def api_ping_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, monitor=None, monitor2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of Ping resources.

    Retrieves the collection of Ping resources.

    :param page: The collection page number
    :type page: int
    :param data_segment_code: 
    :type data_segment_code: str
    :param data_segment_code2: 
    :type data_segment_code2: List[str]
    :param monitor: 
    :type monitor: str
    :param monitor2: 
    :type monitor2: List[str]
    :param partition: 
    :type partition: str
    :param partition2: 
    :type partition2: List[str]
    :param properties: Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]&#x3D;{propertyName}&amp;properties[]&#x3D;{anotherPropertyName}&amp;properties[{nestedPropertyParent}][]&#x3D;{nestedProperty}
    :type properties: List[str]

    """
    return web.Response(status=200)


async def api_ping_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a Ping resource.

    Retrieves a Ping resource.

    :param id: Ping identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_ping_post(request: web.Request, body) -> web.Response:
    """Creates a Ping resource.

    Creates a Ping resource.

    :param body: The new Ping resource
    :type body: dict | bytes

    """
    body = PingPost.from_dict(body)
    return web.Response(status=200)
