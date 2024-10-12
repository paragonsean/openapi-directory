from typing import List, Dict
from aiohttp import web

from openapi_server.models.advanced_search_filter_params import AdvancedSearchFilterParams
from openapi_server.models.comment_for_api_contract import CommentForApiContract
from openapi_server.models.comment_for_api_contract_partial_find_result import CommentForApiContractPartialFindResult
from openapi_server.models.content_language_preference import ContentLanguagePreference
from openapi_server.models.name_match_mode import NameMatchMode
from openapi_server.models.pv_services import PVServices
from openapi_server.models.song_in_list_for_api_contract_partial_find_result import SongInListForApiContractPartialFindResult
from openapi_server.models.song_list_featured_category import SongListFeaturedCategory
from openapi_server.models.song_list_for_api_contract_partial_find_result import SongListForApiContractPartialFindResult
from openapi_server.models.song_list_for_edit_for_api_contract import SongListForEditForApiContract
from openapi_server.models.song_list_optional_fields import SongListOptionalFields
from openapi_server.models.song_list_sort_rule import SongListSortRule
from openapi_server.models.song_optional_fields import SongOptionalFields
from openapi_server.models.song_sort_rule import SongSortRule
from openapi_server import util


async def api_song_lists_comments_comment_id_delete(request: web.Request, comment_id) -> web.Response:
    """api_song_lists_comments_comment_id_delete

    

    :param comment_id: 
    :type comment_id: int

    """
    return web.Response(status=200)


async def api_song_lists_comments_comment_id_post(request: web.Request, comment_id, body=None) -> web.Response:
    """api_song_lists_comments_comment_id_post

    

    :param comment_id: 
    :type comment_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = CommentForApiContract.from_dict(body)
    return web.Response(status=200)


async def api_song_lists_featured_get(request: web.Request, query=None, tag_id=None, child_tags=None, name_match_mode=None, featured_category=None, start=None, max_results=None, get_total_count=None, sort=None, fields=None, lang=None) -> web.Response:
    """api_song_lists_featured_get

    

    :param query: 
    :type query: str
    :param tag_id: 
    :type tag_id: List[int]
    :param child_tags: 
    :type child_tags: bool
    :param name_match_mode: 
    :type name_match_mode: dict | bytes
    :param featured_category: 
    :type featured_category: dict | bytes
    :param start: 
    :type start: int
    :param max_results: 
    :type max_results: int
    :param get_total_count: 
    :type get_total_count: bool
    :param sort: 
    :type sort: dict | bytes
    :param fields: 
    :type fields: dict | bytes
    :param lang: 
    :type lang: dict | bytes

    """
    name_match_mode = .from_dict(name_match_mode)
    featured_category = .from_dict(featured_category)
    sort = .from_dict(sort)
    fields = .from_dict(fields)
    lang = .from_dict(lang)
    return web.Response(status=200)


async def api_song_lists_featured_names_get(request: web.Request, query=None, name_match_mode=None, featured_category=None, max_results=None) -> web.Response:
    """api_song_lists_featured_names_get

    

    :param query: 
    :type query: str
    :param name_match_mode: 
    :type name_match_mode: dict | bytes
    :param featured_category: 
    :type featured_category: dict | bytes
    :param max_results: 
    :type max_results: int

    """
    name_match_mode = .from_dict(name_match_mode)
    featured_category = .from_dict(featured_category)
    return web.Response(status=200)


async def api_song_lists_id_delete(request: web.Request, id, notes=None, hard_delete=None) -> web.Response:
    """api_song_lists_id_delete

    

    :param id: 
    :type id: int
    :param notes: 
    :type notes: str
    :param hard_delete: 
    :type hard_delete: bool

    """
    return web.Response(status=200)


async def api_song_lists_list_id_comments_get(request: web.Request, list_id) -> web.Response:
    """api_song_lists_list_id_comments_get

    

    :param list_id: 
    :type list_id: int

    """
    return web.Response(status=200)


async def api_song_lists_list_id_comments_post(request: web.Request, list_id, body=None) -> web.Response:
    """api_song_lists_list_id_comments_post

    

    :param list_id: 
    :type list_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = CommentForApiContract.from_dict(body)
    return web.Response(status=200)


async def api_song_lists_list_id_songs_get(request: web.Request, list_id, query=None, song_types=None, pv_services=None, tag_id=None, artist_id=None, child_voicebanks=None, advanced_filters=None, start=None, max_results=None, get_total_count=None, sort=None, name_match_mode=None, fields=None, lang=None) -> web.Response:
    """api_song_lists_list_id_songs_get

    

    :param list_id: 
    :type list_id: int
    :param query: 
    :type query: str
    :param song_types: 
    :type song_types: str
    :param pv_services: 
    :type pv_services: dict | bytes
    :param tag_id: 
    :type tag_id: List[int]
    :param artist_id: 
    :type artist_id: List[int]
    :param child_voicebanks: 
    :type child_voicebanks: bool
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
    :param name_match_mode: 
    :type name_match_mode: dict | bytes
    :param fields: 
    :type fields: dict | bytes
    :param lang: 
    :type lang: dict | bytes

    """
    pv_services = .from_dict(pv_services)
    advanced_filters = [AdvancedSearchFilterParams.from_dict(d) for d in advanced_filters]
    sort = .from_dict(sort)
    name_match_mode = .from_dict(name_match_mode)
    fields = .from_dict(fields)
    lang = .from_dict(lang)
    return web.Response(status=200)


async def api_song_lists_post(request: web.Request, body=None) -> web.Response:
    """api_song_lists_post

    

    :param body: 
    :type body: dict | bytes

    """
    body = SongListForEditForApiContract.from_dict(body)
    return web.Response(status=200)
