from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_transport_sms77_get_collection200_response import ApiTransportSms77GetCollection200Response
from openapi_server.models.transport_sms77_get import TransportSms77Get
from openapi_server.models.transport_sms77_jsonld_get import TransportSms77JsonldGet
from openapi_server.models.transport_sms77_jsonld_post import TransportSms77JsonldPost
from openapi_server.models.transport_sms77_jsonld_put import TransportSms77JsonldPut
from openapi_server.models.transport_sms77_patch import TransportSms77Patch
from openapi_server.models.transport_sms77_post import TransportSms77Post
from openapi_server.models.transport_sms77_put import TransportSms77Put
from openapi_server import util


async def api_transport_sms77_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of TransportSms77 resources.

    Retrieves the collection of TransportSms77 resources.

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


async def api_transport_sms77_id_delete(request: web.Request, id) -> web.Response:
    """Removes the TransportSms77 resource.

    Removes the TransportSms77 resource.

    :param id: TransportSms77 identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_sms77_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TransportSms77 resource.

    Retrieves a TransportSms77 resource.

    :param id: TransportSms77 identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_sms77_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the TransportSms77 resource.

    Updates the TransportSms77 resource.

    :param id: TransportSms77 identifier
    :type id: str
    :param body: The updated TransportSms77 resource
    :type body: dict | bytes

    """
    body = TransportSms77Patch.from_dict(body)
    return web.Response(status=200)


async def api_transport_sms77_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the TransportSms77 resource.

    Replaces the TransportSms77 resource.

    :param id: TransportSms77 identifier
    :type id: str
    :param body: The updated TransportSms77 resource
    :type body: dict | bytes

    """
    body = TransportSms77Put.from_dict(body)
    return web.Response(status=200)


async def api_transport_sms77_post(request: web.Request, body) -> web.Response:
    """Creates a TransportSms77 resource.

    Creates a TransportSms77 resource.

    :param body: The new TransportSms77 resource
    :type body: dict | bytes

    """
    body = TransportSms77Post.from_dict(body)
    return web.Response(status=200)
