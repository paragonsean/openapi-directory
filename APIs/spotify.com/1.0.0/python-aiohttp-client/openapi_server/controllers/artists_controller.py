from typing import List, Dict
from aiohttp import web

from openapi_server.models.artist_object import ArtistObject
from openapi_server.models.follow_artists_users_request import FollowArtistsUsersRequest
from openapi_server.models.get_an_artists_top_tracks200_response import GetAnArtistsTopTracks200Response
from openapi_server.models.get_followed200_response import GetFollowed200Response
from openapi_server.models.get_multiple_albums401_response import GetMultipleAlbums401Response
from openapi_server.models.get_multiple_artists200_response import GetMultipleArtists200Response
from openapi_server.models.paging_simplified_album_object import PagingSimplifiedAlbumObject
from openapi_server.models.unfollow_artists_users_request import UnfollowArtistsUsersRequest
from openapi_server import util


async def check_current_user_follows_0(request: web.Request, type, ids) -> web.Response:
    """Check If User Follows Artists or Users 

    Check to see if the current user is following one or more artists or other Spotify users. 

    :param type: 
    :type type: str
    :param ids: 
    :type ids: str

    """
    return web.Response(status=200)


async def follow_artists_users_0(request: web.Request, type, ids, body=None) -> web.Response:
    """Follow Artists or Users 

    Add the current user as a follower of one or more artists or other Spotify users. 

    :param type: 
    :type type: str
    :param ids: 
    :type ids: str
    :param body: 
    :type body: dict | bytes

    """
    body = FollowArtistsUsersRequest.from_dict(body)
    return web.Response(status=200)


async def get_an_artist(request: web.Request, id) -> web.Response:
    """Get Artist 

    Get Spotify catalog information for a single artist identified by their unique Spotify ID. 

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_an_artists_albums(request: web.Request, id, include_groups=None, market=None, limit=None, offset=None) -> web.Response:
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


async def get_an_artists_related_artists(request: web.Request, id) -> web.Response:
    """Get Artist&#39;s Related Artists 

    Get Spotify catalog information about artists similar to a given artist. Similarity is based on analysis of the Spotify community&#39;s [listening history](http://news.spotify.com/se/2010/02/03/related-artists/). 

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_an_artists_top_tracks(request: web.Request, id, market=None) -> web.Response:
    """Get Artist&#39;s Top Tracks 

    Get Spotify catalog information about an artist&#39;s top tracks by country. 

    :param id: 
    :type id: str
    :param market: 
    :type market: str

    """
    return web.Response(status=200)


async def get_followed_1(request: web.Request, type, after=None, limit=None) -> web.Response:
    """Get Followed Artists 

    Get the current user&#39;s followed artists. 

    :param type: 
    :type type: str
    :param after: 
    :type after: str
    :param limit: 
    :type limit: int

    """
    return web.Response(status=200)


async def get_multiple_artists(request: web.Request, ids) -> web.Response:
    """Get Several Artists 

    Get Spotify catalog information for several artists based on their Spotify IDs. 

    :param ids: 
    :type ids: str

    """
    return web.Response(status=200)


async def unfollow_artists_users_0(request: web.Request, type, ids, body=None) -> web.Response:
    """Unfollow Artists or Users 

    Remove the current user as a follower of one or more artists or other Spotify users. 

    :param type: 
    :type type: str
    :param ids: 
    :type ids: str
    :param body: 
    :type body: dict | bytes

    """
    body = UnfollowArtistsUsersRequest.from_dict(body)
    return web.Response(status=200)
