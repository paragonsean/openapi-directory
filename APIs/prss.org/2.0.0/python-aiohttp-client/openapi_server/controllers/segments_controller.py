from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.segment import Segment
from openapi_server import util


async def api_v2_segments_get(request: web.Request, episode_id, segment_number=None, page_start=None, page_size=None, order_by_id=None) -> web.Response:
    """Returns the segments matching the query parameters.

    

    :param episode_id: The ID of the episode that owns the segment.
    :type episode_id: int
    :param segment_number: 
    :type segment_number: int
    :param page_start: The start page of the results to return. The first item is indexed at 0.
    :type page_start: int
    :param page_size: The number of items to return. Must be between 0 and 500, inclusive.
    :type page_size: int
    :param order_by_id: The sort order of the list of segments, based on segment ID. If unspecified, the segments are returned in random order. If using paging to iterate through the results, sort order should be specified.
    :type order_by_id: str

    """
    return web.Response(status=200)


async def api_v2_segments_id_content_get(request: web.Request, id) -> web.Response:
    """UNDER DEVELOPMENT - Returns the audio content segment matching the given ID.

    

    :param id: 
    :type id: int

    """
    return web.Response(status=200)


async def api_v2_segments_id_delete(request: web.Request, id) -> web.Response:
    """Deletes the segment with the given ID.

    

    :param id: 
    :type id: int

    """
    return web.Response(status=200)


async def api_v2_segments_id_get(request: web.Request, id) -> web.Response:
    """Returns the segment matching the given ID.

    

    :param id: 
    :type id: int

    """
    return web.Response(status=200)


async def api_v2_segments_post(request: web.Request, cd_drive_uri, episode_id, segment_number, in_cue=None, out_cue=None) -> web.Response:
    """Creates a new segment.

    

    :param cd_drive_uri: The URI to the segment content in CD Drive. Format should be &#39;cddrive:id:{value}&#39; or &#39;cddrive://{path}&#39;.
    :type cd_drive_uri: str
    :param episode_id: The ID of the episode that owns the segment.
    :type episode_id: int
    :param segment_number: The segment number of the segment.
    :type segment_number: int
    :param in_cue: The incue for the segment. Defaults to the program segment incue.
    :type in_cue: str
    :param out_cue: The outcue for the segment. Defaults to the program segment outcue.
    :type out_cue: str

    """
    return web.Response(status=200)
