from typing import List, Dict
from aiohttp import web

from openapi_server.models.advanced_search_filter_params import AdvancedSearchFilterParams
from openapi_server.models.artist_for_api_contract import ArtistForApiContract
from openapi_server.models.artist_for_api_contract_partial_find_result import ArtistForApiContractPartialFindResult
from openapi_server.models.artist_optional_fields import ArtistOptionalFields
from openapi_server.models.artist_relations_fields import ArtistRelationsFields
from openapi_server.models.artist_sort_rule import ArtistSortRule
from openapi_server.models.comment_for_api_contract import CommentForApiContract
from openapi_server.models.content_language_preference import ContentLanguagePreference
from openapi_server.models.entry_status import EntryStatus
from openapi_server.models.name_match_mode import NameMatchMode
from openapi_server import util


async def api_artists_comments_comment_id_delete(request: web.Request, comment_id) -> web.Response:
    """api_artists_comments_comment_id_delete

    

    :param comment_id: 
    :type comment_id: int

    """
    return web.Response(status=200)


async def api_artists_comments_comment_id_post(request: web.Request, comment_id, body=None) -> web.Response:
    """api_artists_comments_comment_id_post

    

    :param comment_id: 
    :type comment_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = CommentForApiContract.from_dict(body)
    return web.Response(status=200)


async def api_artists_get(request: web.Request, query=None, artist_types=None, allow_base_voicebanks=None, tag_name=None, tag_id=None, child_tags=None, followed_by_user_id=None, status=None, advanced_filters=None, start=None, max_results=None, get_total_count=None, sort=None, prefer_accurate_matches=None, name_match_mode=None, fields=None, lang=None) -> web.Response:
    """api_artists_get

    

    :param query: 
    :type query: str
    :param artist_types: 
    :type artist_types: str
    :param allow_base_voicebanks: 
    :type allow_base_voicebanks: bool
    :param tag_name: 
    :type tag_name: List[str]
    :param tag_id: 
    :type tag_id: List[int]
    :param child_tags: 
    :type child_tags: bool
    :param followed_by_user_id: 
    :type followed_by_user_id: int
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

    """
    status = .from_dict(status)
    advanced_filters = [AdvancedSearchFilterParams.from_dict(d) for d in advanced_filters]
    sort = .from_dict(sort)
    name_match_mode = .from_dict(name_match_mode)
    fields = .from_dict(fields)
    lang = .from_dict(lang)
    return web.Response(status=200)


async def api_artists_id_comments_get(request: web.Request, id) -> web.Response:
    """api_artists_id_comments_get

    

    :param id: 
    :type id: int

    """
    return web.Response(status=200)


async def api_artists_id_comments_post(request: web.Request, id, body=None) -> web.Response:
    """api_artists_id_comments_post

    

    :param id: 
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = CommentForApiContract.from_dict(body)
    return web.Response(status=200)


async def api_artists_id_delete(request: web.Request, id, notes=None) -> web.Response:
    """api_artists_id_delete

    

    :param id: 
    :type id: int
    :param notes: 
    :type notes: str

    """
    return web.Response(status=200)


async def api_artists_id_get(request: web.Request, id, fields=None, relations=None, lang=None) -> web.Response:
    """api_artists_id_get

    

    :param id: 
    :type id: int
    :param fields: 
    :type fields: dict | bytes
    :param relations: 
    :type relations: dict | bytes
    :param lang: 
    :type lang: dict | bytes

    """
    fields = .from_dict(fields)
    relations = .from_dict(relations)
    lang = .from_dict(lang)
    return web.Response(status=200)


async def api_artists_names_get(request: web.Request, query=None, name_match_mode=None, max_results=None) -> web.Response:
    """api_artists_names_get

    

    :param query: 
    :type query: str
    :param name_match_mode: 
    :type name_match_mode: dict | bytes
    :param max_results: 
    :type max_results: int

    """
    name_match_mode = .from_dict(name_match_mode)
    return web.Response(status=200)
