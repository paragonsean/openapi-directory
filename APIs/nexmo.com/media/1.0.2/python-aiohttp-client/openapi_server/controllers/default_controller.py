from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_and_search_media_items200_response import ListAndSearchMediaItems200Response
from openapi_server.models.media import Media
from openapi_server import util


async def delete_a_media_item(request: web.Request, ) -> web.Response:
    """Delete a media item

    Delete a previously created media item by ID.


    """
    return web.Response(status=200)


async def list_and_search_media_items(request: web.Request, order=None, page_index=None, page_size=None, start_time=None, end_time=None) -> web.Response:
    """List and search media items

    Retrieve information about multiple media items with the ability to search and paginate.

    :param order: The order of search results.
    :type order: str
    :param page_index: Which page to retrieve in pagination
    :type page_index: int
    :param page_size: How many items at most per page
    :type page_size: int
    :param start_time: Retrieve results created on or after this timestap.
    :type start_time: str
    :param end_time: Retrieve results created on or before this timestamp.
    :type end_time: str

    """
    return web.Response(status=200)


async def retrieve_a_media_item(request: web.Request, ) -> web.Response:
    """Retrieve a media item

    Retrieve information about a single media item


    """
    return web.Response(status=200)


async def update_a_media_item(request: web.Request, description=None, max_downloads_allowed=None, metadata_primary=None, metadata_secondary=None, mime_type=None, public=None, title=None) -> web.Response:
    """Update a media item

    Update a previously created media item by ID.

    :param description: A description of the media file.
    :type description: str
    :param max_downloads_allowed: The maximum number of times the file may be downloaded. Unlimited when not provided.
    :type max_downloads_allowed: int
    :param metadata_primary: A string containing metadata about the media file.
    :type metadata_primary: str
    :param metadata_secondary: A string containing further metadata about the media file.
    :type metadata_secondary: str
    :param mime_type: The MIME type of the media file.
    :type mime_type: str
    :param public: Whether the item is publicly available without authentication.
    :type public: bool
    :param title: A string containing a title for the media file.
    :type title: str

    """
    return web.Response(status=200)
