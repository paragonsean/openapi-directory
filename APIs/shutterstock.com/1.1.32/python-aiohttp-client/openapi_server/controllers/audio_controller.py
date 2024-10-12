from typing import List, Dict
from aiohttp import web

from openapi_server.models.audio import Audio
from openapi_server.models.audio_data_list import AudioDataList
from openapi_server.models.audio_search_results import AudioSearchResults
from openapi_server.models.audio_url import AudioUrl
from openapi_server.models.collection import Collection
from openapi_server.models.collection_create_request import CollectionCreateRequest
from openapi_server.models.collection_create_response import CollectionCreateResponse
from openapi_server.models.collection_data_list import CollectionDataList
from openapi_server.models.collection_item_data_list import CollectionItemDataList
from openapi_server.models.collection_item_request import CollectionItemRequest
from openapi_server.models.collection_update_request import CollectionUpdateRequest
from openapi_server.models.download_history_data_list import DownloadHistoryDataList
from openapi_server.models.genre_list import GenreList
from openapi_server.models.instrument_list import InstrumentList
from openapi_server.models.license_audio_request import LicenseAudioRequest
from openapi_server.models.license_audio_result_data_list import LicenseAudioResultDataList
from openapi_server.models.mood_list import MoodList
from openapi_server import util


async def add_track_collection_items(request: web.Request, id, body) -> web.Response:
    """Add audio tracks to collections

    This endpoint adds one or more tracks to a collection by track IDs.

    :param id: Collection ID
    :type id: str
    :param body: List of items to add to collection
    :type body: dict | bytes

    """
    body = CollectionItemRequest.from_dict(body)
    return web.Response(status=200)


async def create_track_collection(request: web.Request, body) -> web.Response:
    """Create audio collections

    This endpoint creates one or more collections (soundboxes). To add tracks, use &#x60;POST /v2/audio/collections/{id}/items&#x60;.

    :param body: Collection metadata
    :type body: dict | bytes

    """
    body = CollectionCreateRequest.from_dict(body)
    return web.Response(status=200)


async def delete_track_collection(request: web.Request, id) -> web.Response:
    """Delete audio collections

    This endpoint deletes a collection.

    :param id: Collection ID
    :type id: str

    """
    return web.Response(status=200)


async def delete_track_collection_items(request: web.Request, id, item_id=None) -> web.Response:
    """Remove audio tracks from collections

    This endpoint removes one or more tracks from a collection.

    :param id: Collection ID
    :type id: str
    :param item_id: One or more item IDs to remove from the collection
    :type item_id: List[str]

    """
    return web.Response(status=200)


async def download_tracks(request: web.Request, id) -> web.Response:
    """Download audio tracks

    This endpoint redownloads tracks that you have already received a license for. The download links in the response are valid for 8 hours.

    :param id: License ID
    :type id: str

    """
    return web.Response(status=200)


async def get_track(request: web.Request, id, view=None, search_id=None) -> web.Response:
    """Get details about audio tracks

    This endpoint shows information about a track, including its genres, instruments, and other attributes.

    :param id: Audio track ID
    :type id: int
    :param view: Amount of detail to render in the response
    :type view: str
    :param search_id: The ID of the search that is related to this request
    :type search_id: str

    """
    return web.Response(status=200)


async def get_track_collection(request: web.Request, id, embed=None, share_code=None) -> web.Response:
    """Get the details of audio collections

    This endpoint gets more detailed information about a collection, including the number of items in it and when it was last updated. To get the tracks in collections, use &#x60;GET /v2/audio/collections/{id}/items&#x60;.

    :param id: Collection ID
    :type id: str
    :param embed: Which sharing information to include in the response, such as a URL to the collection
    :type embed: List[str]
    :param share_code: Code to retrieve a shared collection
    :type share_code: str

    """
    return web.Response(status=200)


async def get_track_collection_items(request: web.Request, id, page=None, per_page=None, share_code=None, sort=None) -> web.Response:
    """Get the contents of audio collections

    This endpoint lists the IDs of tracks in a collection and the date that each was added.

    :param id: Collection ID
    :type id: str
    :param page: Page number
    :type page: int
    :param per_page: Number of results per page
    :type per_page: int
    :param share_code: Code to retrieve the contents of a shared collection
    :type share_code: str
    :param sort: Sort order
    :type sort: str

    """
    return web.Response(status=200)


async def get_track_collection_list(request: web.Request, page=None, per_page=None, embed=None) -> web.Response:
    """List audio collections

    This endpoint lists your collections of audio tracks and their basic attributes.

    :param page: Page number
    :type page: int
    :param per_page: Number of results per page
    :type per_page: int
    :param embed: Which sharing information to include in the response, such as a URL to the collection
    :type embed: List[str]

    """
    return web.Response(status=200)


async def get_track_license_list(request: web.Request, audio_id=None, license=None, page=None, per_page=None, sort=None, username=None, start_date=None, end_date=None, download_availability=None, team_history=None) -> web.Response:
    """List audio licenses

    This endpoint lists existing licenses. You can filter the results according to the track ID to see if you have an existing license for a specific track.

    :param audio_id: Show licenses for the specified track ID
    :type audio_id: str
    :param license: Restrict results by license. Prepending a &#x60;-&#x60; sign will exclude results by license
    :type license: str
    :param page: Page number
    :type page: int
    :param per_page: Number of results per page
    :type per_page: int
    :param sort: Sort order
    :type sort: str
    :param username: Filter licenses by username of licensee
    :type username: str
    :param start_date: Show licenses created on or after the specified date
    :type start_date: str
    :param end_date: Show licenses created before the specified date
    :type end_date: str
    :param download_availability: Filter licenses by download availability
    :type download_availability: str
    :param team_history: Set to true to see license history for all members of your team.
    :type team_history: bool

    """
    start_date = util.deserialize_datetime(start_date)
    end_date = util.deserialize_datetime(end_date)
    return web.Response(status=200)


async def get_track_list(request: web.Request, id, view=None, search_id=None) -> web.Response:
    """List audio tracks

    This endpoint lists information about one or more audio tracks, including the description and publication date.

    :param id: One or more audio IDs
    :type id: List[str]
    :param view: Amount of detail to render in the response
    :type view: str
    :param search_id: The ID of the search that is related to this request
    :type search_id: str

    """
    return web.Response(status=200)


async def license_track(request: web.Request, body, license=None, search_id=None) -> web.Response:
    """License audio tracks

    This endpoint gets licenses for one or more tracks. The download links in the response are valid for 8 hours.

    :param body: Tracks to license
    :type body: dict | bytes
    :param license: License type
    :type license: str
    :param search_id: The ID of the search that led to licensing this track
    :type search_id: str

    """
    body = LicenseAudioRequest.from_dict(body)
    return web.Response(status=200)


async def list_genres(request: web.Request, language=None) -> web.Response:
    """List audio genres

    This endpoint returns a list of all audio genres.

    :param language: Which language the genres will be returned
    :type language: str

    """
    return web.Response(status=200)


async def list_instruments(request: web.Request, language=None) -> web.Response:
    """List audio instruments

    This endpoint returns a list of all audio instruments.

    :param language: Which language the instruments will be returned in
    :type language: str

    """
    return web.Response(status=200)


async def list_moods(request: web.Request, language=None) -> web.Response:
    """List audio moods

    This endpoint returns a list of all audio moods.

    :param language: Which language the moods will be returned in
    :type language: str

    """
    return web.Response(status=200)


async def rename_track_collection(request: web.Request, id, body) -> web.Response:
    """Rename audio collections

    This endpoint sets a new name for a collection.

    :param id: Collection ID
    :type id: str
    :param body: Collection changes
    :type body: dict | bytes

    """
    body = CollectionUpdateRequest.from_dict(body)
    return web.Response(status=200)


async def search_tracks(request: web.Request, artists=None, bpm=None, bpm_from=None, bpm_to=None, duration=None, duration_from=None, duration_to=None, genre=None, is_instrumental=None, instruments=None, moods=None, page=None, per_page=None, query=None, sort=None, sort_order=None, vocal_description=None, view=None, fields=None, library=None, language=None) -> web.Response:
    """Search for tracks

    This endpoint searches for tracks. If you specify more than one search parameter, the API uses an AND condition. Array parameters can be specified multiple times; in this case, the API uses an AND or an OR condition with those values, depending on the parameter.

    :param artists: Show tracks with one of the specified artist names or IDs
    :type artists: List[str]
    :param bpm: (Deprecated; use bpm_from and bpm_to instead) Show tracks with the specified beats per minute
    :type bpm: int
    :param bpm_from: Show tracks with the specified beats per minute or faster
    :type bpm_from: int
    :param bpm_to: Show tracks with the specified beats per minute or slower
    :type bpm_to: int
    :param duration: Show tracks with the specified duration in seconds
    :type duration: int
    :param duration_from: Show tracks with the specified duration or longer in seconds
    :type duration_from: int
    :param duration_to: Show tracks with the specified duration or shorter in seconds
    :type duration_to: int
    :param genre: Show tracks with each of the specified genres; to get the list of genres, use &#x60;GET /v2/audio/genres&#x60;
    :type genre: List[str]
    :param is_instrumental: Show instrumental music only
    :type is_instrumental: bool
    :param instruments: Show tracks with each of the specified instruments; to get the list of instruments, use &#x60;GET /v2/audio/instruments&#x60;
    :type instruments: List[str]
    :param moods: Show tracks with each of the specified moods; to get the list of moods, use &#x60;GET /v2/audio/moods&#x60;
    :type moods: List[str]
    :param page: Page number
    :type page: int
    :param per_page: Number of results per page
    :type per_page: int
    :param query: One or more search terms separated by spaces
    :type query: str
    :param sort: Sort by
    :type sort: str
    :param sort_order: Sort order
    :type sort_order: str
    :param vocal_description: Show tracks with the specified vocal description (male, female)
    :type vocal_description: str
    :param view: Amount of detail to render in the response
    :type view: str
    :param fields: Fields to display in the response; see the documentation for the fields parameter in the overview section
    :type fields: str
    :param library: Which library to search
    :type library: str
    :param language: Which language to search in
    :type language: str

    """
    return web.Response(status=200)
