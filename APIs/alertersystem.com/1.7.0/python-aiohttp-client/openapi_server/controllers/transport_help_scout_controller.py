from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_transport_help_scout_get_collection200_response import ApiTransportHelpScoutGetCollection200Response
from openapi_server.models.transport_help_scout_get import TransportHelpScoutGet
from openapi_server.models.transport_help_scout_jsonld_get import TransportHelpScoutJsonldGet
from openapi_server.models.transport_help_scout_jsonld_post import TransportHelpScoutJsonldPost
from openapi_server.models.transport_help_scout_jsonld_put import TransportHelpScoutJsonldPut
from openapi_server.models.transport_help_scout_patch import TransportHelpScoutPatch
from openapi_server.models.transport_help_scout_post import TransportHelpScoutPost
from openapi_server.models.transport_help_scout_put import TransportHelpScoutPut
from openapi_server import util


async def api_transport_help_scout_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of TransportHelpScout resources.

    Retrieves the collection of TransportHelpScout resources.

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


async def api_transport_help_scout_id_delete(request: web.Request, id) -> web.Response:
    """Removes the TransportHelpScout resource.

    Removes the TransportHelpScout resource.

    :param id: TransportHelpScout identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_help_scout_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TransportHelpScout resource.

    Retrieves a TransportHelpScout resource.

    :param id: TransportHelpScout identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_help_scout_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the TransportHelpScout resource.

    Updates the TransportHelpScout resource.

    :param id: TransportHelpScout identifier
    :type id: str
    :param body: The updated TransportHelpScout resource
    :type body: dict | bytes

    """
    body = TransportHelpScoutPatch.from_dict(body)
    return web.Response(status=200)


async def api_transport_help_scout_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the TransportHelpScout resource.

    Replaces the TransportHelpScout resource.

    :param id: TransportHelpScout identifier
    :type id: str
    :param body: The updated TransportHelpScout resource
    :type body: dict | bytes

    """
    body = TransportHelpScoutPut.from_dict(body)
    return web.Response(status=200)


async def api_transport_help_scout_post(request: web.Request, body) -> web.Response:
    """Creates a TransportHelpScout resource.

    Creates a TransportHelpScout resource.

    :param body: The new TransportHelpScout resource
    :type body: dict | bytes

    """
    body = TransportHelpScoutPost.from_dict(body)
    return web.Response(status=200)
