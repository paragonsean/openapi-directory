from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_transport_sendinblue_get_collection200_response import ApiTransportSendinblueGetCollection200Response
from openapi_server.models.transport_sendinblue_get import TransportSendinblueGet
from openapi_server.models.transport_sendinblue_jsonld_get import TransportSendinblueJsonldGet
from openapi_server.models.transport_sendinblue_jsonld_post import TransportSendinblueJsonldPost
from openapi_server.models.transport_sendinblue_jsonld_put import TransportSendinblueJsonldPut
from openapi_server.models.transport_sendinblue_patch import TransportSendinbluePatch
from openapi_server.models.transport_sendinblue_post import TransportSendinbluePost
from openapi_server.models.transport_sendinblue_put import TransportSendinbluePut
from openapi_server import util


async def api_transport_sendinblue_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of TransportSendinblue resources.

    Retrieves the collection of TransportSendinblue resources.

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


async def api_transport_sendinblue_id_delete(request: web.Request, id) -> web.Response:
    """Removes the TransportSendinblue resource.

    Removes the TransportSendinblue resource.

    :param id: TransportSendinblue identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_sendinblue_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TransportSendinblue resource.

    Retrieves a TransportSendinblue resource.

    :param id: TransportSendinblue identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_sendinblue_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the TransportSendinblue resource.

    Updates the TransportSendinblue resource.

    :param id: TransportSendinblue identifier
    :type id: str
    :param body: The updated TransportSendinblue resource
    :type body: dict | bytes

    """
    body = TransportSendinbluePatch.from_dict(body)
    return web.Response(status=200)


async def api_transport_sendinblue_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the TransportSendinblue resource.

    Replaces the TransportSendinblue resource.

    :param id: TransportSendinblue identifier
    :type id: str
    :param body: The updated TransportSendinblue resource
    :type body: dict | bytes

    """
    body = TransportSendinbluePut.from_dict(body)
    return web.Response(status=200)


async def api_transport_sendinblue_post(request: web.Request, body) -> web.Response:
    """Creates a TransportSendinblue resource.

    Creates a TransportSendinblue resource.

    :param body: The new TransportSendinblue resource
    :type body: dict | bytes

    """
    body = TransportSendinbluePost.from_dict(body)
    return web.Response(status=200)
