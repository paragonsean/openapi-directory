from typing import List, Dict
from aiohttp import web

from openapi_server.models.album import Album
from openapi_server.models.error import Error
from openapi_server.models.legacy_error import LegacyError
from openapi_server.models.replace_videos_in_album_alt1_request import ReplaceVideosInAlbumAlt1Request
from openapi_server.models.set_video_as_album_thumbnail_alt1_request import SetVideoAsAlbumThumbnailAlt1Request
from openapi_server.models.video import Video
from openapi_server import util


async def add_video_to_album(request: web.Request, album_id, user_id, video_id) -> web.Response:
    """Add a specific video to an album

    

    :param album_id: The ID of the album.
    :type album_id: 
    :param user_id: The ID of the user.
    :type user_id: 
    :param video_id: The ID of the video.
    :type video_id: 

    """
    return web.Response(status=200)


async def add_video_to_album_alt1(request: web.Request, album_id, video_id) -> web.Response:
    """Add a specific video to an album

    

    :param album_id: The ID of the album.
    :type album_id: 
    :param video_id: The ID of the video.
    :type video_id: 

    """
    return web.Response(status=200)


async def get_album_video(request: web.Request, album_id, user_id, video_id, password=None) -> web.Response:
    """Get a specific video in an album

    This method gets a single video from an album. You can use this method to determine whether the album contains the specified video.

    :param album_id: The ID of the album.
    :type album_id: 
    :param user_id: The ID of the user.
    :type user_id: 
    :param video_id: The ID of the video.
    :type video_id: 
    :param password: The password of the album.
    :type password: str

    """
    return web.Response(status=200)


async def get_album_video_alt1(request: web.Request, album_id, video_id, password=None) -> web.Response:
    """Get a specific video in an album

    This method gets a single video from an album. You can use this method to determine whether the album contains the specified video.

    :param album_id: The ID of the album.
    :type album_id: 
    :param video_id: The ID of the video.
    :type video_id: 
    :param password: The password of the album.
    :type password: str

    """
    return web.Response(status=200)


async def get_album_videos(request: web.Request, album_id, user_id, containing_uri=None, direction=None, filter=None, filter_embeddable=None, page=None, password=None, per_page=None, query=None, sort=None, weak_search=None) -> web.Response:
    """Get all the videos in an album

    

    :param album_id: The ID of the album.
    :type album_id: 
    :param user_id: The ID of the user.
    :type user_id: 
    :param containing_uri: The page containing the video URI.
    :type containing_uri: str
    :param direction: The sort direction of the results.
    :type direction: str
    :param filter: The attribute by which to filter the results.
    :type filter: str
    :param filter_embeddable: Whether to filter the results by embeddable videos (&#x60;true&#x60;) or non-embeddable videos (&#x60;false&#x60;). Required only if **filter** is &#x60;embeddable&#x60;.
    :type filter_embeddable: bool
    :param page: The page number of the results to show.
    :type page: 
    :param password: The password of the album.
    :type password: str
    :param per_page: The number of items to show on each page of results, up to a maximum of 100.
    :type per_page: 
    :param query: The search query to use to filter the results.
    :type query: str
    :param sort: The way to sort the results.
    :type sort: str
    :param weak_search: Whether to include private videos in the search. Please note that a separate search service provides this functionality. The service performs a partial text search on the video&#39;s name.
    :type weak_search: bool

    """
    return web.Response(status=200)


async def get_album_videos_alt1(request: web.Request, album_id, containing_uri=None, direction=None, filter=None, filter_embeddable=None, page=None, password=None, per_page=None, query=None, sort=None, weak_search=None) -> web.Response:
    """Get all the videos in an album

    

    :param album_id: The ID of the album.
    :type album_id: 
    :param containing_uri: The page containing the video URI.
    :type containing_uri: str
    :param direction: The sort direction of the results.
    :type direction: str
    :param filter: The attribute by which to filter the results.
    :type filter: str
    :param filter_embeddable: Whether to filter the results by embeddable videos (&#x60;true&#x60;) or non-embeddable videos (&#x60;false&#x60;). Required only if **filter** is &#x60;embeddable&#x60;.
    :type filter_embeddable: bool
    :param page: The page number of the results to show.
    :type page: 
    :param password: The password of the album.
    :type password: str
    :param per_page: The number of items to show on each page of results, up to a maximum of 100.
    :type per_page: 
    :param query: The search query to use to filter the results.
    :type query: str
    :param sort: The way to sort the results.
    :type sort: str
    :param weak_search: Whether to include private videos in the search. Please note that a separate search service provides this functionality. The service performs a partial text search on the video&#39;s name.
    :type weak_search: bool

    """
    return web.Response(status=200)


async def remove_video_from_album(request: web.Request, album_id, user_id, video_id) -> web.Response:
    """Remove a video from an album

    

    :param album_id: The ID of the album.
    :type album_id: 
    :param user_id: The ID of the user.
    :type user_id: 
    :param video_id: The ID of the video.
    :type video_id: 

    """
    return web.Response(status=200)


async def remove_video_from_album_alt1(request: web.Request, album_id, video_id) -> web.Response:
    """Remove a video from an album

    

    :param album_id: The ID of the album.
    :type album_id: 
    :param video_id: The ID of the video.
    :type video_id: 

    """
    return web.Response(status=200)


async def replace_videos_in_album(request: web.Request, album_id, user_id, body) -> web.Response:
    """Replace all the videos in an album

    This method replaces all the existing videos in an album with one or more videos.

    :param album_id: The ID of the album.
    :type album_id: 
    :param user_id: The ID of the user.
    :type user_id: 
    :param body: 
    :type body: dict | bytes

    """
    body = ReplaceVideosInAlbumAlt1Request.from_dict(body)
    return web.Response(status=200)


async def replace_videos_in_album_alt1(request: web.Request, album_id, body) -> web.Response:
    """Replace all the videos in an album

    This method replaces all the existing videos in an album with one or more videos.

    :param album_id: The ID of the album.
    :type album_id: 
    :param body: 
    :type body: dict | bytes

    """
    body = ReplaceVideosInAlbumAlt1Request.from_dict(body)
    return web.Response(status=200)


async def set_video_as_album_thumbnail(request: web.Request, album_id, user_id, video_id, body=None) -> web.Response:
    """Set a video as the album thumbnail

    

    :param album_id: The ID of the album.
    :type album_id: 
    :param user_id: The ID of the user.
    :type user_id: 
    :param video_id: The ID of the video.
    :type video_id: 
    :param body: 
    :type body: dict | bytes

    """
    body = SetVideoAsAlbumThumbnailAlt1Request.from_dict(body)
    return web.Response(status=200)


async def set_video_as_album_thumbnail_alt1(request: web.Request, album_id, video_id, body=None) -> web.Response:
    """Set a video as the album thumbnail

    

    :param album_id: The ID of the album.
    :type album_id: 
    :param video_id: The ID of the video.
    :type video_id: 
    :param body: 
    :type body: dict | bytes

    """
    body = SetVideoAsAlbumThumbnailAlt1Request.from_dict(body)
    return web.Response(status=200)
