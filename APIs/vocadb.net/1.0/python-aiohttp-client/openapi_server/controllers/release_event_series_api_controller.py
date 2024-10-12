from typing import List, Dict
from aiohttp import web

from openapi_server.models.content_language_preference import ContentLanguagePreference
from openapi_server.models.name_match_mode import NameMatchMode
from openapi_server.models.release_event_series_for_api_contract import ReleaseEventSeriesForApiContract
from openapi_server.models.release_event_series_for_api_contract_partial_find_result import ReleaseEventSeriesForApiContractPartialFindResult
from openapi_server.models.release_event_series_for_edit_for_api_contract import ReleaseEventSeriesForEditForApiContract
from openapi_server.models.release_event_series_optional_fields import ReleaseEventSeriesOptionalFields
from openapi_server import util


async def api_release_event_series_get(request: web.Request, query=None, fields=None, start=None, max_results=None, get_total_count=None, name_match_mode=None, lang=None) -> web.Response:
    """api_release_event_series_get

    

    :param query: 
    :type query: str
    :param fields: 
    :type fields: dict | bytes
    :param start: 
    :type start: int
    :param max_results: 
    :type max_results: int
    :param get_total_count: 
    :type get_total_count: bool
    :param name_match_mode: 
    :type name_match_mode: dict | bytes
    :param lang: 
    :type lang: dict | bytes

    """
    fields = .from_dict(fields)
    name_match_mode = .from_dict(name_match_mode)
    lang = .from_dict(lang)
    return web.Response(status=200)


async def api_release_event_series_id_delete(request: web.Request, id, notes=None, hard_delete=None) -> web.Response:
    """api_release_event_series_id_delete

    

    :param id: 
    :type id: int
    :param notes: 
    :type notes: str
    :param hard_delete: 
    :type hard_delete: bool

    """
    return web.Response(status=200)


async def api_release_event_series_id_for_edit_get(request: web.Request, id) -> web.Response:
    """api_release_event_series_id_for_edit_get

    

    :param id: 
    :type id: int

    """
    return web.Response(status=200)


async def api_release_event_series_id_get(request: web.Request, id, fields=None, lang=None) -> web.Response:
    """api_release_event_series_id_get

    

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
