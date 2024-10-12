from typing import List, Dict
from aiohttp import web

from openapi_server.models.content_language_preference import ContentLanguagePreference
from openapi_server.models.distance_unit import DistanceUnit
from openapi_server.models.name_match_mode import NameMatchMode
from openapi_server.models.venue_for_api_contract_partial_find_result import VenueForApiContractPartialFindResult
from openapi_server.models.venue_optional_fields import VenueOptionalFields
from openapi_server.models.venue_report_type import VenueReportType
from openapi_server.models.venue_sort_rule import VenueSortRule
from openapi_server import util


async def api_venues_get(request: web.Request, query=None, fields=None, start=None, max_results=None, get_total_count=None, name_match_mode=None, lang=None, sort_rule=None, latitude=None, longitude=None, radius=None, distance_unit=None) -> web.Response:
    """api_venues_get

    

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
    :param sort_rule: 
    :type sort_rule: dict | bytes
    :param latitude: 
    :type latitude: float
    :param longitude: 
    :type longitude: float
    :param radius: 
    :type radius: float
    :param distance_unit: 
    :type distance_unit: dict | bytes

    """
    fields = .from_dict(fields)
    name_match_mode = .from_dict(name_match_mode)
    lang = .from_dict(lang)
    sort_rule = .from_dict(sort_rule)
    distance_unit = .from_dict(distance_unit)
    return web.Response(status=200)


async def api_venues_id_delete(request: web.Request, id, notes=None, hard_delete=None) -> web.Response:
    """api_venues_id_delete

    

    :param id: 
    :type id: int
    :param notes: 
    :type notes: str
    :param hard_delete: 
    :type hard_delete: bool

    """
    return web.Response(status=200)


async def api_venues_id_reports_post(request: web.Request, id, report_type=None, notes=None, version_number=None) -> web.Response:
    """api_venues_id_reports_post

    

    :param id: 
    :type id: int
    :param report_type: 
    :type report_type: dict | bytes
    :param notes: 
    :type notes: str
    :param version_number: 
    :type version_number: int

    """
    report_type = .from_dict(report_type)
    return web.Response(status=200)
