from typing import List, Dict
from aiohttp import web

from openapi_server.models.content_language_preference import ContentLanguagePreference
from openapi_server.models.entry_for_api_contract_partial_find_result import EntryForApiContractPartialFindResult
from openapi_server.models.entry_optional_fields import EntryOptionalFields
from openapi_server.models.entry_sort_rule import EntrySortRule
from openapi_server.models.entry_status import EntryStatus
from openapi_server.models.entry_types import EntryTypes
from openapi_server.models.name_match_mode import NameMatchMode
from openapi_server import util


async def api_entries_get(request: web.Request, query=None, tag_name=None, tag_id=None, child_tags=None, entry_types=None, status=None, start=None, max_results=None, get_total_count=None, sort=None, name_match_mode=None, fields=None, lang=None) -> web.Response:
    """api_entries_get

    

    :param query: 
    :type query: str
    :param tag_name: 
    :type tag_name: List[str]
    :param tag_id: 
    :type tag_id: List[int]
    :param child_tags: 
    :type child_tags: bool
    :param entry_types: 
    :type entry_types: dict | bytes
    :param status: 
    :type status: dict | bytes
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
    entry_types = .from_dict(entry_types)
    status = .from_dict(status)
    sort = .from_dict(sort)
    name_match_mode = .from_dict(name_match_mode)
    fields = .from_dict(fields)
    lang = .from_dict(lang)
    return web.Response(status=200)


async def api_entries_names_get(request: web.Request, query=None, name_match_mode=None, max_results=None) -> web.Response:
    """api_entries_names_get

    

    :param query: 
    :type query: str
    :param name_match_mode: 
    :type name_match_mode: dict | bytes
    :param max_results: 
    :type max_results: int

    """
    name_match_mode = .from_dict(name_match_mode)
    return web.Response(status=200)
