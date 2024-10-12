from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_transport_mobyt_get_collection200_response import ApiTransportMobytGetCollection200Response
from openapi_server.models.transport_mobyt_get import TransportMobytGet
from openapi_server.models.transport_mobyt_jsonld_get import TransportMobytJsonldGet
from openapi_server.models.transport_mobyt_jsonld_post import TransportMobytJsonldPost
from openapi_server.models.transport_mobyt_jsonld_put import TransportMobytJsonldPut
from openapi_server.models.transport_mobyt_patch import TransportMobytPatch
from openapi_server.models.transport_mobyt_post import TransportMobytPost
from openapi_server.models.transport_mobyt_put import TransportMobytPut
from openapi_server import util


async def api_transport_mobyt_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of TransportMobyt resources.

    Retrieves the collection of TransportMobyt resources.

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


async def api_transport_mobyt_id_delete(request: web.Request, id) -> web.Response:
    """Removes the TransportMobyt resource.

    Removes the TransportMobyt resource.

    :param id: TransportMobyt identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_mobyt_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TransportMobyt resource.

    Retrieves a TransportMobyt resource.

    :param id: TransportMobyt identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_mobyt_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the TransportMobyt resource.

    Updates the TransportMobyt resource.

    :param id: TransportMobyt identifier
    :type id: str
    :param body: The updated TransportMobyt resource
    :type body: dict | bytes

    """
    body = TransportMobytPatch.from_dict(body)
    return web.Response(status=200)


async def api_transport_mobyt_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the TransportMobyt resource.

    Replaces the TransportMobyt resource.

    :param id: TransportMobyt identifier
    :type id: str
    :param body: The updated TransportMobyt resource
    :type body: dict | bytes

    """
    body = TransportMobytPut.from_dict(body)
    return web.Response(status=200)


async def api_transport_mobyt_post(request: web.Request, body) -> web.Response:
    """Creates a TransportMobyt resource.

    Creates a TransportMobyt resource.

    :param body: The new TransportMobyt resource
    :type body: dict | bytes

    """
    body = TransportMobytPost.from_dict(body)
    return web.Response(status=200)
