from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_transport_twilio_get_collection200_response import ApiTransportTwilioGetCollection200Response
from openapi_server.models.transport_twilio_get import TransportTwilioGet
from openapi_server.models.transport_twilio_jsonld_get import TransportTwilioJsonldGet
from openapi_server.models.transport_twilio_jsonld_post import TransportTwilioJsonldPost
from openapi_server.models.transport_twilio_jsonld_put import TransportTwilioJsonldPut
from openapi_server.models.transport_twilio_patch import TransportTwilioPatch
from openapi_server.models.transport_twilio_post import TransportTwilioPost
from openapi_server.models.transport_twilio_put import TransportTwilioPut
from openapi_server import util


async def api_transport_twilio_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of TransportTwilio resources.

    Retrieves the collection of TransportTwilio resources.

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


async def api_transport_twilio_id_delete(request: web.Request, id) -> web.Response:
    """Removes the TransportTwilio resource.

    Removes the TransportTwilio resource.

    :param id: TransportTwilio identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_twilio_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TransportTwilio resource.

    Retrieves a TransportTwilio resource.

    :param id: TransportTwilio identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_twilio_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the TransportTwilio resource.

    Updates the TransportTwilio resource.

    :param id: TransportTwilio identifier
    :type id: str
    :param body: The updated TransportTwilio resource
    :type body: dict | bytes

    """
    body = TransportTwilioPatch.from_dict(body)
    return web.Response(status=200)


async def api_transport_twilio_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the TransportTwilio resource.

    Replaces the TransportTwilio resource.

    :param id: TransportTwilio identifier
    :type id: str
    :param body: The updated TransportTwilio resource
    :type body: dict | bytes

    """
    body = TransportTwilioPut.from_dict(body)
    return web.Response(status=200)


async def api_transport_twilio_post(request: web.Request, body) -> web.Response:
    """Creates a TransportTwilio resource.

    Creates a TransportTwilio resource.

    :param body: The new TransportTwilio resource
    :type body: dict | bytes

    """
    body = TransportTwilioPost.from_dict(body)
    return web.Response(status=200)
