from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_transport_iqsms_get_collection200_response import ApiTransportIqsmsGetCollection200Response
from openapi_server.models.transport_iqsms_get import TransportIqsmsGet
from openapi_server.models.transport_iqsms_jsonld_get import TransportIqsmsJsonldGet
from openapi_server.models.transport_iqsms_jsonld_post import TransportIqsmsJsonldPost
from openapi_server.models.transport_iqsms_jsonld_put import TransportIqsmsJsonldPut
from openapi_server.models.transport_iqsms_patch import TransportIqsmsPatch
from openapi_server.models.transport_iqsms_post import TransportIqsmsPost
from openapi_server.models.transport_iqsms_put import TransportIqsmsPut
from openapi_server import util


async def api_transport_iqsms_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of TransportIqsms resources.

    Retrieves the collection of TransportIqsms resources.

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


async def api_transport_iqsms_id_delete(request: web.Request, id) -> web.Response:
    """Removes the TransportIqsms resource.

    Removes the TransportIqsms resource.

    :param id: TransportIqsms identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_iqsms_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TransportIqsms resource.

    Retrieves a TransportIqsms resource.

    :param id: TransportIqsms identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_iqsms_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the TransportIqsms resource.

    Updates the TransportIqsms resource.

    :param id: TransportIqsms identifier
    :type id: str
    :param body: The updated TransportIqsms resource
    :type body: dict | bytes

    """
    body = TransportIqsmsPatch.from_dict(body)
    return web.Response(status=200)


async def api_transport_iqsms_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the TransportIqsms resource.

    Replaces the TransportIqsms resource.

    :param id: TransportIqsms identifier
    :type id: str
    :param body: The updated TransportIqsms resource
    :type body: dict | bytes

    """
    body = TransportIqsmsPut.from_dict(body)
    return web.Response(status=200)


async def api_transport_iqsms_post(request: web.Request, body) -> web.Response:
    """Creates a TransportIqsms resource.

    Creates a TransportIqsms resource.

    :param body: The new TransportIqsms resource
    :type body: dict | bytes

    """
    body = TransportIqsmsPost.from_dict(body)
    return web.Response(status=200)
