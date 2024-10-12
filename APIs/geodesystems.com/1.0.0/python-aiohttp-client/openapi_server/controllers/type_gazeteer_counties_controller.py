from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def search_gazeteer_counties(request: web.Request, text=None, name=None, description=None, fromdate=None, todate=None, createdate_from=None, createdate_to=None, changedate_from=None, changedate_to=None, group=None, filesuffix=None, maxlatitude=None, minlongitude=None, minlatitude=None, maxlongitude=None, max=None, skip=None, search_db_gazeteer_counties_state_abbreviation=None, search_db_gazeteer_counties_state_fips=None, search_db_gazeteer_counties_county_fips=None, search_db_gazeteer_counties_full_county_fips=None, search_db_gazeteer_counties_county_name=None, search_db_gazeteer_counties_area_land=None, search_db_gazeteer_counties_area_water=None, search_db_gazeteer_counties_location=None) -> web.Response:
    """Search API for &#39;Census Gazeteer Counties&#39; entry type

    API to search for entries of type Census Gazeteer Counties

    :param text: Search text
    :type text: str
    :param name: Search name
    :type name: str
    :param description: Search description
    :type description: str
    :param fromdate: From date
    :type fromdate: str
    :param todate: To date
    :type todate: str
    :param createdate_from: Archive create date from
    :type createdate_from: str
    :param createdate_to: Archive create date to
    :type createdate_to: str
    :param changedate_from: Archive change date from
    :type changedate_from: str
    :param changedate_to: Archive change date to
    :type changedate_to: str
    :param group: Parent entry
    :type group: str
    :param filesuffix: File suffix
    :type filesuffix: str
    :param maxlatitude: Northern bounds of search
    :type maxlatitude: float
    :param minlongitude: Western bounds of search
    :type minlongitude: float
    :param minlatitude: Southern bounds of search
    :type minlatitude: float
    :param maxlongitude: Eastern bounds of search
    :type maxlongitude: float
    :param max: Max number of results
    :type max: int
    :param skip: Number to skip
    :type skip: int
    :param search_db_gazeteer_counties_state_abbreviation: State Abbreviation
    :type search_db_gazeteer_counties_state_abbreviation: str
    :param search_db_gazeteer_counties_state_fips: State Fips
    :type search_db_gazeteer_counties_state_fips: str
    :param search_db_gazeteer_counties_county_fips: County Fips
    :type search_db_gazeteer_counties_county_fips: str
    :param search_db_gazeteer_counties_full_county_fips: Full County Fips
    :type search_db_gazeteer_counties_full_county_fips: str
    :param search_db_gazeteer_counties_county_name: County Name
    :type search_db_gazeteer_counties_county_name: str
    :param search_db_gazeteer_counties_area_land: Area Land
    :type search_db_gazeteer_counties_area_land: float
    :param search_db_gazeteer_counties_area_water: Area Water
    :type search_db_gazeteer_counties_area_water: float
    :param search_db_gazeteer_counties_location: Location
    :type search_db_gazeteer_counties_location: str

    """
    fromdate = util.deserialize_datetime(fromdate)
    todate = util.deserialize_datetime(todate)
    createdate_from = util.deserialize_datetime(createdate_from)
    createdate_to = util.deserialize_datetime(createdate_to)
    changedate_from = util.deserialize_datetime(changedate_from)
    changedate_to = util.deserialize_datetime(changedate_to)
    return web.Response(status=200)
