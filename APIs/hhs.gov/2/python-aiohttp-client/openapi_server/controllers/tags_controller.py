from typing import List, Dict
from aiohttp import web

from openapi_server.models.media_item_wrapped import MediaItemWrapped
from openapi_server.models.tag_language_marshaller_wrapped import TagLanguageMarshallerWrapped
from openapi_server.models.tag_marshaller_wrapped import TagMarshallerWrapped
from openapi_server.models.tag_type_marshaller_wrapped import TagTypeMarshallerWrapped
from openapi_server import util


async def resources_tags_format_get(request: web.Request, format, sort=None, max=None, offset=None, name=None, name_contains=None, media_id=None, type_id=None, type_name=None) -> web.Response:
    """Get Tags

    List of Tags

    :param format: Automatically added
    :type format: str
    :param sort: The name of the property to which sorting will be applied
    :type sort: str
    :param max: The maximum number of records to return
    :type max: int
    :param offset: Return records starting at the offset index.
    :type offset: int
    :param name: Return tags[s] matching the supplied name
    :type name: str
    :param name_contains: Return tags which contain the supplied partial name.
    :type name_contains: str
    :param media_id: Return tags associated with the supplied media id.
    :type media_id: int
    :param type_id: Return tags belonging to the supplied tag type id.
    :type type_id: int
    :param type_name: Return tags belonging to the supplied tag type name.
    :type type_name: str

    """
    return web.Response(status=200)


async def resources_tags_id_format_get(request: web.Request, id, format) -> web.Response:
    """Get Tag by ID

    Information about a specific tag

    :param id: The id of the record to look up
    :type id: int
    :param format: Automatically added
    :type format: str

    """
    return web.Response(status=200)


async def resources_tags_id_media_format_get(request: web.Request, id, format, sort=None, max=None, offset=None) -> web.Response:
    """Get MediaItems for Tag

    MediaItem

    :param id: The id of the tag to look up
    :type id: int
    :param format: Automatically added
    :type format: str
    :param sort: The name of the property to which sorting will be applied
    :type sort: str
    :param max: The maximum number of records to return
    :type max: int
    :param offset: Return records starting at the offset index.
    :type offset: int

    """
    return web.Response(status=200)


async def resources_tags_id_related_format_get(request: web.Request, id, format, sort=None, max=None, offset=None) -> web.Response:
    """Get related Tags by ID

    Information about related tags to a specific tag

    :param id: The id of the tag to look up
    :type id: int
    :param format: Automatically added
    :type format: str
    :param sort: The name of the property to which sorting will be applied
    :type sort: str
    :param max: The maximum number of records to return
    :type max: int
    :param offset: Return records starting at the offset index.
    :type offset: int

    """
    return web.Response(status=200)


async def resources_tags_id_syndicate_format_get(request: web.Request, id, format, display_method=None) -> web.Response:
    """Get MediaItems for Tag

    MediaItem

    :param id: The id of the record to look up
    :type id: int
    :param format: Automatically added
    :type format: str
    :param display_method: Method used to render an html request. Accepts one: [mv, list, feed]
    :type display_method: str

    """
    return web.Response(status=200)


async def resources_tags_tag_languages_format_get(request: web.Request, format) -> web.Response:
    """Get TagLanguages

    List of Tag Languages

    :param format: Automatically added
    :type format: str

    """
    return web.Response(status=200)


async def resources_tags_tag_types_format_get(request: web.Request, format) -> web.Response:
    """Get MediaItems for Tag

    List of Types

    :param format: Automatically added
    :type format: str

    """
    return web.Response(status=200)
