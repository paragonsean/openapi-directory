from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_transport_free_mobile_get_collection200_response import ApiTransportFreeMobileGetCollection200Response
from openapi_server.models.transport_free_mobile_get import TransportFreeMobileGet
from openapi_server.models.transport_free_mobile_jsonld_get import TransportFreeMobileJsonldGet
from openapi_server.models.transport_free_mobile_jsonld_post import TransportFreeMobileJsonldPost
from openapi_server.models.transport_free_mobile_jsonld_put import TransportFreeMobileJsonldPut
from openapi_server.models.transport_free_mobile_patch import TransportFreeMobilePatch
from openapi_server.models.transport_free_mobile_post import TransportFreeMobilePost
from openapi_server.models.transport_free_mobile_put import TransportFreeMobilePut
from openapi_server import util


async def api_transport_free_mobile_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of TransportFreeMobile resources.

    Retrieves the collection of TransportFreeMobile resources.

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


async def api_transport_free_mobile_id_delete(request: web.Request, id) -> web.Response:
    """Removes the TransportFreeMobile resource.

    Removes the TransportFreeMobile resource.

    :param id: TransportFreeMobile identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_free_mobile_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TransportFreeMobile resource.

    Retrieves a TransportFreeMobile resource.

    :param id: TransportFreeMobile identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_free_mobile_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the TransportFreeMobile resource.

    Updates the TransportFreeMobile resource.

    :param id: TransportFreeMobile identifier
    :type id: str
    :param body: The updated TransportFreeMobile resource
    :type body: dict | bytes

    """
    body = TransportFreeMobilePatch.from_dict(body)
    return web.Response(status=200)


async def api_transport_free_mobile_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the TransportFreeMobile resource.

    Replaces the TransportFreeMobile resource.

    :param id: TransportFreeMobile identifier
    :type id: str
    :param body: The updated TransportFreeMobile resource
    :type body: dict | bytes

    """
    body = TransportFreeMobilePut.from_dict(body)
    return web.Response(status=200)


async def api_transport_free_mobile_post(request: web.Request, body) -> web.Response:
    """Creates a TransportFreeMobile resource.

    Creates a TransportFreeMobile resource.

    :param body: The new TransportFreeMobile resource
    :type body: dict | bytes

    """
    body = TransportFreeMobilePost.from_dict(body)
    return web.Response(status=200)
