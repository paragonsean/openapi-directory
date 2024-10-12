from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_tracks_to_playlist_request import AddTracksToPlaylistRequest
from openapi_server.models.audio_analysis_object import AudioAnalysisObject
from openapi_server.models.audio_features_object import AudioFeaturesObject
from openapi_server.models.get_an_artists_top_tracks200_response import GetAnArtistsTopTracks200Response
from openapi_server.models.get_multiple_albums401_response import GetMultipleAlbums401Response
from openapi_server.models.get_several_audio_features200_response import GetSeveralAudioFeatures200Response
from openapi_server.models.paging_playlist_track_object import PagingPlaylistTrackObject
from openapi_server.models.paging_saved_track_object import PagingSavedTrackObject
from openapi_server.models.paging_simplified_track_object import PagingSimplifiedTrackObject
from openapi_server.models.paging_track_object import PagingTrackObject
from openapi_server.models.recommendations_object import RecommendationsObject
from openapi_server.models.remove_tracks_playlist_request import RemoveTracksPlaylistRequest
from openapi_server.models.reorder_or_replace_playlists_tracks200_response import ReorderOrReplacePlaylistsTracks200Response
from openapi_server.models.reorder_or_replace_playlists_tracks_request import ReorderOrReplacePlaylistsTracksRequest
from openapi_server.models.save_albums_user_request import SaveAlbumsUserRequest
from openapi_server.models.save_tracks_user_request import SaveTracksUserRequest
from openapi_server.models.track_object import TrackObject
from openapi_server import util


async def add_tracks_to_playlist_0(request: web.Request, playlist_id, position=None, uris=None, body=None) -> web.Response:
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


async def check_users_saved_tracks(request: web.Request, ids) -> web.Response:
    """Check User&#39;s Saved Tracks 

    Check if one or more tracks is already saved in the current Spotify user&#39;s &#39;Your Music&#39; library. 

    :param ids: 
    :type ids: str

    """
    return web.Response(status=200)


async def get_an_albums_tracks_0(request: web.Request, id, market=None, limit=None, offset=None) -> web.Response:
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


async def get_an_artists_top_tracks_0(request: web.Request, id, market=None) -> web.Response:
    """Get Artist&#39;s Top Tracks 

    Get Spotify catalog information about an artist&#39;s top tracks by country. 

    :param id: 
    :type id: str
    :param market: 
    :type market: str

    """
    return web.Response(status=200)


async def get_audio_analysis(request: web.Request, id) -> web.Response:
    """Get Track&#39;s Audio Analysis 

    Get a low-level audio analysis for a track in the Spotify catalog. The audio analysis describes the track’s structure and musical content, including rhythm, pitch, and timbre. 

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_audio_features(request: web.Request, id) -> web.Response:
    """Get Track&#39;s Audio Features 

    Get audio feature information for a single track identified by its unique Spotify ID. 

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_playlists_tracks_0(request: web.Request, playlist_id, market=None, fields=None, limit=None, offset=None, additional_types=None) -> web.Response:
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


async def get_recommendations(request: web.Request, limit=None, market=None, seed_artists=None, seed_genres=None, seed_tracks=None, min_acousticness=None, max_acousticness=None, target_acousticness=None, min_danceability=None, max_danceability=None, target_danceability=None, min_duration_ms=None, max_duration_ms=None, target_duration_ms=None, min_energy=None, max_energy=None, target_energy=None, min_instrumentalness=None, max_instrumentalness=None, target_instrumentalness=None, min_key=None, max_key=None, target_key=None, min_liveness=None, max_liveness=None, target_liveness=None, min_loudness=None, max_loudness=None, target_loudness=None, min_mode=None, max_mode=None, target_mode=None, min_popularity=None, max_popularity=None, target_popularity=None, min_speechiness=None, max_speechiness=None, target_speechiness=None, min_tempo=None, max_tempo=None, target_tempo=None, min_time_signature=None, max_time_signature=None, target_time_signature=None, min_valence=None, max_valence=None, target_valence=None) -> web.Response:
    """Get Recommendations 

    Recommendations are generated based on the available information for a given seed entity and matched against similar artists and tracks. If there is sufficient information about the provided seeds, a list of tracks will be returned together with pool size details.  For artists and tracks that are very new or obscure there might not be enough data to generate a list of tracks. 

    :param limit: 
    :type limit: int
    :param market: 
    :type market: str
    :param seed_artists: 
    :type seed_artists: str
    :param seed_genres: 
    :type seed_genres: str
    :param seed_tracks: 
    :type seed_tracks: str
    :param min_acousticness: 
    :type min_acousticness: 
    :param max_acousticness: 
    :type max_acousticness: 
    :param target_acousticness: 
    :type target_acousticness: 
    :param min_danceability: 
    :type min_danceability: 
    :param max_danceability: 
    :type max_danceability: 
    :param target_danceability: 
    :type target_danceability: 
    :param min_duration_ms: 
    :type min_duration_ms: int
    :param max_duration_ms: 
    :type max_duration_ms: int
    :param target_duration_ms: 
    :type target_duration_ms: int
    :param min_energy: 
    :type min_energy: 
    :param max_energy: 
    :type max_energy: 
    :param target_energy: 
    :type target_energy: 
    :param min_instrumentalness: 
    :type min_instrumentalness: 
    :param max_instrumentalness: 
    :type max_instrumentalness: 
    :param target_instrumentalness: 
    :type target_instrumentalness: 
    :param min_key: 
    :type min_key: int
    :param max_key: 
    :type max_key: int
    :param target_key: 
    :type target_key: int
    :param min_liveness: 
    :type min_liveness: 
    :param max_liveness: 
    :type max_liveness: 
    :param target_liveness: 
    :type target_liveness: 
    :param min_loudness: 
    :type min_loudness: 
    :param max_loudness: 
    :type max_loudness: 
    :param target_loudness: 
    :type target_loudness: 
    :param min_mode: 
    :type min_mode: int
    :param max_mode: 
    :type max_mode: int
    :param target_mode: 
    :type target_mode: int
    :param min_popularity: 
    :type min_popularity: int
    :param max_popularity: 
    :type max_popularity: int
    :param target_popularity: 
    :type target_popularity: int
    :param min_speechiness: 
    :type min_speechiness: 
    :param max_speechiness: 
    :type max_speechiness: 
    :param target_speechiness: 
    :type target_speechiness: 
    :param min_tempo: 
    :type min_tempo: 
    :param max_tempo: 
    :type max_tempo: 
    :param target_tempo: 
    :type target_tempo: 
    :param min_time_signature: 
    :type min_time_signature: int
    :param max_time_signature: 
    :type max_time_signature: int
    :param target_time_signature: 
    :type target_time_signature: int
    :param min_valence: 
    :type min_valence: 
    :param max_valence: 
    :type max_valence: 
    :param target_valence: 
    :type target_valence: 

    """
    return web.Response(status=200)


async def get_several_audio_features(request: web.Request, ids) -> web.Response:
    """Get Tracks&#39; Audio Features 

    Get audio features for multiple tracks based on their Spotify IDs. 

    :param ids: 
    :type ids: str

    """
    return web.Response(status=200)


async def get_several_tracks(request: web.Request, ids, market=None) -> web.Response:
    """Get Several Tracks 

    Get Spotify catalog information for multiple tracks based on their Spotify IDs. 

    :param ids: 
    :type ids: str
    :param market: 
    :type market: str

    """
    return web.Response(status=200)


async def get_track(request: web.Request, id, market=None) -> web.Response:
    """Get Track 

    Get Spotify catalog information for a single track identified by its unique Spotify ID. 

    :param id: 
    :type id: str
    :param market: 
    :type market: str

    """
    return web.Response(status=200)


async def get_users_saved_tracks(request: web.Request, market=None, limit=None, offset=None) -> web.Response:
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


async def get_users_top_tracks_0(request: web.Request, time_range=None, limit=None, offset=None) -> web.Response:
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


async def remove_tracks_playlist_0(request: web.Request, playlist_id, body=None) -> web.Response:
    """Remove Playlist Items 

    Remove one or more items from a user&#39;s playlist. 

    :param playlist_id: 
    :type playlist_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = RemoveTracksPlaylistRequest.from_dict(body)
    return web.Response(status=200)


async def remove_tracks_user(request: web.Request, ids, body=None) -> web.Response:
    """Remove User&#39;s Saved Tracks 

    Remove one or more tracks from the current user&#39;s &#39;Your Music&#39; library. 

    :param ids: 
    :type ids: str
    :param body: 
    :type body: dict | bytes

    """
    body = SaveAlbumsUserRequest.from_dict(body)
    return web.Response(status=200)


async def reorder_or_replace_playlists_tracks_0(request: web.Request, playlist_id, uris=None, body=None) -> web.Response:
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


async def save_tracks_user(request: web.Request, ids, body=None) -> web.Response:
    """Save Tracks for Current User 

    Save one or more tracks to the current user&#39;s &#39;Your Music&#39; library. 

    :param ids: 
    :type ids: str
    :param body: 
    :type body: dict | bytes

    """
    body = SaveTracksUserRequest.from_dict(body)
    return web.Response(status=200)
