from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_transport_pager_tree_get_collection200_response import ApiTransportPagerTreeGetCollection200Response
from openapi_server.models.transport_pager_tree_get import TransportPagerTreeGet
from openapi_server.models.transport_pager_tree_jsonld_get import TransportPagerTreeJsonldGet
from openapi_server.models.transport_pager_tree_jsonld_post import TransportPagerTreeJsonldPost
from openapi_server.models.transport_pager_tree_jsonld_put import TransportPagerTreeJsonldPut
from openapi_server.models.transport_pager_tree_patch import TransportPagerTreePatch
from openapi_server.models.transport_pager_tree_post import TransportPagerTreePost
from openapi_server.models.transport_pager_tree_put import TransportPagerTreePut
from openapi_server import util


async def api_transport_pager_tree_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of TransportPagerTree resources.

    Retrieves the collection of TransportPagerTree resources.

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


async def api_transport_pager_tree_id_delete(request: web.Request, id) -> web.Response:
    """Removes the TransportPagerTree resource.

    Removes the TransportPagerTree resource.

    :param id: TransportPagerTree identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_pager_tree_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TransportPagerTree resource.

    Retrieves a TransportPagerTree resource.

    :param id: TransportPagerTree identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_pager_tree_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the TransportPagerTree resource.

    Updates the TransportPagerTree resource.

    :param id: TransportPagerTree identifier
    :type id: str
    :param body: The updated TransportPagerTree resource
    :type body: dict | bytes

    """
    body = TransportPagerTreePatch.from_dict(body)
    return web.Response(status=200)


async def api_transport_pager_tree_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the TransportPagerTree resource.

    Replaces the TransportPagerTree resource.

    :param id: TransportPagerTree identifier
    :type id: str
    :param body: The updated TransportPagerTree resource
    :type body: dict | bytes

    """
    body = TransportPagerTreePut.from_dict(body)
    return web.Response(status=200)


async def api_transport_pager_tree_post(request: web.Request, body) -> web.Response:
    """Creates a TransportPagerTree resource.

    Creates a TransportPagerTree resource.

    :param body: The new TransportPagerTree resource
    :type body: dict | bytes

    """
    body = TransportPagerTreePost.from_dict(body)
    return web.Response(status=200)
