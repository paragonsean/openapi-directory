from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_transport_twitter_get_collection200_response import ApiTransportTwitterGetCollection200Response
from openapi_server.models.transport_twitter_get import TransportTwitterGet
from openapi_server.models.transport_twitter_jsonld_get import TransportTwitterJsonldGet
from openapi_server.models.transport_twitter_jsonld_post import TransportTwitterJsonldPost
from openapi_server.models.transport_twitter_jsonld_put import TransportTwitterJsonldPut
from openapi_server.models.transport_twitter_patch import TransportTwitterPatch
from openapi_server.models.transport_twitter_post import TransportTwitterPost
from openapi_server.models.transport_twitter_put import TransportTwitterPut
from openapi_server import util


async def api_transport_twitter_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of TransportTwitter resources.

    Retrieves the collection of TransportTwitter resources.

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


async def api_transport_twitter_id_delete(request: web.Request, id) -> web.Response:
    """Removes the TransportTwitter resource.

    Removes the TransportTwitter resource.

    :param id: TransportTwitter identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_twitter_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TransportTwitter resource.

    Retrieves a TransportTwitter resource.

    :param id: TransportTwitter identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_twitter_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the TransportTwitter resource.

    Updates the TransportTwitter resource.

    :param id: TransportTwitter identifier
    :type id: str
    :param body: The updated TransportTwitter resource
    :type body: dict | bytes

    """
    body = TransportTwitterPatch.from_dict(body)
    return web.Response(status=200)


async def api_transport_twitter_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the TransportTwitter resource.

    Replaces the TransportTwitter resource.

    :param id: TransportTwitter identifier
    :type id: str
    :param body: The updated TransportTwitter resource
    :type body: dict | bytes

    """
    body = TransportTwitterPut.from_dict(body)
    return web.Response(status=200)


async def api_transport_twitter_post(request: web.Request, body) -> web.Response:
    """Creates a TransportTwitter resource.

    Creates a TransportTwitter resource.

    :param body: The new TransportTwitter resource
    :type body: dict | bytes

    """
    body = TransportTwitterPost.from_dict(body)
    return web.Response(status=200)
