from typing import List, Dict
from aiohttp import web

from openapi_server.models.advanced_search_filter_params import AdvancedSearchFilterParams
from openapi_server.models.album_for_api_contract import AlbumForApiContract
from openapi_server.models.album_for_api_contract_partial_find_result import AlbumForApiContractPartialFindResult
from openapi_server.models.album_for_user_for_api_contract import AlbumForUserForApiContract
from openapi_server.models.album_optional_fields import AlbumOptionalFields
from openapi_server.models.album_review_contract import AlbumReviewContract
from openapi_server.models.album_sort_rule import AlbumSortRule
from openapi_server.models.artist_album_participation_status import ArtistAlbumParticipationStatus
from openapi_server.models.comment_for_api_contract import CommentForApiContract
from openapi_server.models.content_language_preference import ContentLanguagePreference
from openapi_server.models.disc_type import DiscType
from openapi_server.models.entry_status import EntryStatus
from openapi_server.models.name_match_mode import NameMatchMode
from openapi_server.models.song_in_album_for_api_contract import SongInAlbumForApiContract
from openapi_server.models.song_optional_fields import SongOptionalFields
from openapi_server import util


async def api_albums_comments_comment_id_delete(request: web.Request, comment_id) -> web.Response:
    """api_albums_comments_comment_id_delete

    

    :param comment_id: 
    :type comment_id: int

    """
    return web.Response(status=200)


async def api_albums_comments_comment_id_post(request: web.Request, comment_id, body=None) -> web.Response:
    """api_albums_comments_comment_id_post

    

    :param comment_id: 
    :type comment_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = CommentForApiContract.from_dict(body)
    return web.Response(status=200)


async def api_albums_get(request: web.Request, query=None, disc_types=None, tag_name=None, tag_id=None, child_tags=None, artist_id=None, artist_participation_status=None, child_voicebanks=None, include_members=None, barcode=None, status=None, release_date_after=None, release_date_before=None, advanced_filters=None, start=None, max_results=None, get_total_count=None, sort=None, prefer_accurate_matches=None, deleted=None, name_match_mode=None, fields=None, lang=None) -> web.Response:
    """api_albums_get

    

    :param query: 
    :type query: str
    :param disc_types: 
    :type disc_types: dict | bytes
    :param tag_name: 
    :type tag_name: List[str]
    :param tag_id: 
    :type tag_id: List[int]
    :param child_tags: 
    :type child_tags: bool
    :param artist_id: 
    :type artist_id: List[int]
    :param artist_participation_status: 
    :type artist_participation_status: dict | bytes
    :param child_voicebanks: 
    :type child_voicebanks: bool
    :param include_members: 
    :type include_members: bool
    :param barcode: 
    :type barcode: str
    :param status: 
    :type status: dict | bytes
    :param release_date_after: 
    :type release_date_after: str
    :param release_date_before: 
    :type release_date_before: str
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
    :param deleted: 
    :type deleted: bool
    :param name_match_mode: 
    :type name_match_mode: dict | bytes
    :param fields: 
    :type fields: dict | bytes
    :param lang: 
    :type lang: dict | bytes

    """
    disc_types = .from_dict(disc_types)
    artist_participation_status = .from_dict(artist_participation_status)
    status = .from_dict(status)
    release_date_after = util.deserialize_datetime(release_date_after)
    release_date_before = util.deserialize_datetime(release_date_before)
    advanced_filters = [AdvancedSearchFilterParams.from_dict(d) for d in advanced_filters]
    sort = .from_dict(sort)
    name_match_mode = .from_dict(name_match_mode)
    fields = .from_dict(fields)
    lang = .from_dict(lang)
    return web.Response(status=200)


async def api_albums_id_comments_get(request: web.Request, id) -> web.Response:
    """api_albums_id_comments_get

    

    :param id: 
    :type id: int

    """
    return web.Response(status=200)


async def api_albums_id_comments_post(request: web.Request, id, body=None) -> web.Response:
    """api_albums_id_comments_post

    

    :param id: 
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = CommentForApiContract.from_dict(body)
    return web.Response(status=200)


async def api_albums_id_delete(request: web.Request, id, notes=None) -> web.Response:
    """api_albums_id_delete

    

    :param id: 
    :type id: int
    :param notes: 
    :type notes: str

    """
    return web.Response(status=200)


async def api_albums_id_get(request: web.Request, id, fields=None, song_fields=None, lang=None) -> web.Response:
    """api_albums_id_get

    

    :param id: 
    :type id: int
    :param fields: 
    :type fields: dict | bytes
    :param song_fields: 
    :type song_fields: dict | bytes
    :param lang: 
    :type lang: dict | bytes

    """
    fields = .from_dict(fields)
    song_fields = .from_dict(song_fields)
    lang = .from_dict(lang)
    return web.Response(status=200)


async def api_albums_id_reviews_get(request: web.Request, id, language_code=None) -> web.Response:
    """api_albums_id_reviews_get

    

    :param id: 
    :type id: int
    :param language_code: 
    :type language_code: str

    """
    return web.Response(status=200)


async def api_albums_id_reviews_post(request: web.Request, id, body=None) -> web.Response:
    """api_albums_id_reviews_post

    

    :param id: 
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = AlbumReviewContract.from_dict(body)
    return web.Response(status=200)


async def api_albums_id_reviews_review_id_delete(request: web.Request, review_id, id) -> web.Response:
    """api_albums_id_reviews_review_id_delete

    

    :param review_id: 
    :type review_id: int
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def api_albums_id_tracks_fields_get(request: web.Request, id, _field=None, disc_number=None, lang=None) -> web.Response:
    """api_albums_id_tracks_fields_get

    

    :param id: 
    :type id: int
    :param _field: 
    :type _field: List[str]
    :param disc_number: 
    :type disc_number: int
    :param lang: 
    :type lang: dict | bytes

    """
    lang = .from_dict(lang)
    return web.Response(status=200)


async def api_albums_id_tracks_get(request: web.Request, id, fields=None, lang=None) -> web.Response:
    """api_albums_id_tracks_get

    

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


async def api_albums_id_user_collections_get(request: web.Request, id, language_preference=None) -> web.Response:
    """api_albums_id_user_collections_get

    

    :param id: 
    :type id: int
    :param language_preference: 
    :type language_preference: dict | bytes

    """
    language_preference = .from_dict(language_preference)
    return web.Response(status=200)


async def api_albums_names_get(request: web.Request, query=None, name_match_mode=None, max_results=None) -> web.Response:
    """api_albums_names_get

    

    :param query: 
    :type query: str
    :param name_match_mode: 
    :type name_match_mode: dict | bytes
    :param max_results: 
    :type max_results: int

    """
    name_match_mode = .from_dict(name_match_mode)
    return web.Response(status=200)


async def api_albums_new_get(request: web.Request, language_preference=None, fields=None) -> web.Response:
    """api_albums_new_get

    

    :param language_preference: 
    :type language_preference: dict | bytes
    :param fields: 
    :type fields: dict | bytes

    """
    language_preference = .from_dict(language_preference)
    fields = .from_dict(fields)
    return web.Response(status=200)


async def api_albums_top_get(request: web.Request, ignore_ids=None, language_preference=None, fields=None) -> web.Response:
    """api_albums_top_get

    

    :param ignore_ids: 
    :type ignore_ids: List[int]
    :param language_preference: 
    :type language_preference: dict | bytes
    :param fields: 
    :type fields: dict | bytes

    """
    language_preference = .from_dict(language_preference)
    fields = .from_dict(fields)
    return web.Response(status=200)
