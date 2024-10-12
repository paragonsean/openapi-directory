from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_transport_sendberry_get_collection200_response import ApiTransportSendberryGetCollection200Response
from openapi_server.models.transport_sendberry_get import TransportSendberryGet
from openapi_server.models.transport_sendberry_jsonld_get import TransportSendberryJsonldGet
from openapi_server.models.transport_sendberry_jsonld_post import TransportSendberryJsonldPost
from openapi_server.models.transport_sendberry_jsonld_put import TransportSendberryJsonldPut
from openapi_server.models.transport_sendberry_patch import TransportSendberryPatch
from openapi_server.models.transport_sendberry_post import TransportSendberryPost
from openapi_server.models.transport_sendberry_put import TransportSendberryPut
from openapi_server import util


async def api_transport_sendberry_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of TransportSendberry resources.

    Retrieves the collection of TransportSendberry resources.

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


async def api_transport_sendberry_id_delete(request: web.Request, id) -> web.Response:
    """Removes the TransportSendberry resource.

    Removes the TransportSendberry resource.

    :param id: TransportSendberry identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_sendberry_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TransportSendberry resource.

    Retrieves a TransportSendberry resource.

    :param id: TransportSendberry identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_sendberry_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the TransportSendberry resource.

    Updates the TransportSendberry resource.

    :param id: TransportSendberry identifier
    :type id: str
    :param body: The updated TransportSendberry resource
    :type body: dict | bytes

    """
    body = TransportSendberryPatch.from_dict(body)
    return web.Response(status=200)


async def api_transport_sendberry_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the TransportSendberry resource.

    Replaces the TransportSendberry resource.

    :param id: TransportSendberry identifier
    :type id: str
    :param body: The updated TransportSendberry resource
    :type body: dict | bytes

    """
    body = TransportSendberryPut.from_dict(body)
    return web.Response(status=200)


async def api_transport_sendberry_post(request: web.Request, body) -> web.Response:
    """Creates a TransportSendberry resource.

    Creates a TransportSendberry resource.

    :param body: The new TransportSendberry resource
    :type body: dict | bytes

    """
    body = TransportSendberryPost.from_dict(body)
    return web.Response(status=200)
