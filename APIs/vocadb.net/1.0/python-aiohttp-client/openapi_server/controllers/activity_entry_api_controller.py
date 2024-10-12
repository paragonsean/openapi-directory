from typing import List, Dict
from aiohttp import web

from openapi_server.models.activity_entry_for_api_contract_partial_find_result import ActivityEntryForApiContractPartialFindResult
from openapi_server.models.activity_entry_optional_fields import ActivityEntryOptionalFields
from openapi_server.models.activity_entry_sort_rule import ActivityEntrySortRule
from openapi_server.models.content_language_preference import ContentLanguagePreference
from openapi_server.models.entry_edit_event import EntryEditEvent
from openapi_server.models.entry_optional_fields import EntryOptionalFields
from openapi_server.models.entry_type import EntryType
from openapi_server import util


async def api_activity_entries_get(request: web.Request, before=None, since=None, user_id=None, edit_event=None, entry_type=None, max_results=None, get_total_count=None, fields=None, entry_fields=None, lang=None, sort_rule=None) -> web.Response:
    """api_activity_entries_get

    

    :param before: 
    :type before: str
    :param since: 
    :type since: str
    :param user_id: 
    :type user_id: int
    :param edit_event: 
    :type edit_event: dict | bytes
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
    edit_event = .from_dict(edit_event)
    entry_type = .from_dict(entry_type)
    fields = .from_dict(fields)
    entry_fields = .from_dict(entry_fields)
    lang = .from_dict(lang)
    sort_rule = .from_dict(sort_rule)
    return web.Response(status=200)
