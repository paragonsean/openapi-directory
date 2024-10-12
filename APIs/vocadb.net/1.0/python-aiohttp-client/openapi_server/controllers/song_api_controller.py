from typing import List, Dict
from aiohttp import web

from openapi_server.models.advanced_search_filter_params import AdvancedSearchFilterParams
from openapi_server.models.artist_album_participation_status import ArtistAlbumParticipationStatus
from openapi_server.models.comment_for_api_contract import CommentForApiContract
from openapi_server.models.content_language_preference import ContentLanguagePreference
from openapi_server.models.entry_status import EntryStatus
from openapi_server.models.lyrics_for_song_contract import LyricsForSongContract
from openapi_server.models.name_match_mode import NameMatchMode
from openapi_server.models.pv_service import PVService
from openapi_server.models.pv_services import PVServices
from openapi_server.models.rated_song_for_user_for_api_contract import RatedSongForUserForApiContract
from openapi_server.models.related_songs_contract import RelatedSongsContract
from openapi_server.models.song_for_api_contract import SongForApiContract
from openapi_server.models.song_for_api_contract_partial_find_result import SongForApiContractPartialFindResult
from openapi_server.models.song_optional_fields import SongOptionalFields
from openapi_server.models.song_rating_contract import SongRatingContract
from openapi_server.models.song_sort_rule import SongSortRule
from openapi_server.models.song_vocalist_selection import SongVocalistSelection
from openapi_server.models.top_songs_date_filter_type import TopSongsDateFilterType
from openapi_server.models.user_optional_fields import UserOptionalFields
from openapi_server import util


async def api_songs_by_pv_get(request: web.Request, pv_service=None, pv_id=None, fields=None, lang=None) -> web.Response:
    """api_songs_by_pv_get

    

    :param pv_service: 
    :type pv_service: dict | bytes
    :param pv_id: 
    :type pv_id: str
    :param fields: 
    :type fields: dict | bytes
    :param lang: 
    :type lang: dict | bytes

    """
    pv_service = .from_dict(pv_service)
    fields = .from_dict(fields)
    lang = .from_dict(lang)
    return web.Response(status=200)


async def api_songs_comments_comment_id_delete(request: web.Request, comment_id) -> web.Response:
    """api_songs_comments_comment_id_delete

    

    :param comment_id: 
    :type comment_id: int

    """
    return web.Response(status=200)


async def api_songs_comments_comment_id_post(request: web.Request, comment_id, body=None) -> web.Response:
    """api_songs_comments_comment_id_post

    

    :param comment_id: 
    :type comment_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = CommentForApiContract.from_dict(body)
    return web.Response(status=200)


async def api_songs_get(request: web.Request, query=None, song_types=None, after_date=None, before_date=None, tag_name=None, tag_id=None, child_tags=None, unify_types_and_tags=None, artist_id=None, artist_participation_status=None, child_voicebanks=None, include_members=None, only_with_pvs=None, pv_services=None, since=None, min_score=None, user_collection_id=None, release_event_id=None, parent_song_id=None, status=None, advanced_filters=None, start=None, max_results=None, get_total_count=None, sort=None, prefer_accurate_matches=None, name_match_mode=None, fields=None, lang=None, min_milli_bpm=None, max_milli_bpm=None, min_length=None, max_length=None) -> web.Response:
    """api_songs_get

    

    :param query: 
    :type query: str
    :param song_types: 
    :type song_types: str
    :param after_date: 
    :type after_date: str
    :param before_date: 
    :type before_date: str
    :param tag_name: 
    :type tag_name: List[str]
    :param tag_id: 
    :type tag_id: List[int]
    :param child_tags: 
    :type child_tags: bool
    :param unify_types_and_tags: 
    :type unify_types_and_tags: bool
    :param artist_id: 
    :type artist_id: List[int]
    :param artist_participation_status: 
    :type artist_participation_status: dict | bytes
    :param child_voicebanks: 
    :type child_voicebanks: bool
    :param include_members: 
    :type include_members: bool
    :param only_with_pvs: 
    :type only_with_pvs: bool
    :param pv_services: 
    :type pv_services: dict | bytes
    :param since: 
    :type since: int
    :param min_score: 
    :type min_score: int
    :param user_collection_id: 
    :type user_collection_id: int
    :param release_event_id: 
    :type release_event_id: int
    :param parent_song_id: 
    :type parent_song_id: int
    :param status: 
    :type status: dict | bytes
    :param advanced_filters: 
    :type advanced_filters: list | bytes
    :param start: 
    :type start: int
    :param max_results: 
    :type max_results: int
    :param get_total_count: 
    :type get_total_count: bool
    :param sort: 
    :type sort: dict | bytes
    :param prefer_accurate_matches: 
    :type prefer_accurate_matches: bool
    :param name_match_mode: 
    :type name_match_mode: dict | bytes
    :param fields: 
    :type fields: dict | bytes
    :param lang: 
    :type lang: dict | bytes
    :param min_milli_bpm: 
    :type min_milli_bpm: int
    :param max_milli_bpm: 
    :type max_milli_bpm: int
    :param min_length: 
    :type min_length: int
    :param max_length: 
    :type max_length: int

    """
    after_date = util.deserialize_datetime(after_date)
    before_date = util.deserialize_datetime(before_date)
    artist_participation_status = .from_dict(artist_participation_status)
    pv_services = .from_dict(pv_services)
    status = .from_dict(status)
    advanced_filters = [AdvancedSearchFilterParams.from_dict(d) for d in advanced_filters]
    sort = .from_dict(sort)
    name_match_mode = .from_dict(name_match_mode)
    fields = .from_dict(fields)
    lang = .from_dict(lang)
    return web.Response(status=200)


async def api_songs_highlighted_get(request: web.Request, language_preference=None, fields=None) -> web.Response:
    """api_songs_highlighted_get

    

    :param language_preference: 
    :type language_preference: dict | bytes
    :param fields: 
    :type fields: dict | bytes

    """
    language_preference = .from_dict(language_preference)
    fields = .from_dict(fields)
    return web.Response(status=200)


async def api_songs_id_comments_get(request: web.Request, id) -> web.Response:
    """api_songs_id_comments_get

    

    :param id: 
    :type id: int

    """
    return web.Response(status=200)


async def api_songs_id_comments_post(request: web.Request, id, body=None) -> web.Response:
    """api_songs_id_comments_post

    

    :param id: 
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = CommentForApiContract.from_dict(body)
    return web.Response(status=200)


async def api_songs_id_delete(request: web.Request, id, notes=None) -> web.Response:
    """api_songs_id_delete

    

    :param id: 
    :type id: int
    :param notes: 
    :type notes: str

    """
    return web.Response(status=200)


async def api_songs_id_derived_get(request: web.Request, id, fields=None, lang=None) -> web.Response:
    """api_songs_id_derived_get

    

    :param id: 
    :type id: int
    :param fields: 
    :type fields: dict | bytes
    :param lang: 
    :type lang: dict | bytes

    """
    fields = .from_dict(fields)
    lang = .from_dict(lang)
    return web.Response(status=200)


async def api_songs_id_get(request: web.Request, id, fields=None, lang=None) -> web.Response:
    """api_songs_id_get

    

    :param id: 
    :type id: int
    :param fields: 
    :type fields: dict | bytes
    :param lang: 
    :type lang: dict | bytes

    """
    fields = .from_dict(fields)
    lang = .from_dict(lang)
    return web.Response(status=200)


async def api_songs_id_ratings_get(request: web.Request, id, user_fields=None, lang=None) -> web.Response:
    """api_songs_id_ratings_get

    

    :param id: 
    :type id: int
    :param user_fields: 
    :type user_fields: dict | bytes
    :param lang: 
    :type lang: dict | bytes

    """
    user_fields = .from_dict(user_fields)
    lang = .from_dict(lang)
    return web.Response(status=200)


async def api_songs_id_ratings_post(request: web.Request, id, body=None) -> web.Response:
    """api_songs_id_ratings_post

    

    :param id: 
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = SongRatingContract.from_dict(body)
    return web.Response(status=200)


async def api_songs_id_related_get(request: web.Request, id, fields=None, lang=None) -> web.Response:
    """api_songs_id_related_get

    

    :param id: 
    :type id: int
    :param fields: 
    :type fields: dict | bytes
    :param lang: 
    :type lang: dict | bytes

    """
    fields = .from_dict(fields)
    lang = .from_dict(lang)
    return web.Response(status=200)


async def api_songs_lyrics_lyrics_id_get(request: web.Request, lyrics_id) -> web.Response:
    """api_songs_lyrics_lyrics_id_get

    

    :param lyrics_id: 
    :type lyrics_id: int

    """
    return web.Response(status=200)


async def api_songs_names_get(request: web.Request, query=None, name_match_mode=None, max_results=None) -> web.Response:
    """api_songs_names_get

    

    :param query: 
    :type query: str
    :param name_match_mode: 
    :type name_match_mode: dict | bytes
    :param max_results: 
    :type max_results: int

    """
    name_match_mode = .from_dict(name_match_mode)
    return web.Response(status=200)


async def api_songs_top_rated_get(request: web.Request, duration_hours=None, start_date=None, filter_by=None, vocalist=None, max_results=None, fields=None, language_preference=None) -> web.Response:
    """api_songs_top_rated_get

    

    :param duration_hours: 
    :type duration_hours: int
    :param start_date: 
    :type start_date: str
    :param filter_by: 
    :type filter_by: dict | bytes
    :param vocalist: 
    :type vocalist: dict | bytes
    :param max_results: 
    :type max_results: int
    :param fields: 
    :type fields: dict | bytes
    :param language_preference: 
    :type language_preference: dict | bytes

    """
    start_date = util.deserialize_datetime(start_date)
    filter_by = .from_dict(filter_by)
    vocalist = .from_dict(vocalist)
    fields = .from_dict(fields)
    language_preference = .from_dict(language_preference)
    return web.Response(status=200)
