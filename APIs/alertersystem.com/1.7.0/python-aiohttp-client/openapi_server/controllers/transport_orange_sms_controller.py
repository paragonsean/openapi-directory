from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_transport_orange_sms_get_collection200_response import ApiTransportOrangeSmsGetCollection200Response
from openapi_server.models.transport_orange_sms_get import TransportOrangeSmsGet
from openapi_server.models.transport_orange_sms_jsonld_get import TransportOrangeSmsJsonldGet
from openapi_server.models.transport_orange_sms_jsonld_post import TransportOrangeSmsJsonldPost
from openapi_server.models.transport_orange_sms_jsonld_put import TransportOrangeSmsJsonldPut
from openapi_server.models.transport_orange_sms_patch import TransportOrangeSmsPatch
from openapi_server.models.transport_orange_sms_post import TransportOrangeSmsPost
from openapi_server.models.transport_orange_sms_put import TransportOrangeSmsPut
from openapi_server import util


async def api_transport_orange_sms_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of TransportOrangeSms resources.

    Retrieves the collection of TransportOrangeSms resources.

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


async def api_transport_orange_sms_id_delete(request: web.Request, id) -> web.Response:
    """Removes the TransportOrangeSms resource.

    Removes the TransportOrangeSms resource.

    :param id: TransportOrangeSms identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_orange_sms_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TransportOrangeSms resource.

    Retrieves a TransportOrangeSms resource.

    :param id: TransportOrangeSms identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_orange_sms_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the TransportOrangeSms resource.

    Updates the TransportOrangeSms resource.

    :param id: TransportOrangeSms identifier
    :type id: str
    :param body: The updated TransportOrangeSms resource
    :type body: dict | bytes

    """
    body = TransportOrangeSmsPatch.from_dict(body)
    return web.Response(status=200)


async def api_transport_orange_sms_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the TransportOrangeSms resource.

    Replaces the TransportOrangeSms resource.

    :param id: TransportOrangeSms identifier
    :type id: str
    :param body: The updated TransportOrangeSms resource
    :type body: dict | bytes

    """
    body = TransportOrangeSmsPut.from_dict(body)
    return web.Response(status=200)


async def api_transport_orange_sms_post(request: web.Request, body) -> web.Response:
    """Creates a TransportOrangeSms resource.

    Creates a TransportOrangeSms resource.

    :param body: The new TransportOrangeSms resource
    :type body: dict | bytes

    """
    body = TransportOrangeSmsPost.from_dict(body)
    return web.Response(status=200)
