from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_transport_simple_textin_get_collection200_response import ApiTransportSimpleTextinGetCollection200Response
from openapi_server.models.transport_simple_textin_get import TransportSimpleTextinGet
from openapi_server.models.transport_simple_textin_jsonld_get import TransportSimpleTextinJsonldGet
from openapi_server.models.transport_simple_textin_jsonld_post import TransportSimpleTextinJsonldPost
from openapi_server.models.transport_simple_textin_jsonld_put import TransportSimpleTextinJsonldPut
from openapi_server.models.transport_simple_textin_patch import TransportSimpleTextinPatch
from openapi_server.models.transport_simple_textin_post import TransportSimpleTextinPost
from openapi_server.models.transport_simple_textin_put import TransportSimpleTextinPut
from openapi_server import util


async def api_transport_simple_textin_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of TransportSimpleTextin resources.

    Retrieves the collection of TransportSimpleTextin resources.

    :param page: The collection page number
    :type page: int
    :param data_segment_code: 
    :type data_segment_code: str
    :param data_segment_code2: 
    :type data_segment_code2: List[str]
    :param partition: 
    :type partition: str
    :param partition2: 
    :type partition2: List[str]
    :param properties: Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]&#x3D;{propertyName}&amp;properties[]&#x3D;{anotherPropertyName}&amp;properties[{nestedPropertyParent}][]&#x3D;{nestedProperty}
    :type properties: List[str]

    """
    return web.Response(status=200)


async def api_transport_simple_textin_id_delete(request: web.Request, id) -> web.Response:
    """Removes the TransportSimpleTextin resource.

    Removes the TransportSimpleTextin resource.

    :param id: TransportSimpleTextin identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_simple_textin_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TransportSimpleTextin resource.

    Retrieves a TransportSimpleTextin resource.

    :param id: TransportSimpleTextin identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_simple_textin_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the TransportSimpleTextin resource.

    Updates the TransportSimpleTextin resource.

    :param id: TransportSimpleTextin identifier
    :type id: str
    :param body: The updated TransportSimpleTextin resource
    :type body: dict | bytes

    """
    body = TransportSimpleTextinPatch.from_dict(body)
    return web.Response(status=200)


async def api_transport_simple_textin_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the TransportSimpleTextin resource.

    Replaces the TransportSimpleTextin resource.

    :param id: TransportSimpleTextin identifier
    :type id: str
    :param body: The updated TransportSimpleTextin resource
    :type body: dict | bytes

    """
    body = TransportSimpleTextinPut.from_dict(body)
    return web.Response(status=200)


async def api_transport_simple_textin_post(request: web.Request, body) -> web.Response:
    """Creates a TransportSimpleTextin resource.

    Creates a TransportSimpleTextin resource.

    :param body: The new TransportSimpleTextin resource
    :type body: dict | bytes

    """
    body = TransportSimpleTextinPost.from_dict(body)
    return web.Response(status=200)
