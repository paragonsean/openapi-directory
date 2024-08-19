from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_tracks_to_playlist_request import AddTracksToPlaylistRequest
from openapi_server.models.change_playlist_details_request import ChangePlaylistDetailsRequest
from openapi_server.models.create_playlist_request import CreatePlaylistRequest
from openapi_server.models.follow_playlist_request import FollowPlaylistRequest
from openapi_server.models.get_multiple_albums401_response import GetMultipleAlbums401Response
from openapi_server.models.image_object import ImageObject
from openapi_server.models.paging_featured_playlist_object import PagingFeaturedPlaylistObject
from openapi_server.models.paging_playlist_object import PagingPlaylistObject
from openapi_server.models.paging_playlist_track_object import PagingPlaylistTrackObject
from openapi_server.models.playlist_object import PlaylistObject
from openapi_server.models.remove_tracks_playlist_request import RemoveTracksPlaylistRequest
from openapi_server.models.reorder_or_replace_playlists_tracks200_response import ReorderOrReplacePlaylistsTracks200Response
from openapi_server.models.reorder_or_replace_playlists_tracks_request import ReorderOrReplacePlaylistsTracksRequest
from openapi_server import util


async def add_tracks_to_playlist(request: web.Request, playlist_id, position=None, uris=None, body=None) -> web.Response:
    """Add Items to Playlist 

    Add one or more items to a user&#39;s playlist. 

    :param playlist_id: 
    :type playlist_id: str
    :param position: 
    :type position: int
    :param uris: 
    :type uris: str
    :param body: 
    :type body: dict | bytes

    """
    body = AddTracksToPlaylistRequest.from_dict(body)
    return web.Response(status=200)


async def change_playlist_details(request: web.Request, playlist_id, body=None) -> web.Response:
    """Change Playlist Details 

    Change a playlist&#39;s name and public/private state. (The user must, of course, own the playlist.) 

    :param playlist_id: 
    :type playlist_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ChangePlaylistDetailsRequest.from_dict(body)
    return web.Response(status=200)


async def check_if_user_follows_playlist_0(request: web.Request, playlist_id, ids) -> web.Response:
    """Check if Users Follow Playlist 

    Check to see if one or more Spotify users are following a specified playlist. 

    :param playlist_id: 
    :type playlist_id: str
    :param ids: 
    :type ids: str

    """
    return web.Response(status=200)


async def create_playlist(request: web.Request, user_id, body=None) -> web.Response:
    """Create Playlist 

    Create a playlist for a Spotify user. (The playlist will be empty until you [add tracks](/documentation/web-api/reference/add-tracks-to-playlist).) 

    :param user_id: 
    :type user_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreatePlaylistRequest.from_dict(body)
    return web.Response(status=200)


async def follow_playlist_0(request: web.Request, playlist_id, body=None) -> web.Response:
    """Follow Playlist 

    Add the current user as a follower of a playlist. 

    :param playlist_id: 
    :type playlist_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = FollowPlaylistRequest.from_dict(body)
    return web.Response(status=200)


async def get_a_categories_playlists(request: web.Request, category_id, country=None, limit=None, offset=None) -> web.Response:
    """Get Category&#39;s Playlists 

    Get a list of Spotify playlists tagged with a particular category. 

    :param category_id: 
    :type category_id: str
    :param country: 
    :type country: str
    :param limit: 
    :type limit: int
    :param offset: 
    :type offset: int

    """
    return web.Response(status=200)


async def get_a_list_of_current_users_playlists(request: web.Request, limit=None, offset=None) -> web.Response:
    """Get Current User&#39;s Playlists 

    Get a list of the playlists owned or followed by the current Spotify user. 

    :param limit: 
    :type limit: int
    :param offset: 
    :type offset: int

    """
    return web.Response(status=200)


async def get_featured_playlists(request: web.Request, country=None, locale=None, timestamp=None, limit=None, offset=None) -> web.Response:
    """Get Featured Playlists 

    Get a list of Spotify featured playlists (shown, for example, on a Spotify player&#39;s &#39;Browse&#39; tab). 

    :param country: 
    :type country: str
    :param locale: 
    :type locale: str
    :param timestamp: 
    :type timestamp: str
    :param limit: 
    :type limit: int
    :param offset: 
    :type offset: int

    """
    return web.Response(status=200)


async def get_list_users_playlists(request: web.Request, user_id, limit=None, offset=None) -> web.Response:
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


async def get_playlist(request: web.Request, playlist_id, market=None, fields=None, additional_types=None) -> web.Response:
    """Get Playlist 

    Get a playlist owned by a Spotify user. 

    :param playlist_id: 
    :type playlist_id: str
    :param market: 
    :type market: str
    :param fields: 
    :type fields: str
    :param additional_types: 
    :type additional_types: str

    """
    return web.Response(status=200)


async def get_playlist_cover(request: web.Request, playlist_id) -> web.Response:
    """Get Playlist Cover Image 

    Get the current image associated with a specific playlist. 

    :param playlist_id: 
    :type playlist_id: str

    """
    return web.Response(status=200)


async def get_playlists_tracks(request: web.Request, playlist_id, market=None, fields=None, limit=None, offset=None, additional_types=None) -> web.Response:
    """Get Playlist Items 

    Get full details of the items of a playlist owned by a Spotify user. 

    :param playlist_id: 
    :type playlist_id: str
    :param market: 
    :type market: str
    :param fields: 
    :type fields: str
    :param limit: 
    :type limit: int
    :param offset: 
    :type offset: int
    :param additional_types: 
    :type additional_types: str

    """
    return web.Response(status=200)


async def remove_tracks_playlist(request: web.Request, playlist_id, body=None) -> web.Response:
    """Remove Playlist Items 

    Remove one or more items from a user&#39;s playlist. 

    :param playlist_id: 
    :type playlist_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = RemoveTracksPlaylistRequest.from_dict(body)
    return web.Response(status=200)


async def reorder_or_replace_playlists_tracks(request: web.Request, playlist_id, uris=None, body=None) -> web.Response:
    """Update Playlist Items 

    Either reorder or replace items in a playlist depending on the request&#39;s parameters. To reorder items, include &#x60;range_start&#x60;, &#x60;insert_before&#x60;, &#x60;range_length&#x60; and &#x60;snapshot_id&#x60; in the request&#39;s body. To replace items, include &#x60;uris&#x60; as either a query parameter or in the request&#39;s body. Replacing items in a playlist will overwrite its existing items. This operation can be used for replacing or clearing items in a playlist. &lt;br/&gt; **Note**: Replace and reorder are mutually exclusive operations which share the same endpoint, but have different parameters. These operations can&#39;t be applied together in a single request. 

    :param playlist_id: 
    :type playlist_id: str
    :param uris: 
    :type uris: str
    :param body: 
    :type body: dict | bytes

    """
    body = ReorderOrReplacePlaylistsTracksRequest.from_dict(body)
    return web.Response(status=200)


async def unfollow_playlist_0(request: web.Request, playlist_id) -> web.Response:
    """Unfollow Playlist 

    Remove the current user as a follower of a playlist. 

    :param playlist_id: 
    :type playlist_id: str

    """
    return web.Response(status=200)


async def upload_custom_playlist_cover(request: web.Request, playlist_id, body) -> web.Response:
    """Add Custom Playlist Cover Image 

    Replace the image used to represent a specific playlist. 

    :param playlist_id: 
    :type playlist_id: str
    :param body: The new cover image of the playlist as a Base64 encoded JPEG image. Maximum payload size is 256KB.
    :type body: str

    """
    return web.Response(status=200)
