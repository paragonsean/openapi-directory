from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_transport_turbo_sms_get_collection200_response import ApiTransportTurboSmsGetCollection200Response
from openapi_server.models.transport_turbo_sms_get import TransportTurboSmsGet
from openapi_server.models.transport_turbo_sms_jsonld_get import TransportTurboSmsJsonldGet
from openapi_server.models.transport_turbo_sms_jsonld_post import TransportTurboSmsJsonldPost
from openapi_server.models.transport_turbo_sms_jsonld_put import TransportTurboSmsJsonldPut
from openapi_server.models.transport_turbo_sms_patch import TransportTurboSmsPatch
from openapi_server.models.transport_turbo_sms_post import TransportTurboSmsPost
from openapi_server.models.transport_turbo_sms_put import TransportTurboSmsPut
from openapi_server import util


async def api_transport_turbo_sms_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of TransportTurboSms resources.

    Retrieves the collection of TransportTurboSms resources.

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


async def api_transport_turbo_sms_id_delete(request: web.Request, id) -> web.Response:
    """Removes the TransportTurboSms resource.

    Removes the TransportTurboSms resource.

    :param id: TransportTurboSms identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_turbo_sms_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TransportTurboSms resource.

    Retrieves a TransportTurboSms resource.

    :param id: TransportTurboSms identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_turbo_sms_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the TransportTurboSms resource.

    Updates the TransportTurboSms resource.

    :param id: TransportTurboSms identifier
    :type id: str
    :param body: The updated TransportTurboSms resource
    :type body: dict | bytes

    """
    body = TransportTurboSmsPatch.from_dict(body)
    return web.Response(status=200)


async def api_transport_turbo_sms_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the TransportTurboSms resource.

    Replaces the TransportTurboSms resource.

    :param id: TransportTurboSms identifier
    :type id: str
    :param body: The updated TransportTurboSms resource
    :type body: dict | bytes

    """
    body = TransportTurboSmsPut.from_dict(body)
    return web.Response(status=200)


async def api_transport_turbo_sms_post(request: web.Request, body) -> web.Response:
    """Creates a TransportTurboSms resource.

    Creates a TransportTurboSms resource.

    :param body: The new TransportTurboSms resource
    :type body: dict | bytes

    """
    body = TransportTurboSmsPost.from_dict(body)
    return web.Response(status=200)
