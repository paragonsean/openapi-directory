from typing import List, Dict
from aiohttp import web

from openapi_server.models.comment_for_api_contract import CommentForApiContract
from openapi_server.models.comment_for_api_contract_partial_find_result import CommentForApiContractPartialFindResult
from openapi_server.models.comment_optional_fields import CommentOptionalFields
from openapi_server.models.comment_sort_rule import CommentSortRule
from openapi_server.models.content_language_preference import ContentLanguagePreference
from openapi_server.models.entry_optional_fields import EntryOptionalFields
from openapi_server.models.entry_type import EntryType
from openapi_server import util


async def api_comments_entry_type_comments_comment_id_delete(request: web.Request, entry_type, comment_id) -> web.Response:
    """api_comments_entry_type_comments_comment_id_delete

    

    :param entry_type: 
    :type entry_type: dict | bytes
    :param comment_id: 
    :type comment_id: int

    """
    entry_type = .from_dict(entry_type)
    return web.Response(status=200)


async def api_comments_entry_type_comments_comment_id_post(request: web.Request, entry_type, comment_id, body=None) -> web.Response:
    """api_comments_entry_type_comments_comment_id_post

    

    :param entry_type: 
    :type entry_type: dict | bytes
    :param comment_id: 
    :type comment_id: int
    :param body: 
    :type body: dict | bytes

    """
    entry_type = .from_dict(entry_type)
    body = CommentForApiContract.from_dict(body)
    return web.Response(status=200)


async def api_comments_entry_type_comments_get(request: web.Request, entry_type, entry_id=None) -> web.Response:
    """api_comments_entry_type_comments_get

    

    :param entry_type: 
    :type entry_type: dict | bytes
    :param entry_id: 
    :type entry_id: int

    """
    entry_type = .from_dict(entry_type)
    return web.Response(status=200)


async def api_comments_entry_type_comments_post(request: web.Request, entry_type, body=None) -> web.Response:
    """api_comments_entry_type_comments_post

    

    :param entry_type: 
    :type entry_type: dict | bytes
    :param body: 
    :type body: dict | bytes

    """
    entry_type = .from_dict(entry_type)
    body = CommentForApiContract.from_dict(body)
    return web.Response(status=200)


async def api_comments_get(request: web.Request, before=None, since=None, user_id=None, entry_type=None, max_results=None, get_total_count=None, fields=None, entry_fields=None, lang=None, sort_rule=None) -> web.Response:
    """api_comments_get

    

    :param before: 
    :type before: str
    :param since: 
    :type since: str
    :param user_id: 
    :type user_id: int
    :param entry_type: 
    :type entry_type: dict | bytes
    :param max_results: 
    :type max_results: int
    :param get_total_count: 
    :type get_total_count: bool
    :param fields: 
    :type fields: dict | bytes
    :param entry_fields: 
    :type entry_fields: dict | bytes
    :param lang: 
    :type lang: dict | bytes
    :param sort_rule: 
    :type sort_rule: dict | bytes

    """
    before = util.deserialize_datetime(before)
    since = util.deserialize_datetime(since)
    entry_type = .from_dict(entry_type)
    fields = .from_dict(fields)
    entry_fields = .from_dict(entry_fields)
    lang = .from_dict(lang)
    sort_rule = .from_dict(sort_rule)
    return web.Response(status=200)
