from typing import List, Dict
from aiohttp import web

from openapi_server.models.follow_artists_users_request import FollowArtistsUsersRequest
from openapi_server.models.follow_playlist_request import FollowPlaylistRequest
from openapi_server.models.get_followed200_response import GetFollowed200Response
from openapi_server.models.get_multiple_albums401_response import GetMultipleAlbums401Response
from openapi_server.models.paging_artist_object import PagingArtistObject
from openapi_server.models.paging_playlist_object import PagingPlaylistObject
from openapi_server.models.paging_track_object import PagingTrackObject
from openapi_server.models.private_user_object import PrivateUserObject
from openapi_server.models.public_user_object import PublicUserObject
from openapi_server.models.unfollow_artists_users_request import UnfollowArtistsUsersRequest
from openapi_server import util


async def check_current_user_follows(request: web.Request, type, ids) -> web.Response:
    """Check If User Follows Artists or Users 

    Check to see if the current user is following one or more artists or other Spotify users. 

    :param type: 
    :type type: str
    :param ids: 
    :type ids: str

    """
    return web.Response(status=200)


async def check_if_user_follows_playlist(request: web.Request, playlist_id, ids) -> web.Response:
    """Check if Users Follow Playlist 

    Check to see if one or more Spotify users are following a specified playlist. 

    :param playlist_id: 
    :type playlist_id: str
    :param ids: 
    :type ids: str

    """
    return web.Response(status=200)


async def follow_artists_users(request: web.Request, type, ids, body=None) -> web.Response:
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


async def follow_playlist(request: web.Request, playlist_id, body=None) -> web.Response:
    """Follow Playlist 

    Add the current user as a follower of a playlist. 

    :param playlist_id: 
    :type playlist_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = FollowPlaylistRequest.from_dict(body)
    return web.Response(status=200)


async def get_current_users_profile(request: web.Request, ) -> web.Response:
    """Get Current User&#39;s Profile 

    Get detailed profile information about the current user (including the current user&#39;s username). 


    """
    return web.Response(status=200)


async def get_followed(request: web.Request, type, after=None, limit=None) -> web.Response:
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


async def get_list_users_playlists_0(request: web.Request, user_id, limit=None, offset=None) -> web.Response:
    """Get User&#39;s Playlists 

    Get a list of the playlists owned or followed by a Spotify user. 

    :param user_id: 
    :type user_id: str
    :param limit: 
    :type limit: int
    :param offset: 
    :type offset: int

    """
    return web.Response(status=200)


async def get_users_profile(request: web.Request, user_id) -> web.Response:
    """Get User&#39;s Profile 

    Get public profile information about a Spotify user. 

    :param user_id: 
    :type user_id: str

    """
    return web.Response(status=200)


async def get_users_top_artists(request: web.Request, time_range=None, limit=None, offset=None) -> web.Response:
    """Get User&#39;s Top Artists 

    Get the current user&#39;s top artists based on calculated affinity. 

    :param time_range: 
    :type time_range: str
    :param limit: 
    :type limit: int
    :param offset: 
    :type offset: int

    """
    return web.Response(status=200)


async def get_users_top_tracks(request: web.Request, time_range=None, limit=None, offset=None) -> web.Response:
    """Get User&#39;s Top Tracks 

    Get the current user&#39;s top tracks based on calculated affinity. 

    :param time_range: 
    :type time_range: str
    :param limit: 
    :type limit: int
    :param offset: 
    :type offset: int

    """
    return web.Response(status=200)


async def unfollow_artists_users(request: web.Request, type, ids, body=None) -> web.Response:
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


async def unfollow_playlist(request: web.Request, playlist_id) -> web.Response:
    """Unfollow Playlist 

    Remove the current user as a follower of a playlist. 

    :param playlist_id: 
    :type playlist_id: str

    """
    return web.Response(status=200)
