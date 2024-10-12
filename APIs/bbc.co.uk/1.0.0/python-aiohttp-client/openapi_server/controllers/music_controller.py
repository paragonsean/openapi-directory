from typing import List, Dict
from aiohttp import web

from openapi_server.models.music_popularity_artists import MusicPopularityArtists
from openapi_server.models.music_popularity_error import MusicPopularityError
from openapi_server.models.music_popularity_playlists import MusicPopularityPlaylists
from openapi_server.models.music_popularity_tracks import MusicPopularityTracks
from openapi_server.models.personalised_music_batch_request import PersonalisedMusicBatchRequest
from openapi_server.models.personalised_music_error_response import PersonalisedMusicErrorResponse
from openapi_server.models.personalised_music_request import PersonalisedMusicRequest
from openapi_server.models.personalised_music_response import PersonalisedMusicResponse
from openapi_server.models.personalised_music_success import PersonalisedMusicSuccess
from openapi_server import util


async def delete_personalised_music_favourites_by_type_by_id(request: web.Request, authorization, x_authentication_provider, x_api_key, type, id) -> web.Response:
    """Favourite Track or Clip

    Delete track or clip from a BBC Music user favourites. 

    :param authorization: Bearer OAUTH_TOKEN
    :type authorization: str
    :param x_authentication_provider: Authentication type
    :type x_authentication_provider: str
    :param x_api_key: API_KEY
    :type x_api_key: str
    :param type: Supported Music favourite types: Clips or Tracks
    :type type: str
    :param id: Clip PID or Track ID
    :type id: str

    """
    return web.Response(status=200)


async def delete_personalised_music_follows_by_type_by_id(request: web.Request, authorization, x_authentication_provider, x_api_key, type, id, music_data=None, music_context=None, music_within_uk=None) -> web.Response:
    """Followed Network, Category, Artist, Playlist and Genre

    Remove a single network, category, artist, playlist, network, genre or service entity is in a users follows 

    :param authorization: Bearer OAUTH_TOKEN
    :type authorization: str
    :param x_authentication_provider: Authentication type
    :type x_authentication_provider: str
    :param x_api_key: API_KEY
    :type x_api_key: str
    :param type: Supported Music follows types: Playlists, Services, Genres &amp; Artists
    :type type: str
    :param id: Playlists, Services, Networks, Genres, Categories or Artists ID
    :type id: str
    :param music_data: Omits music data from the response, defaults to true
    :type music_data: bool
    :param music_context: Specify context to be passed to Music API
    :type music_context: str
    :param music_within_uk: Specify location to be passed to Music API
    :type music_within_uk: bool

    """
    return web.Response(status=200)


async def get_music_popular_artist_by_id(request: web.Request, x_api_key, id, since=None, until=None, decomposed=None) -> web.Response:
    """Single Artist Popularity

    Popularity Artist By Id 

    :param x_api_key: API_KEY
    :type x_api_key: str
    :param id: MusicBrainz Id - Used to get single resource score
    :type id: str
    :param since: ISO 8601 Date yyyy-mm-dd.  Returns items between given time period and now
    :type since: str
    :param until: ISO 8601 Date yyyy-mm-dd.  Returns items between given &#39;since&#39; and &#39;until&#39; date params
    :type until: str
    :param decomposed: In addition to the overall score, return a list of scores broken down by day N.B Must be used in conjunction with since and/or until and since is &gt;&#x3D; 31 days
    :type decomposed: bool

    """
    return web.Response(status=200)


async def get_music_popular_artists(request: web.Request, x_api_key, since=None, until=None, decomposed=None, offset=None, limit=None) -> web.Response:
    """Popular Artists

    List of Most Popular artists from BBC Music. 

    :param x_api_key: API_KEY
    :type x_api_key: str
    :param since: ISO 8601 Date yyyy-mm-dd.  Returns items between given time period and now
    :type since: str
    :param until: ISO 8601 Date yyyy-mm-dd.  Returns items between given &#39;since&#39; and &#39;until&#39; date params
    :type until: str
    :param decomposed: In addition to the overall score, return a list of scores broken down by day N.B Must be used in conjunction with since and/or until and since is &gt;&#x3D; 31 days
    :type decomposed: bool
    :param offset: Paginated results offset
    :type offset: int
    :param limit: Paginated results limit
    :type limit: int

    """
    return web.Response(status=200)


async def get_music_popular_playlist_by_id(request: web.Request, x_api_key, id, since=None, until=None, decomposed=None) -> web.Response:
    """Single Playlist Popularity

    Popular playlist by Id 

    :param x_api_key: API_KEY
    :type x_api_key: str
    :param id: BBC Music Playlist Id - Used to get single resource score
    :type id: str
    :param since: ISO 8601 Date yyyy-mm-dd.  Returns items between given time period and now
    :type since: str
    :param until: ISO 8601 Date yyyy-mm-dd.  Returns items between given &#39;since&#39; and &#39;until&#39; date params
    :type until: str
    :param decomposed: In addition to the overall score, return a list of scores broken down by day N.B Must be used in conjunction with since and/or until and since is &gt;&#x3D; 31 days
    :type decomposed: bool

    """
    return web.Response(status=200)


async def get_music_popular_playlists(request: web.Request, x_api_key, since=None, until=None, decomposed=None, offset=None, limit=None) -> web.Response:
    """Popular Playlists

    List of Most Popular playlists from BBC Music. 

    :param x_api_key: API_KEY
    :type x_api_key: str
    :param since: ISO 8601 Date yyyy-mm-dd.  Returns items between given time period and now
    :type since: str
    :param until: ISO 8601 Date yyyy-mm-dd.  Returns items between given &#39;since&#39; and &#39;until&#39; date params
    :type until: str
    :param decomposed: In addition to the overall score, return a list of scores broken down by day N.B Must be used in conjunction with since and/or until and since is &gt;&#x3D; 31 days
    :type decomposed: bool
    :param offset: Paginated results offset
    :type offset: int
    :param limit: Paginated results limit
    :type limit: int

    """
    return web.Response(status=200)


async def get_music_popular_track_by_id(request: web.Request, x_api_key, id, since=None, until=None, network=None, programme=None, artist=None, decomposed=None) -> web.Response:
    """Single Track Popularity

    Popular Track for BBC Music 

    :param x_api_key: API_KEY
    :type x_api_key: str
    :param id: BBC Music Track Id - Used to get single resource score
    :type id: str
    :param since: ISO 8601 Date yyyy-mm-dd.  Returns items between given time period and now
    :type since: str
    :param until: ISO 8601 Date yyyy-mm-dd.  Returns items between given &#39;since&#39; and &#39;until&#39; date params
    :type until: str
    :param network: Return items with given Network ID
    :type network: str
    :param programme: Items with given Programme Pid
    :type programme: str
    :param artist: MusicBrainz artist ID
    :type artist: str
    :param decomposed: In addition to the overall score, return a list of scores broken down by day N.B Must be used in conjunction with since and/or until and since is &gt;&#x3D; 31 days
    :type decomposed: bool

    """
    return web.Response(status=200)


async def get_music_popular_tracks(request: web.Request, x_api_key, since=None, until=None, network=None, programme=None, artist=None, decomposed=None, offset=None, limit=None) -> web.Response:
    """Popular Tracks

    List of popular tracks for BBC Music. Filter by time, network, artist, playlist or programme. 

    :param x_api_key: API_KEY
    :type x_api_key: str
    :param since: ISO 8601 Date yyyy-mm-dd.  Returns items between given time period and now
    :type since: str
    :param until: ISO 8601 Date yyyy-mm-dd.  Returns items between given &#39;since&#39; and &#39;until&#39; date params
    :type until: str
    :param network: Return items with given Network ID
    :type network: str
    :param programme: Items with given Programme Pid
    :type programme: str
    :param artist: MusicBrainz artist ID
    :type artist: str
    :param decomposed: In addition to the overall score, return a list of scores broken down by day N.B Must be used in conjunction with since and/or until and since is &gt;&#x3D; 31 days
    :type decomposed: bool
    :param offset: Paginated results offset
    :type offset: int
    :param limit: Paginated results limit
    :type limit: int

    """
    return web.Response(status=200)


async def get_personalised_music_favourites(request: web.Request, authorization, x_authentication_provider, x_api_key, offset=None, limit=None, action=None, music_data=None) -> web.Response:
    """Favourite Tracks or Clips

    List of favourited tracks and clips for a given user for BBC Music. 

    :param authorization: Bearer OAUTH_TOKEN
    :type authorization: str
    :param x_authentication_provider: Authentication type
    :type x_authentication_provider: str
    :param x_api_key: API_KEY
    :type x_api_key: str
    :param offset: Paginated results offset
    :type offset: int
    :param limit: Paginated results limit
    :type limit: int
    :param action: Filters activities based on the type of action
    :type action: str
    :param music_data: Omits music data from the response, defaults to true
    :type music_data: bool

    """
    return web.Response(status=200)


async def get_personalised_music_favourites_by_type(request: web.Request, authorization, x_authentication_provider, x_api_key, type, action=None, offset=None, limit=None) -> web.Response:
    """Favourite Tracks or Clips by Type

    List of favourited tracks or clips for a given user for BBC Music. 

    :param authorization: Bearer OAUTH_TOKEN
    :type authorization: str
    :param x_authentication_provider: Authentication type
    :type x_authentication_provider: str
    :param x_api_key: API_KEY
    :type x_api_key: str
    :param type: Supported Music favourite types: Clips or Tracks
    :type type: str
    :param action: Filters activities based on the type of action
    :type action: str
    :param offset: Paginated results offset
    :type offset: int
    :param limit: Paginated results limit
    :type limit: int

    """
    return web.Response(status=200)


async def get_personalised_music_favourites_by_type_by_id(request: web.Request, authorization, x_authentication_provider, x_api_key, type, id) -> web.Response:
    """Favourite Track or Clip

    Check to see if a single track or clip entity is in a users favourites - determines UX of add button. 

    :param authorization: Bearer OAUTH_TOKEN
    :type authorization: str
    :param x_authentication_provider: Authentication type
    :type x_authentication_provider: str
    :param x_api_key: API_KEY
    :type x_api_key: str
    :param type: Supported Music favourite types: Clips or Tracks
    :type type: str
    :param id: Clip PID or Track ID
    :type id: str

    """
    return web.Response(status=200)


async def get_personalised_music_follows(request: web.Request, authorization, x_authentication_provider, x_api_key, action=None, music_data=None, music_context=None, music_within_uk=None, offset=None, limit=None) -> web.Response:
    """Followed Networks, Categories, Artists, Playlists and Genres

    List of followed networks, categories, artists, playlists and genres for a given user for BBC Music. 

    :param authorization: Bearer OAUTH_TOKEN
    :type authorization: str
    :param x_authentication_provider: Authentication type
    :type x_authentication_provider: str
    :param x_api_key: API_KEY
    :type x_api_key: str
    :param action: Filters activities based on the type of action
    :type action: str
    :param music_data: Omits music data from the response, defaults to true
    :type music_data: bool
    :param music_context: Specify context to be passed to Music API
    :type music_context: str
    :param music_within_uk: Specify location to be passed to Music API
    :type music_within_uk: bool
    :param offset: Paginated results offset
    :type offset: int
    :param limit: Paginated results limit
    :type limit: int

    """
    return web.Response(status=200)


async def get_personalised_music_follows_by_type(request: web.Request, authorization, x_authentication_provider, x_api_key, type, action=None, music_data=None, music_context=None, music_within_uk=None, offset=None, limit=None) -> web.Response:
    """Followed Networks, Categories, Artists, Playlists and Genres by Type

    List of followed networks, categories, artists, playlists, networks, genres, categories or services for a given BBC Music user. 

    :param authorization: Bearer OAUTH_TOKEN
    :type authorization: str
    :param x_authentication_provider: Authentication type
    :type x_authentication_provider: str
    :param x_api_key: API_KEY
    :type x_api_key: str
    :param type: Supported Music follows types: Playlists, Services, Genres &amp; Artists
    :type type: str
    :param action: Filters activities based on the type of action
    :type action: str
    :param music_data: Omits music data from the response, defaults to true
    :type music_data: bool
    :param music_context: Specify context to be passed to Music API
    :type music_context: str
    :param music_within_uk: Specify location to be passed to Music API
    :type music_within_uk: bool
    :param offset: Paginated results offset
    :type offset: int
    :param limit: Paginated results limit
    :type limit: int

    """
    return web.Response(status=200)


async def get_personalised_music_follows_by_type_by_id(request: web.Request, authorization, x_authentication_provider, x_api_key, type, id, music_data=None, music_context=None, music_within_uk=None) -> web.Response:
    """Followed Network, Category, Artist, Playlist and Genre

    Check to see if a single network, category, artist, playlist, network, genre or service entity is in a users follows - determines UX of add button. 

    :param authorization: Bearer OAUTH_TOKEN
    :type authorization: str
    :param x_authentication_provider: Authentication type
    :type x_authentication_provider: str
    :param x_api_key: API_KEY
    :type x_api_key: str
    :param type: Supported Music follows types: Playlists, Services, Genres &amp; Artists
    :type type: str
    :param id: Playlists, Services, Networks, Genres, Categories or Artists ID
    :type id: str
    :param music_data: Omits music data from the response, defaults to true
    :type music_data: bool
    :param music_context: Specify context to be passed to Music API
    :type music_context: str
    :param music_within_uk: Specify location to be passed to Music API
    :type music_within_uk: bool

    """
    return web.Response(status=200)


async def post_personalised_music_favourites_batch(request: web.Request, authorization, x_authentication_provider, x_api_key, body) -> web.Response:
    """Favourite Tracks or Clips

    Add multiple tracks and/or clips to a BBC Music user&#39;s favourites.  N.B. Any HTML tags submitted in metadata will be removed 

    :param authorization: Bearer OAUTH_TOKEN
    :type authorization: str
    :param x_authentication_provider: Authentication type
    :type x_authentication_provider: str
    :param x_api_key: API_KEY
    :type x_api_key: str
    :param body: Action favourited or unfavourited
    :type body: list | bytes

    """
    body = [PersonalisedMusicBatchRequest.from_dict(d) for d in body]
    return web.Response(status=200)


async def post_personalised_music_favourites_by_type_by_id(request: web.Request, authorization, x_authentication_provider, x_api_key, type, id, body) -> web.Response:
    """Favourite Track or Clip

    Add track or clip to a BBC Music user favourites.  N.B. Any HTML tags submitted in metadata will be removed 

    :param authorization: Bearer OAUTH_TOKEN
    :type authorization: str
    :param x_authentication_provider: Authentication type
    :type x_authentication_provider: str
    :param x_api_key: API_KEY
    :type x_api_key: str
    :param type: Supported Music favourite types: Clips or Tracks
    :type type: str
    :param id: Clip PID or Track ID
    :type id: str
    :param body: Action favourited or unfavourited
    :type body: dict | bytes

    """
    body = PersonalisedMusicRequest.from_dict(body)
    return web.Response(status=200)


async def post_personalised_music_follows_batch(request: web.Request, authorization, x_authentication_provider, x_api_key, body, action=None, music_data=None, music_context=None, music_within_uk=None) -> web.Response:
    """Followed Networks, Categories, Artists, Playlists and Genres

    Add networks, categories, artists, playlists, networks, genres or services in a users follows  N.B. Any HTML tags submitted in metadata will be removed 

    :param authorization: Bearer OAUTH_TOKEN
    :type authorization: str
    :param x_authentication_provider: Authentication type
    :type x_authentication_provider: str
    :param x_api_key: API_KEY
    :type x_api_key: str
    :param body: Action followed or unfollowed
    :type body: list | bytes
    :param action: Filters activities based on the type of action
    :type action: str
    :param music_data: Omits music data from the response, defaults to true
    :type music_data: bool
    :param music_context: Specify context to be passed to Music API
    :type music_context: str
    :param music_within_uk: Specify location to be passed to Music API
    :type music_within_uk: bool

    """
    body = [PersonalisedMusicBatchRequest.from_dict(d) for d in body]
    return web.Response(status=200)


async def post_personalised_music_follows_by_type_by_id(request: web.Request, authorization, x_authentication_provider, x_api_key, type, id, body, music_data=None, music_context=None, music_within_uk=None) -> web.Response:
    """Followed Network, Category, Artist, Playlist and Genre

    Add a single network, category, artist, playlist, network, genre or service entity is in a users follows  N.B. Any HTML tags submitted in metadata will be removed 

    :param authorization: Bearer OAUTH_TOKEN
    :type authorization: str
    :param x_authentication_provider: Authentication type
    :type x_authentication_provider: str
    :param x_api_key: API_KEY
    :type x_api_key: str
    :param type: Supported Music follows types: Playlists, Services, Genres &amp; Artists
    :type type: str
    :param id: Playlists, Services, Networks, Genres, Categories or Artists ID
    :type id: str
    :param body: Action followed or unfollowed
    :type body: dict | bytes
    :param music_data: Omits music data from the response, defaults to true
    :type music_data: bool
    :param music_context: Specify context to be passed to Music API
    :type music_context: str
    :param music_within_uk: Specify location to be passed to Music API
    :type music_within_uk: bool

    """
    body = PersonalisedMusicRequest.from_dict(body)
    return web.Response(status=200)


async def put_personalised_music_favourites_batch(request: web.Request, authorization, x_authentication_provider, x_api_key, body) -> web.Response:
    """Favourite Tracks or Clips

    Update tracks or clips from a BBC Music user favourites.  N.B. Any HTML tags submitted in metadata will be removed 

    :param authorization: Bearer OAUTH_TOKEN
    :type authorization: str
    :param x_authentication_provider: Authentication type
    :type x_authentication_provider: str
    :param x_api_key: API_KEY
    :type x_api_key: str
    :param body: Action favourited or unfavourited
    :type body: list | bytes

    """
    body = [PersonalisedMusicBatchRequest.from_dict(d) for d in body]
    return web.Response(status=200)


async def put_personalised_music_favourites_by_type_by_id(request: web.Request, authorization, x_authentication_provider, x_api_key, type, id, body) -> web.Response:
    """Favourite Track or Clip

    Update tracks or clips from a BBC Music user favourites.  N.B. Any HTML tags submitted in metadata will be removed 

    :param authorization: Bearer OAUTH_TOKEN
    :type authorization: str
    :param x_authentication_provider: Authentication type
    :type x_authentication_provider: str
    :param x_api_key: API_KEY
    :type x_api_key: str
    :param type: Supported Music favourite types: Clips or Tracks
    :type type: str
    :param id: Clip PID or Track ID
    :type id: str
    :param body: Action favourited or unfavourited
    :type body: dict | bytes

    """
    body = PersonalisedMusicRequest.from_dict(body)
    return web.Response(status=200)


async def put_personalised_music_follows_batch(request: web.Request, authorization, x_authentication_provider, x_api_key, body, action=None, music_data=None, music_context=None, music_within_uk=None) -> web.Response:
    """Followed Networks, Categories, Artists, Playlists and Genres

    Update networks, categories, artists, playlists, networks, genres or services in a users follows  N.B. Any HTML tags submitted in metadata will be removed 

    :param authorization: Bearer OAUTH_TOKEN
    :type authorization: str
    :param x_authentication_provider: Authentication type
    :type x_authentication_provider: str
    :param x_api_key: API_KEY
    :type x_api_key: str
    :param body: Action followed or unfollowed
    :type body: list | bytes
    :param action: Filters activities based on the type of action
    :type action: str
    :param music_data: Omits music data from the response, defaults to true
    :type music_data: bool
    :param music_context: Specify context to be passed to Music API
    :type music_context: str
    :param music_within_uk: Specify location to be passed to Music API
    :type music_within_uk: bool

    """
    body = [PersonalisedMusicBatchRequest.from_dict(d) for d in body]
    return web.Response(status=200)


async def put_personalised_music_follows_by_type_by_id(request: web.Request, authorization, x_authentication_provider, x_api_key, type, id, body, music_data=None, music_context=None, music_within_uk=None) -> web.Response:
    """Followed Network, Category, Artist, Playlist and Genre

    Update a single network, category, artist, playlist, network, genre or service entity is in a users follows  N.B. Any HTML tags submitted in metadata will be removed 

    :param authorization: Bearer OAUTH_TOKEN
    :type authorization: str
    :param x_authentication_provider: Authentication type
    :type x_authentication_provider: str
    :param x_api_key: API_KEY
    :type x_api_key: str
    :param type: Supported Music follows types: Playlists, Services, Genres &amp; Artists
    :type type: str
    :param id: Playlists, Services, Networks, Genres, Categories or Artists ID
    :type id: str
    :param body: Action followed or unfollowed
    :type body: dict | bytes
    :param music_data: Omits music data from the response, defaults to true
    :type music_data: bool
    :param music_context: Specify context to be passed to Music API
    :type music_context: str
    :param music_within_uk: Specify location to be passed to Music API
    :type music_within_uk: bool

    """
    body = PersonalisedMusicRequest.from_dict(body)
    return web.Response(status=200)
