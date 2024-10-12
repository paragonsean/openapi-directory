from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_transport_message_media_get_collection200_response import ApiTransportMessageMediaGetCollection200Response
from openapi_server.models.transport_message_media_get import TransportMessageMediaGet
from openapi_server.models.transport_message_media_jsonld_get import TransportMessageMediaJsonldGet
from openapi_server.models.transport_message_media_jsonld_post import TransportMessageMediaJsonldPost
from openapi_server.models.transport_message_media_jsonld_put import TransportMessageMediaJsonldPut
from openapi_server.models.transport_message_media_patch import TransportMessageMediaPatch
from openapi_server.models.transport_message_media_post import TransportMessageMediaPost
from openapi_server.models.transport_message_media_put import TransportMessageMediaPut
from openapi_server import util


async def api_transport_message_media_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of TransportMessageMedia resources.

    Retrieves the collection of TransportMessageMedia resources.

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


async def api_transport_message_media_id_delete(request: web.Request, id) -> web.Response:
    """Removes the TransportMessageMedia resource.

    Removes the TransportMessageMedia resource.

    :param id: TransportMessageMedia identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_message_media_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TransportMessageMedia resource.

    Retrieves a TransportMessageMedia resource.

    :param id: TransportMessageMedia identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_message_media_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the TransportMessageMedia resource.

    Updates the TransportMessageMedia resource.

    :param id: TransportMessageMedia identifier
    :type id: str
    :param body: The updated TransportMessageMedia resource
    :type body: dict | bytes

    """
    body = TransportMessageMediaPatch.from_dict(body)
    return web.Response(status=200)


async def api_transport_message_media_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the TransportMessageMedia resource.

    Replaces the TransportMessageMedia resource.

    :param id: TransportMessageMedia identifier
    :type id: str
    :param body: The updated TransportMessageMedia resource
    :type body: dict | bytes

    """
    body = TransportMessageMediaPut.from_dict(body)
    return web.Response(status=200)


async def api_transport_message_media_post(request: web.Request, body) -> web.Response:
    """Creates a TransportMessageMedia resource.

    Creates a TransportMessageMedia resource.

    :param body: The new TransportMessageMedia resource
    :type body: dict | bytes

    """
    body = TransportMessageMediaPost.from_dict(body)
    return web.Response(status=200)
