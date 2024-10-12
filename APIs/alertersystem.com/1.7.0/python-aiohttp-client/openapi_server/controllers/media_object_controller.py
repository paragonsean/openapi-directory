from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_media_object_get_collection200_response import ApiMediaObjectGetCollection200Response
from openapi_server.models.media_object_get import MediaObjectGet
from openapi_server.models.media_object_jsonld_get import MediaObjectJsonldGet
from openapi_server import util


async def api_media_object_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of MediaObject resources.

    Retrieves the collection of MediaObject resources.

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


async def api_media_object_id_delete(request: web.Request, id) -> web.Response:
    """Removes the MediaObject resource.

    Removes the MediaObject resource.

    :param id: MediaObject identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_media_object_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a MediaObject resource.

    Retrieves a MediaObject resource.

    :param id: MediaObject identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_media_object_post(request: web.Request, data_segment_code=None, file=None, keywords=None, partition=None) -> web.Response:
    """Creates a MediaObject resource.

    Creates a MediaObject resource.

    :param data_segment_code: User-provided string on which to segment and filter data. Max 50 characters.
    :type data_segment_code: str
    :param file: 
    :type file: str
    :param keywords: A string of keywords that can be used to search for a resource. Max 100 characters.
    :type keywords: str
    :param partition: The unique id of the partition. Can be just the id or an IRI.
    :type partition: str

    """
    return web.Response(status=200)
