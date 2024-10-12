from typing import List, Dict
from aiohttp import web

from openapi_server.models.tenancy_model import TenancyModel
from openapi_server.models.tenancy_model_results import TenancyModelResults
from openapi_server import util


async def lettings_controller_get_advertised(request: web.Request, short_name, branch_id, offset, count, area_id=None, rent_minimum=None, rent_maximum=None, maximum_tenants=None, want_shared_properties=None, want_student_properties=None) -> web.Response:
    """Search all properties available for rent given a range of search criteria.

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param branch_id: The unique ID of the Branch
    :type branch_id: str
    :param offset: The index of the first item to return
    :type offset: int
    :param count: The maximum number of items to return (up to 1000 per request)
    :type count: int
    :param area_id: The unique ID of the Area
    :type area_id: str
    :param rent_minimum: The minimum advertised rent to search for
    :type rent_minimum: float
    :param rent_maximum: The maximum advertised rent to search for
    :type rent_maximum: float
    :param maximum_tenants: The maximum number of tenants a property can accommodate
    :type maximum_tenants: int
    :param want_shared_properties: Search for shared properties?
    :type want_shared_properties: bool
    :param want_student_properties: Search for student properties?
    :type want_student_properties: bool

    """
    return web.Response(status=200)


async def lettings_controller_get_advertised_between_dates(request: web.Request, short_name, branch_id, offset, count, range_start_date, range_end_date, area_id=None, rent_minimum=None, rent_maximum=None, maximum_tenants=None, want_shared_properties=None, want_student_properties=None) -> web.Response:
    """Search all properties available for rent given a range of search criteria and dates.

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param branch_id: The unique ID of the Branch
    :type branch_id: str
    :param offset: The index of the first item to return
    :type offset: int
    :param count: The maximum number of items to return (up to 1000 per request)
    :type count: int
    :param range_start_date: The date to search from
    :type range_start_date: str
    :param range_end_date: The date to search to
    :type range_end_date: str
    :param area_id: The unique ID of the Area
    :type area_id: str
    :param rent_minimum: The minimum advertised rent to search for
    :type rent_minimum: float
    :param rent_maximum: The maximum advertised rent to search for
    :type rent_maximum: float
    :param maximum_tenants: The maximum number of tenants a property can accommodate
    :type maximum_tenants: int
    :param want_shared_properties: Search for shared properties?
    :type want_shared_properties: bool
    :param want_student_properties: Search for student properties?
    :type want_student_properties: bool

    """
    range_start_date = util.deserialize_datetime(range_start_date)
    range_end_date = util.deserialize_datetime(range_end_date)
    return web.Response(status=200)


async def lettings_controller_get_tenancy_brochure(request: web.Request, short_name, tenancy_id) -> web.Response:
    """Downloads the brochure relating to the latest advertised rental of a property

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param tenancy_id: The unique ID of the tenancy
    :type tenancy_id: str

    """
    return web.Response(status=200)


async def v2_tier2_short_name_lettings_tenancies_get(request: web.Request, short_name, offset, count) -> web.Response:
    """A collection of all the company&#39;s tenancies

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param offset: The index of the first item to return
    :type offset: int
    :param count: The maximum number of items to return (up to 1000 per request)
    :type count: int

    """
    return web.Response(status=200)


async def v2_tier2_short_name_lettings_tenancies_tenancy_idget(request: web.Request, short_name, tenancy_id) -> web.Response:
    """Get a specific tenancy given its unique Object ID (OID)

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param tenancy_id: The unique ID of the Tenancy
    :type tenancy_id: str

    """
    return web.Response(status=200)
