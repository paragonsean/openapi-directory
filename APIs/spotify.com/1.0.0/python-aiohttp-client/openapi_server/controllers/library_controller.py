from typing import List, Dict
from aiohttp import web

from openapi_server.models.change_playlist_details_request import ChangePlaylistDetailsRequest
from openapi_server.models.create_playlist_request import CreatePlaylistRequest
from openapi_server.models.follow_artists_users_request import FollowArtistsUsersRequest
from openapi_server.models.get_followed200_response import GetFollowed200Response
from openapi_server.models.get_multiple_albums401_response import GetMultipleAlbums401Response
from openapi_server.models.get_users_top_artists_and_tracks200_response import GetUsersTopArtistsAndTracks200Response
from openapi_server.models.paging_playlist_object import PagingPlaylistObject
from openapi_server.models.paging_saved_album_object import PagingSavedAlbumObject
from openapi_server.models.paging_saved_episode_object import PagingSavedEpisodeObject
from openapi_server.models.paging_saved_show_object import PagingSavedShowObject
from openapi_server.models.paging_saved_track_object import PagingSavedTrackObject
from openapi_server.models.paging_simplified_audiobook_object import PagingSimplifiedAudiobookObject
from openapi_server.models.playlist_object import PlaylistObject
from openapi_server.models.remove_episodes_user_request import RemoveEpisodesUserRequest
from openapi_server.models.save_albums_user_request import SaveAlbumsUserRequest
from openapi_server.models.save_episodes_user_request import SaveEpisodesUserRequest
from openapi_server.models.save_tracks_user_request import SaveTracksUserRequest
from openapi_server.models.unfollow_artists_users_request import UnfollowArtistsUsersRequest
from openapi_server import util


async def change_playlist_details_0(request: web.Request, playlist_id, body=None) -> web.Response:
    """Change Playlist Details 

    Change a playlist&#39;s name and public/private state. (The user must, of course, own the playlist.) 

    :param playlist_id: 
    :type playlist_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ChangePlaylistDetailsRequest.from_dict(body)
    return web.Response(status=200)


async def check_current_user_follows_1(request: web.Request, type, ids) -> web.Response:
    """Check If User Follows Artists or Users 

    Check to see if the current user is following one or more artists or other Spotify users. 

    :param type: 
    :type type: str
    :param ids: 
    :type ids: str

    """
    return web.Response(status=200)


async def check_users_saved_albums_0(request: web.Request, ids) -> web.Response:
    """Check User&#39;s Saved Albums 

    Check if one or more albums is already saved in the current Spotify user&#39;s &#39;Your Music&#39; library. 

    :param ids: 
    :type ids: str

    """
    return web.Response(status=200)


async def check_users_saved_audiobooks_0(request: web.Request, ids) -> web.Response:
    """Check User&#39;s Saved Audiobooks 

    Check if one or more audiobooks are already saved in the current Spotify user&#39;s library. 

    :param ids: 
    :type ids: str

    """
    return web.Response(status=200)


async def check_users_saved_episodes_0(request: web.Request, ids) -> web.Response:
    """Check User&#39;s Saved Episodes 

    Check if one or more episodes is already saved in the current Spotify user&#39;s &#39;Your Episodes&#39; library.&lt;br/&gt; This API endpoint is in __beta__ and could change without warning. Please share any feedback that you have, or issues that you discover, in our [developer community forum](https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer).. 

    :param ids: 
    :type ids: str

    """
    return web.Response(status=200)


async def check_users_saved_shows_0(request: web.Request, ids) -> web.Response:
    """Check User&#39;s Saved Shows 

    Check if one or more shows is already saved in the current Spotify user&#39;s library. 

    :param ids: 
    :type ids: str

    """
    return web.Response(status=200)


async def check_users_saved_tracks_0(request: web.Request, ids) -> web.Response:
    """Check User&#39;s Saved Tracks 

    Check if one or more tracks is already saved in the current Spotify user&#39;s &#39;Your Music&#39; library. 

    :param ids: 
    :type ids: str

    """
    return web.Response(status=200)


async def create_playlist_0(request: web.Request, user_id, body=None) -> web.Response:
    """Create Playlist 

    Create a playlist for a Spotify user. (The playlist will be empty until you [add tracks](/documentation/web-api/reference/add-tracks-to-playlist).) 

    :param user_id: 
    :type user_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreatePlaylistRequest.from_dict(body)
    return web.Response(status=200)


async def follow_artists_users_1(request: web.Request, type, ids, body=None) -> web.Response:
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


async def get_a_list_of_current_users_playlists_0(request: web.Request, limit=None, offset=None) -> web.Response:
    """Get Current User&#39;s Playlists 

    Get a list of the playlists owned or followed by the current Spotify user. 

    :param limit: 
    :type limit: int
    :param offset: 
    :type offset: int

    """
    return web.Response(status=200)


async def get_followed_0(request: web.Request, type, after=None, limit=None) -> web.Response:
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


async def get_users_saved_albums_0(request: web.Request, limit=None, offset=None, market=None) -> web.Response:
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


async def get_users_saved_audiobooks_0(request: web.Request, limit=None, offset=None) -> web.Response:
    """Get User&#39;s Saved Audiobooks 

    Get a list of the audiobooks saved in the current Spotify user&#39;s &#39;Your Music&#39; library. 

    :param limit: 
    :type limit: int
    :param offset: 
    :type offset: int

    """
    return web.Response(status=200)


async def get_users_saved_episodes_0(request: web.Request, market=None, limit=None, offset=None) -> web.Response:
    """Get User&#39;s Saved Episodes 

    Get a list of the episodes saved in the current Spotify user&#39;s library.&lt;br/&gt; This API endpoint is in __beta__ and could change without warning. Please share any feedback that you have, or issues that you discover, in our [developer community forum](https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer). 

    :param market: 
    :type market: str
    :param limit: 
    :type limit: int
    :param offset: 
    :type offset: int

    """
    return web.Response(status=200)


async def get_users_saved_shows_0(request: web.Request, limit=None, offset=None) -> web.Response:
    """Get User&#39;s Saved Shows 

    Get a list of shows saved in the current Spotify user&#39;s library. Optional parameters can be used to limit the number of shows returned. 

    :param limit: 
    :type limit: int
    :param offset: 
    :type offset: int

    """
    return web.Response(status=200)


async def get_users_saved_tracks_0(request: web.Request, market=None, limit=None, offset=None) -> web.Response:
    """Get User&#39;s Saved Tracks 

    Get a list of the songs saved in the current Spotify user&#39;s &#39;Your Music&#39; library. 

    :param market: 
    :type market: str
    :param limit: 
    :type limit: int
    :param offset: 
    :type offset: int

    """
    return web.Response(status=200)


async def get_users_top_artists_and_tracks_1(request: web.Request, type, time_range=None, limit=None, offset=None) -> web.Response:
    """Get User&#39;s Top Items 

    Get the current user&#39;s top artists or tracks based on calculated affinity. 

    :param type: 
    :type type: str
    :param time_range: 
    :type time_range: str
    :param limit: 
    :type limit: int
    :param offset: 
    :type offset: int

    """
    return web.Response(status=200)


async def remove_albums_user_0(request: web.Request, ids, body=None) -> web.Response:
    """Remove Users&#39; Saved Albums 

    Remove one or more albums from the current user&#39;s &#39;Your Music&#39; library. 

    :param ids: 
    :type ids: str
    :param body: 
    :type body: dict | bytes

    """
    body = SaveAlbumsUserRequest.from_dict(body)
    return web.Response(status=200)


async def remove_audiobooks_user_0(request: web.Request, ids) -> web.Response:
    """Remove User&#39;s Saved Audiobooks 

    Remove one or more audiobooks from the Spotify user&#39;s library. 

    :param ids: 
    :type ids: str

    """
    return web.Response(status=200)


async def remove_episodes_user_0(request: web.Request, ids, body=None) -> web.Response:
    """Remove User&#39;s Saved Episodes 

    Remove one or more episodes from the current user&#39;s library.&lt;br/&gt; This API endpoint is in __beta__ and could change without warning. Please share any feedback that you have, or issues that you discover, in our [developer community forum](https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer). 

    :param ids: 
    :type ids: str
    :param body: 
    :type body: dict | bytes

    """
    body = RemoveEpisodesUserRequest.from_dict(body)
    return web.Response(status=200)


async def remove_shows_user_0(request: web.Request, ids, market=None) -> web.Response:
    """Remove User&#39;s Saved Shows 

    Delete one or more shows from current Spotify user&#39;s library. 

    :param ids: 
    :type ids: str
    :param market: 
    :type market: str

    """
    return web.Response(status=200)


async def remove_tracks_user_0(request: web.Request, ids, body=None) -> web.Response:
    """Remove User&#39;s Saved Tracks 

    Remove one or more tracks from the current user&#39;s &#39;Your Music&#39; library. 

    :param ids: 
    :type ids: str
    :param body: 
    :type body: dict | bytes

    """
    body = SaveAlbumsUserRequest.from_dict(body)
    return web.Response(status=200)


async def save_albums_user_0(request: web.Request, ids, body=None) -> web.Response:
    """Save Albums for Current User 

    Save one or more albums to the current user&#39;s &#39;Your Music&#39; library. 

    :param ids: 
    :type ids: str
    :param body: 
    :type body: dict | bytes

    """
    body = SaveAlbumsUserRequest.from_dict(body)
    return web.Response(status=200)


async def save_audiobooks_user_0(request: web.Request, ids) -> web.Response:
    """Save Audiobooks for Current User 

    Save one or more audiobooks to the current Spotify user&#39;s library. 

    :param ids: 
    :type ids: str

    """
    return web.Response(status=200)


async def save_episodes_user_0(request: web.Request, ids, body=None) -> web.Response:
    """Save Episodes for Current User 

    Save one or more episodes to the current user&#39;s library.&lt;br/&gt; This API endpoint is in __beta__ and could change without warning. Please share any feedback that you have, or issues that you discover, in our [developer community forum](https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer). 

    :param ids: 
    :type ids: str
    :param body: 
    :type body: dict | bytes

    """
    body = SaveEpisodesUserRequest.from_dict(body)
    return web.Response(status=200)


async def save_shows_user_0(request: web.Request, ids) -> web.Response:
    """Save Shows for Current User 

    Save one or more shows to current Spotify user&#39;s library. 

    :param ids: 
    :type ids: str

    """
    return web.Response(status=200)


async def save_tracks_user_0(request: web.Request, ids, body=None) -> web.Response:
    """Save Tracks for Current User 

    Save one or more tracks to the current user&#39;s &#39;Your Music&#39; library. 

    :param ids: 
    :type ids: str
    :param body: 
    :type body: dict | bytes

    """
    body = SaveTracksUserRequest.from_dict(body)
    return web.Response(status=200)


async def unfollow_artists_users_1(request: web.Request, type, ids, body=None) -> web.Response:
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
