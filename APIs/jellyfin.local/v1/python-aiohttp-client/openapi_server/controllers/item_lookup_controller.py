from typing import List, Dict
from aiohttp import web

from openapi_server.models.album_info_remote_search_query import AlbumInfoRemoteSearchQuery
from openapi_server.models.artist_info_remote_search_query import ArtistInfoRemoteSearchQuery
from openapi_server.models.book_info_remote_search_query import BookInfoRemoteSearchQuery
from openapi_server.models.box_set_info_remote_search_query import BoxSetInfoRemoteSearchQuery
from openapi_server.models.external_id_info import ExternalIdInfo
from openapi_server.models.movie_info_remote_search_query import MovieInfoRemoteSearchQuery
from openapi_server.models.music_video_info_remote_search_query import MusicVideoInfoRemoteSearchQuery
from openapi_server.models.person_lookup_info_remote_search_query import PersonLookupInfoRemoteSearchQuery
from openapi_server.models.problem_details import ProblemDetails
from openapi_server.models.remote_search_result import RemoteSearchResult
from openapi_server.models.series_info_remote_search_query import SeriesInfoRemoteSearchQuery
from openapi_server.models.trailer_info_remote_search_query import TrailerInfoRemoteSearchQuery
from openapi_server import util


async def apply_search_criteria(request: web.Request, item_id, body, replace_all_images=None) -> web.Response:
    """Applies search criteria to an item and refreshes metadata.

    

    :param item_id: Item id.
    :type item_id: str
    :type item_id: str
    :param body: The remote search result.
    :type body: dict | bytes
    :param replace_all_images: Optional. Whether or not to replace all images. Default: True.
    :type replace_all_images: bool

    """
    body = RemoteSearchResult.from_dict(body)
    return web.Response(status=200)


async def get_book_remote_search_results(request: web.Request, body) -> web.Response:
    """Get book remote search.

    

    :param body: Remote search query.
    :type body: dict | bytes

    """
    body = BookInfoRemoteSearchQuery.from_dict(body)
    return web.Response(status=200)


async def get_box_set_remote_search_results(request: web.Request, body) -> web.Response:
    """Get box set remote search.

    

    :param body: Remote search query.
    :type body: dict | bytes

    """
    body = BoxSetInfoRemoteSearchQuery.from_dict(body)
    return web.Response(status=200)


async def get_external_id_infos(request: web.Request, item_id) -> web.Response:
    """Get the item&#39;s external id info.

    

    :param item_id: Item id.
    :type item_id: str
    :type item_id: str

    """
    return web.Response(status=200)


async def get_movie_remote_search_results(request: web.Request, body) -> web.Response:
    """Get movie remote search.

    

    :param body: Remote search query.
    :type body: dict | bytes

    """
    body = MovieInfoRemoteSearchQuery.from_dict(body)
    return web.Response(status=200)


async def get_music_album_remote_search_results(request: web.Request, body) -> web.Response:
    """Get music album remote search.

    

    :param body: Remote search query.
    :type body: dict | bytes

    """
    body = AlbumInfoRemoteSearchQuery.from_dict(body)
    return web.Response(status=200)


async def get_music_artist_remote_search_results(request: web.Request, body) -> web.Response:
    """Get music artist remote search.

    

    :param body: Remote search query.
    :type body: dict | bytes

    """
    body = ArtistInfoRemoteSearchQuery.from_dict(body)
    return web.Response(status=200)


async def get_music_video_remote_search_results(request: web.Request, body) -> web.Response:
    """Get music video remote search.

    

    :param body: Remote search query.
    :type body: dict | bytes

    """
    body = MusicVideoInfoRemoteSearchQuery.from_dict(body)
    return web.Response(status=200)


async def get_person_remote_search_results(request: web.Request, body) -> web.Response:
    """Get person remote search.

    

    :param body: Remote search query.
    :type body: dict | bytes

    """
    body = PersonLookupInfoRemoteSearchQuery.from_dict(body)
    return web.Response(status=200)


async def get_remote_search_image(request: web.Request, image_url, provider_name) -> web.Response:
    """Gets a remote image.

    

    :param image_url: The image url.
    :type image_url: str
    :param provider_name: The provider name.
    :type provider_name: str

    """
    return web.Response(status=200)


async def get_series_remote_search_results(request: web.Request, body) -> web.Response:
    """Get series remote search.

    

    :param body: Remote search query.
    :type body: dict | bytes

    """
    body = SeriesInfoRemoteSearchQuery.from_dict(body)
    return web.Response(status=200)


async def get_trailer_remote_search_results(request: web.Request, body) -> web.Response:
    """Get trailer remote search.

    

    :param body: Remote search query.
    :type body: dict | bytes

    """
    body = TrailerInfoRemoteSearchQuery.from_dict(body)
    return web.Response(status=200)
