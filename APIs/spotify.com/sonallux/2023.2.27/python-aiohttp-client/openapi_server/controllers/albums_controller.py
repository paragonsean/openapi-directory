from typing import List, Dict
from aiohttp import web

from openapi_server.models.album_object import AlbumObject
from openapi_server.models.get_multiple_albums200_response import GetMultipleAlbums200Response
from openapi_server.models.get_multiple_albums401_response import GetMultipleAlbums401Response
from openapi_server.models.get_new_releases200_response import GetNewReleases200Response
from openapi_server.models.paging_saved_album_object import PagingSavedAlbumObject
from openapi_server.models.paging_simplified_album_object import PagingSimplifiedAlbumObject
from openapi_server.models.paging_simplified_track_object import PagingSimplifiedTrackObject
from openapi_server.models.save_albums_user_request import SaveAlbumsUserRequest
from openapi_server import util


async def check_users_saved_albums(request: web.Request, ids) -> web.Response:
    """Check User&#39;s Saved Albums 

    Check if one or more albums is already saved in the current Spotify user&#39;s &#39;Your Music&#39; library. 

    :param ids: 
    :type ids: str

    """
    return web.Response(status=200)


async def get_an_album(request: web.Request, id, market=None) -> web.Response:
    """Get Album 

    Get Spotify catalog information for a single album. 

    :param id: 
    :type id: str
    :param market: 
    :type market: str

    """
    return web.Response(status=200)


async def get_an_albums_tracks(request: web.Request, id, market=None, limit=None, offset=None) -> web.Response:
    """Get Album Tracks 

    Get Spotify catalog information about an album’s tracks. Optional parameters can be used to limit the number of tracks returned. 

    :param id: 
    :type id: str
    :param market: 
    :type market: str
    :param limit: 
    :type limit: int
    :param offset: 
    :type offset: int

    """
    return web.Response(status=200)


async def get_an_artists_albums_0(request: web.Request, id, include_groups=None, market=None, limit=None, offset=None) -> web.Response:
    """Get Artist&#39;s Albums 

    Get Spotify catalog information about an artist&#39;s albums. 

    :param id: 
    :type id: str
    :param include_groups: 
    :type include_groups: str
    :param market: 
    :type market: str
    :param limit: 
    :type limit: int
    :param offset: 
    :type offset: int

    """
    return web.Response(status=200)


async def get_multiple_albums(request: web.Request, ids, market=None) -> web.Response:
    """Get Several Albums 

    Get Spotify catalog information for multiple albums identified by their Spotify IDs. 

    :param ids: 
    :type ids: str
    :param market: 
    :type market: str

    """
    return web.Response(status=200)


async def get_new_releases(request: web.Request, country=None, limit=None, offset=None) -> web.Response:
    """Get New Releases 

    Get a list of new album releases featured in Spotify (shown, for example, on a Spotify player’s “Browse” tab). 

    :param country: 
    :type country: str
    :param limit: 
    :type limit: int
    :param offset: 
    :type offset: int

    """
    return web.Response(status=200)


async def get_users_saved_albums(request: web.Request, limit=None, offset=None, market=None) -> web.Response:
    """Get User&#39;s Saved Albums 

    Get a list of the albums saved in the current Spotify user&#39;s &#39;Your Music&#39; library. 

    :param limit: 
    :type limit: int
    :param offset: 
    :type offset: int
    :param market: 
    :type market: str

    """
    return web.Response(status=200)


async def remove_albums_user(request: web.Request, ids, body=None) -> web.Response:
    """Remove Users&#39; Saved Albums 

    Remove one or more albums from the current user&#39;s &#39;Your Music&#39; library. 

    :param ids: 
    :type ids: str
    :param body: 
    :type body: dict | bytes

    """
    body = SaveAlbumsUserRequest.from_dict(body)
    return web.Response(status=200)


async def save_albums_user(request: web.Request, ids, body=None) -> web.Response:
    """Save Albums for Current User 

    Save one or more albums to the current user&#39;s &#39;Your Music&#39; library. 

    :param ids: 
    :type ids: str
    :param body: 
    :type body: dict | bytes

    """
    body = SaveAlbumsUserRequest.from_dict(body)
    return web.Response(status=200)
