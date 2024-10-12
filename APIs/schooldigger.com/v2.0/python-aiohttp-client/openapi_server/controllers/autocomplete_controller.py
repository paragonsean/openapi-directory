from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_autocomplete_school_result import APIAutocompleteSchoolResult
from openapi_server import util


async def autocomplete_get_schools(request: web.Request, app_id, app_key, q=None, q_search_city_state_name=None, st=None, level=None, box_latitude_nw=None, box_longitude_nw=None, box_latitude_se=None, box_longitude_se=None, return_count=None) -> web.Response:
    """Returns a simple and quick list of schools for use in a client-typed autocomplete

    

    :param app_id: Your API app id
    :type app_id: str
    :param app_key: Your API app key
    :type app_key: str
    :param q: Search term for autocomplete (e.g. &#39;Lincol&#39;) (required)
    :type q: str
    :param q_search_city_state_name: Extend the search term to include city and state (e.g. &#39;Lincoln el paso&#39; matches Lincoln Middle School in El Paso) (optional)
    :type q_search_city_state_name: bool
    :param st: Two character state (e.g. &#39;CA&#39;) (optional -- leave blank to search entire U.S.)
    :type st: str
    :param level: Search for schools at this level only. Valid values: &#39;Elementary&#39;, &#39;Middle&#39;, &#39;High&#39;, &#39;Alt&#39;, &#39;Private&#39; (optional - leave blank to search for all schools)
    :type level: str
    :param box_latitude_nw: Search within a &#39;box&#39; defined by (BoxLatitudeNW/BoxLongitudeNW) to (BoxLongitudeSE/BoxLatitudeSE) (optional. Pro, Enterprise API levels only.)
    :type box_latitude_nw: float
    :param box_longitude_nw: Search within a &#39;box&#39; defined by (BoxLatitudeNW/BoxLongitudeNW) to (BoxLongitudeSE/BoxLatitudeSE) (optional. Pro, Enterprise API levels only.)
    :type box_longitude_nw: float
    :param box_latitude_se: Search within a &#39;box&#39; defined by (BoxLatitudeNW/BoxLongitudeNW) to (BoxLongitudeSE/BoxLatitudeSE) (optional. Pro, Enterprise API levels only.)
    :type box_latitude_se: float
    :param box_longitude_se: Search within a &#39;box&#39; defined by (BoxLatitudeNW/BoxLongitudeNW) to (BoxLongitudeSE/BoxLatitudeSE) (optional. Pro, Enterprise API levels only.)
    :type box_longitude_se: float
    :param return_count: Number of schools to return. Valid values: 1-20. (default: 10)
    :type return_count: int

    """
    return web.Response(status=200)
