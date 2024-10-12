from typing import List, Dict
from aiohttp import web

from openapi_server.models.album_for_api_contract import AlbumForApiContract
from openapi_server.models.album_optional_fields import AlbumOptionalFields
from openapi_server.models.content_language_preference import ContentLanguagePreference
from openapi_server.models.entry_status import EntryStatus
from openapi_server.models.event_category import EventCategory
from openapi_server.models.event_report_type import EventReportType
from openapi_server.models.event_sort_rule import EventSortRule
from openapi_server.models.name_match_mode import NameMatchMode
from openapi_server.models.release_event_for_api_contract import ReleaseEventForApiContract
from openapi_server.models.release_event_for_api_contract_partial_find_result import ReleaseEventForApiContractPartialFindResult
from openapi_server.models.release_event_optional_fields import ReleaseEventOptionalFields
from openapi_server.models.song_for_api_contract import SongForApiContract
from openapi_server.models.song_optional_fields import SongOptionalFields
from openapi_server.models.sort_direction import SortDirection
from openapi_server import util


async def api_release_events_event_id_albums_get(request: web.Request, event_id, fields=None, lang=None) -> web.Response:
    """api_release_events_event_id_albums_get

    

    :param event_id: 
    :type event_id: int
    :param fields: 
    :type fields: dict | bytes
    :param lang: 
    :type lang: dict | bytes

    """
    fields = .from_dict(fields)
    lang = .from_dict(lang)
    return web.Response(status=200)


async def api_release_events_event_id_published_songs_get(request: web.Request, event_id, fields=None, lang=None) -> web.Response:
    """api_release_events_event_id_published_songs_get

    

    :param event_id: 
    :type event_id: int
    :param fields: 
    :type fields: dict | bytes
    :param lang: 
    :type lang: dict | bytes

    """
    fields = .from_dict(fields)
    lang = .from_dict(lang)
    return web.Response(status=200)


async def api_release_events_event_id_reports_post(request: web.Request, event_id, report_type=None, notes=None, version_number=None) -> web.Response:
    """api_release_events_event_id_reports_post

    

    :param event_id: 
    :type event_id: int
    :param report_type: 
    :type report_type: dict | bytes
    :param notes: 
    :type notes: str
    :param version_number: 
    :type version_number: int

    """
    report_type = .from_dict(report_type)
    return web.Response(status=200)


async def api_release_events_get(request: web.Request, query=None, name_match_mode=None, series_id=None, after_date=None, before_date=None, category=None, user_collection_id=None, tag_id=None, child_tags=None, artist_id=None, child_voicebanks=None, include_members=None, status=None, start=None, max_results=None, get_total_count=None, sort=None, fields=None, lang=None, sort_direction=None) -> web.Response:
    """api_release_events_get

    

    :param query: 
    :type query: str
    :param name_match_mode: 
    :type name_match_mode: dict | bytes
    :param series_id: 
    :type series_id: int
    :param after_date: 
    :type after_date: str
    :param before_date: 
    :type before_date: str
    :param category: 
    :type category: dict | bytes
    :param user_collection_id: 
    :type user_collection_id: int
    :param tag_id: 
    :type tag_id: List[int]
    :param child_tags: 
    :type child_tags: bool
    :param artist_id: 
    :type artist_id: List[int]
    :param child_voicebanks: 
    :type child_voicebanks: bool
    :param include_members: 
    :type include_members: bool
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
    :param fields: 
    :type fields: dict | bytes
    :param lang: 
    :type lang: dict | bytes
    :param sort_direction: 
    :type sort_direction: dict | bytes

    """
    name_match_mode = .from_dict(name_match_mode)
    after_date = util.deserialize_datetime(after_date)
    before_date = util.deserialize_datetime(before_date)
    category = .from_dict(category)
    status = .from_dict(status)
    sort = .from_dict(sort)
    fields = .from_dict(fields)
    lang = .from_dict(lang)
    sort_direction = .from_dict(sort_direction)
    return web.Response(status=200)


async def api_release_events_id_delete(request: web.Request, id, notes=None, hard_delete=None) -> web.Response:
    """api_release_events_id_delete

    

    :param id: 
    :type id: int
    :param notes: 
    :type notes: str
    :param hard_delete: 
    :type hard_delete: bool

    """
    return web.Response(status=200)


async def api_release_events_id_get(request: web.Request, id, fields=None, lang=None) -> web.Response:
    """api_release_events_id_get

    

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


async def api_release_events_names_get(request: web.Request, query=None, max_results=None) -> web.Response:
    """api_release_events_names_get

    

    :param query: 
    :type query: str
    :param max_results: 
    :type max_results: int

    """
    return web.Response(status=200)
