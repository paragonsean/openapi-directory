from typing import List, Dict
from aiohttp import web

from openapi_server.models.edit_video_request import EditVideoRequest
from openapi_server.models.error import Error
from openapi_server.models.legacy_error import LegacyError
from openapi_server.models.video import Video
from openapi_server import util


async def check_if_user_owns_video(request: web.Request, user_id, video_id) -> web.Response:
    """Check if a user owns a video

    

    :param user_id: The ID of the user.
    :type user_id: 
    :param video_id: The ID of the video.
    :type video_id: 

    """
    return web.Response(status=200)


async def check_if_user_owns_video_alt1(request: web.Request, video_id) -> web.Response:
    """Check if a user owns a video

    

    :param video_id: The ID of the video.
    :type video_id: 

    """
    return web.Response(status=200)


async def delete_video(request: web.Request, video_id) -> web.Response:
    """Delete a video

    

    :param video_id: The ID of the video.
    :type video_id: 

    """
    return web.Response(status=200)


async def edit_video(request: web.Request, video_id, body) -> web.Response:
    """Edit a video

    

    :param video_id: The ID of the video.
    :type video_id: 
    :param body: 
    :type body: dict | bytes

    """
    body = EditVideoRequest.from_dict(body)
    return web.Response(status=200)


async def get_appearances(request: web.Request, user_id, direction=None, filter=None, filter_embeddable=None, page=None, per_page=None, query=None, sort=None) -> web.Response:
    """Get all the videos in which a user appears

    

    :param user_id: The ID of the user.
    :type user_id: 
    :param direction: The sort direction of the results.
    :type direction: str
    :param filter: The attribute by which to filter the results.
    :type filter: str
    :param filter_embeddable: Whether to filter the results by embeddable videos (&#x60;true&#x60;) or non-embeddable videos (&#x60;false&#x60;). Required only if **filter** is &#x60;embeddable&#x60;.
    :type filter_embeddable: bool
    :param page: The page number of the results to show.
    :type page: 
    :param per_page: The number of items to show on each page of results, up to a maximum of 100.
    :type per_page: 
    :param query: The search query to use to filter the results.
    :type query: str
    :param sort: The way to sort the results.
    :type sort: str

    """
    return web.Response(status=200)


async def get_appearances_alt1(request: web.Request, direction=None, filter=None, filter_embeddable=None, page=None, per_page=None, query=None, sort=None) -> web.Response:
    """Get all the videos in which a user appears

    

    :param direction: The sort direction of the results.
    :type direction: str
    :param filter: The attribute by which to filter the results.
    :type filter: str
    :param filter_embeddable: Whether to filter the results by embeddable videos (&#x60;true&#x60;) or non-embeddable videos (&#x60;false&#x60;). Required only if **filter** is &#x60;embeddable&#x60;.
    :type filter_embeddable: bool
    :param page: The page number of the results to show.
    :type page: 
    :param per_page: The number of items to show on each page of results, up to a maximum of 100.
    :type per_page: 
    :param query: The search query to use to filter the results.
    :type query: str
    :param sort: The way to sort the results.
    :type sort: str

    """
    return web.Response(status=200)


async def get_video(request: web.Request, video_id) -> web.Response:
    """Get a specific video

    

    :param video_id: The ID of the video.
    :type video_id: 

    """
    return web.Response(status=200)


async def get_videos(request: web.Request, user_id, containing_uri=None, direction=None, filter=None, filter_embeddable=None, filter_playable=None, page=None, per_page=None, query=None, sort=None) -> web.Response:
    """Get all the videos that a user has uploaded

    

    :param user_id: The ID of the user.
    :type user_id: 
    :param containing_uri: The page that contains the video URI. Only available when not paired with &#x60;query&#x60;.
    :type containing_uri: str
    :param direction: The sort direction of the results.
    :type direction: str
    :param filter: The attribute by which to filter the results.
    :type filter: str
    :param filter_embeddable: Whether to filter the results by embeddable videos (&#x60;true&#x60;) or non-embeddable videos (&#x60;false&#x60;). Required only if **filter** is &#x60;embeddable&#x60;.
    :type filter_embeddable: bool
    :param filter_playable: Whether to filter by all playable videos or by all videos that are not  playable.
    :type filter_playable: bool
    :param page: The page number of the results to show.
    :type page: 
    :param per_page: The number of items to show on each page of results, up to a maximum of 100.
    :type per_page: 
    :param query: The search query to use to filter the results.
    :type query: str
    :param sort: The way to sort the results.
    :type sort: str

    """
    return web.Response(status=200)


async def get_videos_alt1(request: web.Request, containing_uri=None, direction=None, filter=None, filter_embeddable=None, filter_playable=None, page=None, per_page=None, query=None, sort=None) -> web.Response:
    """Get all the videos that a user has uploaded

    

    :param containing_uri: The page that contains the video URI. Only available when not paired with &#x60;query&#x60;.
    :type containing_uri: str
    :param direction: The sort direction of the results.
    :type direction: str
    :param filter: The attribute by which to filter the results.
    :type filter: str
    :param filter_embeddable: Whether to filter the results by embeddable videos (&#x60;true&#x60;) or non-embeddable videos (&#x60;false&#x60;). Required only if **filter** is &#x60;embeddable&#x60;.
    :type filter_embeddable: bool
    :param filter_playable: Whether to filter by all playable videos or by all videos that are not  playable.
    :type filter_playable: bool
    :param page: The page number of the results to show.
    :type page: 
    :param per_page: The number of items to show on each page of results, up to a maximum of 100.
    :type per_page: 
    :param query: The search query to use to filter the results.
    :type query: str
    :param sort: The way to sort the results.
    :type sort: str

    """
    return web.Response(status=200)


async def search_videos(request: web.Request, query, direction=None, filter=None, links=None, page=None, per_page=None, sort=None, uris=None) -> web.Response:
    """Search for videos

    

    :param query: Search query.
    :type query: str
    :param direction: The sort direction of the results.
    :type direction: str
    :param filter: The attribute by which to filter the results. &#x60;CC&#x60; and related filters target videos with the corresponding Creative Commons licenses. For more information, see our [Creative Commons](https://vimeo.com/creativecommons) page.
    :type filter: str
    :param links: A comma-separated list of video URLs to find.
    :type links: str
    :param page: The page number of the results to show.
    :type page: 
    :param per_page: The number of items to show on each page of results, up to a maximum of 100.
    :type per_page: 
    :param sort: The way to sort the results.
    :type sort: str
    :param uris: The comma-separated list of videos to find.
    :type uris: str

    """
    return web.Response(status=200)
