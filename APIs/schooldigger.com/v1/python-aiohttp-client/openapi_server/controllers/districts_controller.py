from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_district import APIDistrict
from openapi_server.models.api_district_list import APIDistrictList
from openapi_server import util


async def districts_get_all_districts(request: web.Request, st, app_id, app_key, q=None, city=None, zip=None, near_latitude=None, near_longitude=None, boundary_address=None, distance_miles=None, is_in_boundary_only=None, box_latitude_nw=None, box_longitude_nw=None, box_latitude_se=None, box_longitude_se=None, page=None, per_page=None, sort_by=None, include_unranked_districts_in_rank_sort=None) -> web.Response:
    """Returns a list of districts

    Search the SchoolDigger database for districts. You may use any combination of criteria as query parameters.

    :param st: Two character state (e.g. &#39;CA&#39;) - required
    :type st: str
    :param app_id: Your API app id
    :type app_id: str
    :param app_key: Your API app key
    :type app_key: str
    :param q: Search term - note: will match district name or city (optional)
    :type q: str
    :param city: Search for districts in this city (optional)
    :type city: str
    :param zip: Search for districts in this 5-digit zip code (optional)
    :type zip: str
    :param near_latitude: Search for districts within (distanceMiles) of (nearLatitude)/(nearLongitude) (e.g. 44.982560) (optional) (Pro, Enterprise API levels only. Enterprise API level will flag districts that include lat/long in its attendance boundary.)
    :type near_latitude: float
    :param near_longitude: Search for districts within (distanceMiles) of (nearLatitude)/(nearLongitude) (e.g. -124.289185) (optional) (Pro, Enterprise API levels only. Enterprise API level will flag districts that include lat/long in its attendance boundary.)
    :type near_longitude: float
    :param boundary_address: Full U.S. address: flag returned districts that include this address in its attendance boundary. Example: &#39;123 Main St. AnyTown CA 90001&#39; (optional) (Enterprise API level only)
    :type boundary_address: str
    :param distance_miles: Search for districts within (distanceMiles) of (nearLatitude)/(nearLongitude) (Default 50 miles) (optional) (Pro, Enterprise API levels only)
    :type distance_miles: int
    :param is_in_boundary_only: Return only the districts that include given location (nearLatitude/nearLongitude) or (boundaryAddress) in its attendance boundary (Enterprise API level only)
    :type is_in_boundary_only: bool
    :param box_latitude_nw: Search for districts within a &#39;box&#39; defined by (BoxLatitudeNW/BoxLongitudeNW) to (BoxLongitudeSE/BoxLatitudeSE) (optional)
    :type box_latitude_nw: float
    :param box_longitude_nw: Search for districts within a &#39;box&#39; defined by (BoxLatitudeNW/BoxLongitudeNW) to (BoxLongitudeSE/BoxLatitudeSE) (optional)
    :type box_longitude_nw: float
    :param box_latitude_se: Search for districts within a &#39;box&#39; defined by (BoxLatitudeNW/BoxLongitudeNW) to (BoxLongitudeSE/BoxLatitudeSE) (optional)
    :type box_latitude_se: float
    :param box_longitude_se: Search for districts within a &#39;box&#39; defined by (BoxLatitudeNW/BoxLongitudeNW) to (BoxLongitudeSE/BoxLatitudeSE) (optional)
    :type box_longitude_se: float
    :param page: Page number to retrieve (optional, default: 1)
    :type page: int
    :param per_page: Number of districts to retrieve on a page (50 max) (optional, default: 10)
    :type per_page: int
    :param sort_by: Sort list. Values are: districtname, distance, rank. For descending order, precede with &#39;-&#39; i.e. -districtname (optional, default: districtname)
    :type sort_by: str
    :param include_unranked_districts_in_rank_sort: If sortBy is &#39;rank&#39;, this boolean determines if districts with no rank are included in the result (optional, default: false)
    :type include_unranked_districts_in_rank_sort: bool

    """
    return web.Response(status=200)


async def districts_get_district(request: web.Request, id, app_id, app_key) -> web.Response:
    """Returns a detailed record for one district

    Retrieve a single district record from the SchoolDigger database

    :param id: The 7 digit District ID (e.g. 0642150)
    :type id: str
    :param app_id: Your API app id
    :type app_id: str
    :param app_key: Your API app key
    :type app_key: str

    """
    return web.Response(status=200)
