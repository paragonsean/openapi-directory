from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_transport_email_get_collection200_response import ApiTransportEmailGetCollection200Response
from openapi_server.models.transport_email_get import TransportEmailGet
from openapi_server.models.transport_email_jsonld_get import TransportEmailJsonldGet
from openapi_server.models.transport_email_jsonld_post import TransportEmailJsonldPost
from openapi_server.models.transport_email_jsonld_put import TransportEmailJsonldPut
from openapi_server.models.transport_email_patch import TransportEmailPatch
from openapi_server.models.transport_email_post import TransportEmailPost
from openapi_server.models.transport_email_put import TransportEmailPut
from openapi_server import util


async def api_transport_email_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of TransportEmail resources.

    Retrieves the collection of TransportEmail resources.

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


async def api_transport_email_id_delete(request: web.Request, id) -> web.Response:
    """Removes the TransportEmail resource.

    Removes the TransportEmail resource.

    :param id: TransportEmail identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_email_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TransportEmail resource.

    Retrieves a TransportEmail resource.

    :param id: TransportEmail identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_email_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the TransportEmail resource.

    Updates the TransportEmail resource.

    :param id: TransportEmail identifier
    :type id: str
    :param body: The updated TransportEmail resource
    :type body: dict | bytes

    """
    body = TransportEmailPatch.from_dict(body)
    return web.Response(status=200)


async def api_transport_email_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the TransportEmail resource.

    Replaces the TransportEmail resource.

    :param id: TransportEmail identifier
    :type id: str
    :param body: The updated TransportEmail resource
    :type body: dict | bytes

    """
    body = TransportEmailPut.from_dict(body)
    return web.Response(status=200)


async def api_transport_email_post(request: web.Request, body) -> web.Response:
    """Creates a TransportEmail resource.

    Creates a TransportEmail resource.

    :param body: The new TransportEmail resource
    :type body: dict | bytes

    """
    body = TransportEmailPost.from_dict(body)
    return web.Response(status=200)
