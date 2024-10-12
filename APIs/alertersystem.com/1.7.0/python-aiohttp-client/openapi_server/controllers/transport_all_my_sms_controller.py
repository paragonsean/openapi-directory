from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_transport_all_my_sms_get_collection200_response import ApiTransportAllMySmsGetCollection200Response
from openapi_server.models.transport_all_my_sms_get import TransportAllMySmsGet
from openapi_server.models.transport_all_my_sms_jsonld_get import TransportAllMySmsJsonldGet
from openapi_server.models.transport_all_my_sms_jsonld_post import TransportAllMySmsJsonldPost
from openapi_server.models.transport_all_my_sms_jsonld_put import TransportAllMySmsJsonldPut
from openapi_server.models.transport_all_my_sms_patch import TransportAllMySmsPatch
from openapi_server.models.transport_all_my_sms_post import TransportAllMySmsPost
from openapi_server.models.transport_all_my_sms_put import TransportAllMySmsPut
from openapi_server import util


async def api_transport_all_my_sms_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of TransportAllMySms resources.

    Retrieves the collection of TransportAllMySms resources.

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


async def api_transport_all_my_sms_id_delete(request: web.Request, id) -> web.Response:
    """Removes the TransportAllMySms resource.

    Removes the TransportAllMySms resource.

    :param id: TransportAllMySms identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_all_my_sms_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TransportAllMySms resource.

    Retrieves a TransportAllMySms resource.

    :param id: TransportAllMySms identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_all_my_sms_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the TransportAllMySms resource.

    Updates the TransportAllMySms resource.

    :param id: TransportAllMySms identifier
    :type id: str
    :param body: The updated TransportAllMySms resource
    :type body: dict | bytes

    """
    body = TransportAllMySmsPatch.from_dict(body)
    return web.Response(status=200)


async def api_transport_all_my_sms_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the TransportAllMySms resource.

    Replaces the TransportAllMySms resource.

    :param id: TransportAllMySms identifier
    :type id: str
    :param body: The updated TransportAllMySms resource
    :type body: dict | bytes

    """
    body = TransportAllMySmsPut.from_dict(body)
    return web.Response(status=200)


async def api_transport_all_my_sms_post(request: web.Request, body) -> web.Response:
    """Creates a TransportAllMySms resource.

    Creates a TransportAllMySms resource.

    :param body: The new TransportAllMySms resource
    :type body: dict | bytes

    """
    body = TransportAllMySmsPost.from_dict(body)
    return web.Response(status=200)
