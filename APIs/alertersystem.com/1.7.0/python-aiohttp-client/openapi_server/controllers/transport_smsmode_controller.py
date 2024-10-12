from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_transport_smsmode_get_collection200_response import ApiTransportSmsmodeGetCollection200Response
from openapi_server.models.transport_smsmode_get import TransportSmsmodeGet
from openapi_server.models.transport_smsmode_jsonld_get import TransportSmsmodeJsonldGet
from openapi_server.models.transport_smsmode_jsonld_post import TransportSmsmodeJsonldPost
from openapi_server.models.transport_smsmode_jsonld_put import TransportSmsmodeJsonldPut
from openapi_server.models.transport_smsmode_patch import TransportSmsmodePatch
from openapi_server.models.transport_smsmode_post import TransportSmsmodePost
from openapi_server.models.transport_smsmode_put import TransportSmsmodePut
from openapi_server import util


async def api_transport_smsmode_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of TransportSmsmode resources.

    Retrieves the collection of TransportSmsmode resources.

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


async def api_transport_smsmode_id_delete(request: web.Request, id) -> web.Response:
    """Removes the TransportSmsmode resource.

    Removes the TransportSmsmode resource.

    :param id: TransportSmsmode identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_smsmode_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TransportSmsmode resource.

    Retrieves a TransportSmsmode resource.

    :param id: TransportSmsmode identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_smsmode_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the TransportSmsmode resource.

    Updates the TransportSmsmode resource.

    :param id: TransportSmsmode identifier
    :type id: str
    :param body: The updated TransportSmsmode resource
    :type body: dict | bytes

    """
    body = TransportSmsmodePatch.from_dict(body)
    return web.Response(status=200)


async def api_transport_smsmode_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the TransportSmsmode resource.

    Replaces the TransportSmsmode resource.

    :param id: TransportSmsmode identifier
    :type id: str
    :param body: The updated TransportSmsmode resource
    :type body: dict | bytes

    """
    body = TransportSmsmodePut.from_dict(body)
    return web.Response(status=200)


async def api_transport_smsmode_post(request: web.Request, body) -> web.Response:
    """Creates a TransportSmsmode resource.

    Creates a TransportSmsmode resource.

    :param body: The new TransportSmsmode resource
    :type body: dict | bytes

    """
    body = TransportSmsmodePost.from_dict(body)
    return web.Response(status=200)
