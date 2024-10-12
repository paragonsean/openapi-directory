from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_school10_full import APISchool10Full
from openapi_server.models.api_school_list import APISchoolList
from openapi_server import util


async def schools_get_all_schools(request: web.Request, st, app_id, app_key, q=None, q_search_school_name_only=None, district_id=None, level=None, city=None, zip=None, is_magnet=None, is_charter=None, is_virtual=None, is_title_i=None, is_title_i_schoolwide=None, near_latitude=None, near_longitude=None, boundary_address=None, distance_miles=None, is_in_boundary_only=None, box_latitude_nw=None, box_longitude_nw=None, box_latitude_se=None, box_longitude_se=None, page=None, per_page=None, sort_by=None, include_unranked_schools_in_rank_sort=None) -> web.Response:
    """Returns a list of schools

    Search the SchoolDigger database for schools. You may use any combination of criteria as query parameters.

    :param st: Two character state (e.g. &#39;CA&#39;) - required
    :type st: str
    :param app_id: Your API app id
    :type app_id: str
    :param app_key: Your API app key
    :type app_key: str
    :param q: Search term - note: will match school name or city (optional)
    :type q: str
    :param q_search_school_name_only: For parameter &#39;q&#39;, only search school names instead of school and city (optional)
    :type q_search_school_name_only: bool
    :param district_id: Search for schools within this district (7 digit district id) (optional)
    :type district_id: str
    :param level: Search for schools at this level. Valid values: &#39;Elementary&#39;, &#39;Middle&#39;, &#39;High&#39;, &#39;Alt&#39;, &#39;Public&#39;, &#39;Private&#39; (optional). &#39;Public&#39; returns all Elementary, Middle, High and Alternative schools
    :type level: str
    :param city: Search for schools in this city (optional)
    :type city: str
    :param zip: Search for schools in this 5-digit zip code (optional)
    :type zip: str
    :param is_magnet: True &#x3D; return only magnet schools, False &#x3D; return only non-magnet schools (optional) (Pro, Enterprise API levels only)
    :type is_magnet: bool
    :param is_charter: True &#x3D; return only charter schools, False &#x3D; return only non-charter schools (optional) (Pro, Enterprise API levels only)
    :type is_charter: bool
    :param is_virtual: True &#x3D; return only virtual schools, False &#x3D; return only non-virtual schools (optional) (Pro, Enterprise API levels only)
    :type is_virtual: bool
    :param is_title_i: True &#x3D; return only Title I schools, False &#x3D; return only non-Title I schools (optional) (Pro, Enterprise API levels only)
    :type is_title_i: bool
    :param is_title_i_schoolwide: True &#x3D; return only Title I school-wide schools, False &#x3D; return only non-Title I school-wide schools (optional) (Pro, Enterprise API levels only)
    :type is_title_i_schoolwide: bool
    :param near_latitude: Search for schools within (distanceMiles) of (nearLatitude)/(nearLongitude) (e.g. 44.982560) (optional) (Pro, Enterprise API levels only. Enterprise API level will flag schools that include lat/long in its attendance boundary.)
    :type near_latitude: float
    :param near_longitude: Search for schools within (distanceMiles) of (nearLatitude)/(nearLongitude) (e.g. -124.289185) (optional) (Pro, Enterprise API levels only. Enterprise API level will flag schools that include lat/long in its attendance boundary.)
    :type near_longitude: float
    :param boundary_address: Full U.S. address: flag returned schools that include this address in its attendance boundary. Example: &#39;123 Main St. AnyTown CA 90001&#39; (optional) (Enterprise API level only) IMPORTANT NOTE: If you have the lat/long of the address, use nearLatitude and nearLongitude instead for much faster response times
    :type boundary_address: str
    :param distance_miles: Search for schools within (distanceMiles) of (nearLatitude)/(nearLongitude) (Default 5 miles) (optional) (Pro, Enterprise API levels only)
    :type distance_miles: int
    :param is_in_boundary_only: Return only the schools that include given location (nearLatitude/nearLongitude) or (boundaryAddress) in its attendance boundary (Enterprise API level only)
    :type is_in_boundary_only: bool
    :param box_latitude_nw: Search for schools within a &#39;box&#39; defined by (boxLatitudeNW/boxLongitudeNW) to (boxLongitudeSE/boxLatitudeSE) (optional)
    :type box_latitude_nw: float
    :param box_longitude_nw: Search for schools within a &#39;box&#39; defined by (boxLatitudeNW/boxLongitudeNW) to (boxLongitudeSE/boxLatitudeSE) (optional)
    :type box_longitude_nw: float
    :param box_latitude_se: Search for schools within a &#39;box&#39; defined by (boxLatitudeNW/boxLongitudeNW) to (boxLongitudeSE/boxLatitudeSE) (optional)
    :type box_latitude_se: float
    :param box_longitude_se: Search for schools within a &#39;box&#39; defined by (boxLatitudeNW/boxLongitudeNW) to (boxLongitudeSE/boxLatitudeSE) (optional)
    :type box_longitude_se: float
    :param page: Page number to retrieve (optional, default: 1)
    :type page: int
    :param per_page: Number of schools to retrieve on a page (50 max) (optional, default: 10)
    :type per_page: int
    :param sort_by: Sort list. Values are: schoolname, distance, rank. For descending order, precede with &#39;-&#39; i.e. -schoolname (optional, default: schoolname)
    :type sort_by: str
    :param include_unranked_schools_in_rank_sort: If sortBy is &#39;rank&#39;, this boolean determines if schools with no rank are included in the result (optional, default: false)
    :type include_unranked_schools_in_rank_sort: bool

    """
    return web.Response(status=200)


async def schools_get_school10(request: web.Request, id, app_id, app_key) -> web.Response:
    """Returns a detailed record for one school

    Retrieve a school record from the SchoolDigger database

    :param id: The 12 digit School ID (e.g. 064215006903)
    :type id: str
    :param app_id: Your API app id
    :type app_id: str
    :param app_key: Your API app key
    :type app_key: str

    """
    return web.Response(status=200)
