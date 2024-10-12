from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_transport_sms_factor_get_collection200_response import ApiTransportSmsFactorGetCollection200Response
from openapi_server.models.transport_sms_factor_get import TransportSmsFactorGet
from openapi_server.models.transport_sms_factor_jsonld_get import TransportSmsFactorJsonldGet
from openapi_server.models.transport_sms_factor_jsonld_post import TransportSmsFactorJsonldPost
from openapi_server.models.transport_sms_factor_jsonld_put import TransportSmsFactorJsonldPut
from openapi_server.models.transport_sms_factor_patch import TransportSmsFactorPatch
from openapi_server.models.transport_sms_factor_post import TransportSmsFactorPost
from openapi_server.models.transport_sms_factor_put import TransportSmsFactorPut
from openapi_server import util


async def api_transport_sms_factor_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of TransportSmsFactor resources.

    Retrieves the collection of TransportSmsFactor resources.

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


async def api_transport_sms_factor_id_delete(request: web.Request, id) -> web.Response:
    """Removes the TransportSmsFactor resource.

    Removes the TransportSmsFactor resource.

    :param id: TransportSmsFactor identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_sms_factor_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TransportSmsFactor resource.

    Retrieves a TransportSmsFactor resource.

    :param id: TransportSmsFactor identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_sms_factor_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the TransportSmsFactor resource.

    Updates the TransportSmsFactor resource.

    :param id: TransportSmsFactor identifier
    :type id: str
    :param body: The updated TransportSmsFactor resource
    :type body: dict | bytes

    """
    body = TransportSmsFactorPatch.from_dict(body)
    return web.Response(status=200)


async def api_transport_sms_factor_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the TransportSmsFactor resource.

    Replaces the TransportSmsFactor resource.

    :param id: TransportSmsFactor identifier
    :type id: str
    :param body: The updated TransportSmsFactor resource
    :type body: dict | bytes

    """
    body = TransportSmsFactorPut.from_dict(body)
    return web.Response(status=200)


async def api_transport_sms_factor_post(request: web.Request, body) -> web.Response:
    """Creates a TransportSmsFactor resource.

    Creates a TransportSmsFactor resource.

    :param body: The new TransportSmsFactor resource
    :type body: dict | bytes

    """
    body = TransportSmsFactorPost.from_dict(body)
    return web.Response(status=200)
