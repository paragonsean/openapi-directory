from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_transport_light_sms_get_collection200_response import ApiTransportLightSmsGetCollection200Response
from openapi_server.models.transport_light_sms_get import TransportLightSmsGet
from openapi_server.models.transport_light_sms_jsonld_get import TransportLightSmsJsonldGet
from openapi_server.models.transport_light_sms_jsonld_post import TransportLightSmsJsonldPost
from openapi_server.models.transport_light_sms_jsonld_put import TransportLightSmsJsonldPut
from openapi_server.models.transport_light_sms_patch import TransportLightSmsPatch
from openapi_server.models.transport_light_sms_post import TransportLightSmsPost
from openapi_server.models.transport_light_sms_put import TransportLightSmsPut
from openapi_server import util


async def api_transport_light_sms_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of TransportLightSms resources.

    Retrieves the collection of TransportLightSms resources.

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


async def api_transport_light_sms_id_delete(request: web.Request, id) -> web.Response:
    """Removes the TransportLightSms resource.

    Removes the TransportLightSms resource.

    :param id: TransportLightSms identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_light_sms_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TransportLightSms resource.

    Retrieves a TransportLightSms resource.

    :param id: TransportLightSms identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_light_sms_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the TransportLightSms resource.

    Updates the TransportLightSms resource.

    :param id: TransportLightSms identifier
    :type id: str
    :param body: The updated TransportLightSms resource
    :type body: dict | bytes

    """
    body = TransportLightSmsPatch.from_dict(body)
    return web.Response(status=200)


async def api_transport_light_sms_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the TransportLightSms resource.

    Replaces the TransportLightSms resource.

    :param id: TransportLightSms identifier
    :type id: str
    :param body: The updated TransportLightSms resource
    :type body: dict | bytes

    """
    body = TransportLightSmsPut.from_dict(body)
    return web.Response(status=200)


async def api_transport_light_sms_post(request: web.Request, body) -> web.Response:
    """Creates a TransportLightSms resource.

    Creates a TransportLightSms resource.

    :param body: The new TransportLightSms resource
    :type body: dict | bytes

    """
    body = TransportLightSmsPost.from_dict(body)
    return web.Response(status=200)
