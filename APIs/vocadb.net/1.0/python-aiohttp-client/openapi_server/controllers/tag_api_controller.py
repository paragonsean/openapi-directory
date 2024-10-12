from typing import List, Dict
from aiohttp import web

from openapi_server.models.comment_for_api_contract import CommentForApiContract
from openapi_server.models.comment_for_api_contract_partial_find_result import CommentForApiContractPartialFindResult
from openapi_server.models.content_language_preference import ContentLanguagePreference
from openapi_server.models.entry_type import EntryType
from openapi_server.models.name_match_mode import NameMatchMode
from openapi_server.models.tag_base_contract import TagBaseContract
from openapi_server.models.tag_for_api_contract import TagForApiContract
from openapi_server.models.tag_for_api_contract_partial_find_result import TagForApiContractPartialFindResult
from openapi_server.models.tag_optional_fields import TagOptionalFields
from openapi_server.models.tag_report_type import TagReportType
from openapi_server.models.tag_sort_rule import TagSortRule
from openapi_server.models.tag_target_types import TagTargetTypes
from openapi_server import util


async def api_tags_by_name_name_get(request: web.Request, name, fields=None, lang=None) -> web.Response:
    """api_tags_by_name_name_get

    

    :param name: 
    :type name: str
    :param fields: 
    :type fields: dict | bytes
    :param lang: 
    :type lang: dict | bytes

    """
    fields = .from_dict(fields)
    lang = .from_dict(lang)
    return web.Response(status=200)


async def api_tags_category_names_get(request: web.Request, query=None, name_match_mode=None) -> web.Response:
    """api_tags_category_names_get

    

    :param query: 
    :type query: str
    :param name_match_mode: 
    :type name_match_mode: dict | bytes

    """
    name_match_mode = .from_dict(name_match_mode)
    return web.Response(status=200)


async def api_tags_comments_comment_id_delete(request: web.Request, comment_id) -> web.Response:
    """api_tags_comments_comment_id_delete

    

    :param comment_id: 
    :type comment_id: int

    """
    return web.Response(status=200)


async def api_tags_comments_comment_id_post(request: web.Request, comment_id, body=None) -> web.Response:
    """api_tags_comments_comment_id_post

    

    :param comment_id: 
    :type comment_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = CommentForApiContract.from_dict(body)
    return web.Response(status=200)


async def api_tags_get(request: web.Request, query=None, allow_children=None, category_name=None, start=None, max_results=None, get_total_count=None, name_match_mode=None, sort=None, prefer_accurate_matches=None, fields=None, lang=None, target=None) -> web.Response:
    """api_tags_get

    

    :param query: 
    :type query: str
    :param allow_children: 
    :type allow_children: bool
    :param category_name: 
    :type category_name: str
    :param start: 
    :type start: int
    :param max_results: 
    :type max_results: int
    :param get_total_count: 
    :type get_total_count: bool
    :param name_match_mode: 
    :type name_match_mode: dict | bytes
    :param sort: 
    :type sort: dict | bytes
    :param prefer_accurate_matches: 
    :type prefer_accurate_matches: bool
    :param fields: 
    :type fields: dict | bytes
    :param lang: 
    :type lang: dict | bytes
    :param target: 
    :type target: dict | bytes

    """
    name_match_mode = .from_dict(name_match_mode)
    sort = .from_dict(sort)
    fields = .from_dict(fields)
    lang = .from_dict(lang)
    target = .from_dict(target)
    return web.Response(status=200)


async def api_tags_id_delete(request: web.Request, id, notes=None, hard_delete=None) -> web.Response:
    """api_tags_id_delete

    

    :param id: 
    :type id: int
    :param notes: 
    :type notes: str
    :param hard_delete: 
    :type hard_delete: bool

    """
    return web.Response(status=200)


async def api_tags_id_get(request: web.Request, id, fields=None, lang=None) -> web.Response:
    """api_tags_id_get

    

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


async def api_tags_names_get(request: web.Request, query=None, allow_aliases=None, max_results=None) -> web.Response:
    """api_tags_names_get

    

    :param query: 
    :type query: str
    :param allow_aliases: 
    :type allow_aliases: bool
    :param max_results: 
    :type max_results: int

    """
    return web.Response(status=200)


async def api_tags_post(request: web.Request, name=None) -> web.Response:
    """api_tags_post

    

    :param name: 
    :type name: str

    """
    return web.Response(status=200)


async def api_tags_tag_id_children_get(request: web.Request, tag_id, fields=None, lang=None) -> web.Response:
    """api_tags_tag_id_children_get

    

    :param tag_id: 
    :type tag_id: int
    :param fields: 
    :type fields: dict | bytes
    :param lang: 
    :type lang: dict | bytes

    """
    fields = .from_dict(fields)
    lang = .from_dict(lang)
    return web.Response(status=200)


async def api_tags_tag_id_comments_get(request: web.Request, tag_id) -> web.Response:
    """api_tags_tag_id_comments_get

    

    :param tag_id: 
    :type tag_id: int

    """
    return web.Response(status=200)


async def api_tags_tag_id_comments_post(request: web.Request, tag_id, body=None) -> web.Response:
    """api_tags_tag_id_comments_post

    

    :param tag_id: 
    :type tag_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = CommentForApiContract.from_dict(body)
    return web.Response(status=200)


async def api_tags_tag_id_reports_post(request: web.Request, tag_id, report_type=None, notes=None, version_number=None) -> web.Response:
    """api_tags_tag_id_reports_post

    

    :param tag_id: 
    :type tag_id: int
    :param report_type: 
    :type report_type: dict | bytes
    :param notes: 
    :type notes: str
    :param version_number: 
    :type version_number: int

    """
    report_type = .from_dict(report_type)
    return web.Response(status=200)


async def api_tags_top_get(request: web.Request, category_name=None, entry_type=None, max_results=None, lang=None) -> web.Response:
    """api_tags_top_get

    

    :param category_name: 
    :type category_name: str
    :param entry_type: 
    :type entry_type: dict | bytes
    :param max_results: 
    :type max_results: int
    :param lang: 
    :type lang: dict | bytes

    """
    entry_type = .from_dict(entry_type)
    lang = .from_dict(lang)
    return web.Response(status=200)
