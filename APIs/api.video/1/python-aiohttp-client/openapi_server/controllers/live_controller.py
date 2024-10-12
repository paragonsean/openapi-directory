from typing import List, Dict
from aiohttp import web

from openapi_server.models.bad_request import BadRequest
from openapi_server.models.live_stream import LiveStream
from openapi_server.models.live_stream_create_payload import LiveStreamCreatePayload
from openapi_server.models.live_stream_list_response import LiveStreamListResponse
from openapi_server.models.live_stream_update_payload import LiveStreamUpdatePayload
from openapi_server.models.not_found import NotFound
from openapi_server import util


async def d_elete_live_streams_live_stream_id(request: web.Request, live_stream_id) -> web.Response:
    """Delete a live stream

    

    :param live_stream_id: The unique ID for the live stream that you want to remove.
    :type live_stream_id: str

    """
    return web.Response(status=200)


async def d_elete_live_streams_live_stream_id_thumbnail(request: web.Request, live_stream_id) -> web.Response:
    """Delete a thumbnail

    Send the unique identifier for a live stream to delete it from the system.

    :param live_stream_id: The unique identifier for the live stream you want to delete. 
    :type live_stream_id: str

    """
    return web.Response(status=200)


async def g_et_live_streams(request: web.Request, stream_key=None, name=None, sort_by=None, sort_order=None, current_page=None, page_size=None) -> web.Response:
    """List all live streams

    With no parameters added to the url, this will return all livestreams. Query by name or key to limit the list.

    :param stream_key: The unique stream key that allows you to stream videos.
    :type stream_key: str
    :param name: You can filter live streams by their name or a part of their name.
    :type name: str
    :param sort_by: Allowed: createdAt, publishedAt, name. createdAt - the time a livestream was created using the specified streamKey. publishedAt - the time a livestream was published using the specified streamKey. name - the name of the livestream. If you choose one of the time based options, the time is presented in ISO-8601 format.
    :type sort_by: str
    :param sort_order: Allowed: asc, desc. Ascending for date and time means that earlier values precede later ones. Descending means that later values preced earlier ones. For title, it is 0-9 and A-Z ascending and Z-A, 9-0 descending.
    :type sort_order: str
    :param current_page: Choose the number of search results to return per page. Minimum value: 1
    :type current_page: int
    :param page_size: Results per page. Allowed values 1-100, default is 25.
    :type page_size: int

    """
    return web.Response(status=200)


async def g_et_live_streams_live_stream_id(request: web.Request, live_stream_id) -> web.Response:
    """Show live stream

    Supply a LivestreamId, and you&#39;ll get all the details for streaming into, and watching the livestream. Tutorials that use the [show livestream endpoint](https://api.video/blog/endpoints/live-stream-status).

    :param live_stream_id: The unique ID for the live stream you want to watch.
    :type live_stream_id: str

    """
    return web.Response(status=200)


async def p_atch_live_streams_live_stream_id(request: web.Request, live_stream_id, body=None) -> web.Response:
    """Update a live stream

    Use this endpoint to update the player, or to turn recording on/off (saving a copy of the livestream). NOTE: If the livestream is actively streaming, changing the recording status will only affect the NEXT stream.    The public&#x3D;false &#39;private livestream&#39; is available as a BETA feature, and should be limited to livestreams of 3,000 viewers or fewer.

    :param live_stream_id: The unique ID for the live stream that you want to update information for such as player details, or whether you want the recording on or off.
    :type live_stream_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = LiveStreamUpdatePayload.from_dict(body)
    return web.Response(status=200)


async def p_ost_live_streams(request: web.Request, body=None) -> web.Response:
    """Create live stream

    A live stream will give you the &#39;connection point&#39; to RTMP your video stream to api.video. It will also give you the details for viewers to watch the same livestream.  The public&#x3D;false &#39;private livestream&#39; is available as a BETA feature, and should be limited to livestreams of 3,000 viewers or fewer. See our [Live Stream Tutorial](https://api.video/blog/tutorials/live-stream-tutorial) for a walkthrough of this API with OBS. Your RTMP endpoint for the livestream is rtmp://broadcast.api.video/s/{streamKey} Tutorials that [create live streams](https://api.video/blog/endpoints/live-create).

    :param body: 
    :type body: dict | bytes

    """
    body = LiveStreamCreatePayload.from_dict(body)
    return web.Response(status=200)


async def p_ost_live_streams_live_stream_id_thumbnail(request: web.Request, live_stream_id, file) -> web.Response:
    """Upload a thumbnail

    Upload an image to use as a backdrop for your livestream. Tutorials that [update live stream thumbnails](https://api.video/blog/endpoints/live-upload-a-thumbnail).

    :param live_stream_id: The unique ID for the live stream you want to upload.
    :type live_stream_id: str
    :param file: The image to be added as a thumbnail.
    :type file: str

    """
    return web.Response(status=200)
