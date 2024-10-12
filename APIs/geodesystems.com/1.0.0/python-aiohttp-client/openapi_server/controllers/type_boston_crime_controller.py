from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def search_boston_crime(request: web.Request, text=None, name=None, description=None, fromdate=None, todate=None, createdate_from=None, createdate_to=None, changedate_from=None, changedate_to=None, group=None, filesuffix=None, maxlatitude=None, minlongitude=None, minlatitude=None, maxlongitude=None, max=None, skip=None, search_db_boston_crime_offense=None, search_db_boston_crime_offense_code_group=None, search_db_boston_crime_offense_description=None, search_db_boston_crime_district=None, search_db_boston_crime_reporting_area=None, search_db_boston_crime_shooting=None, search_db_boston_crime_year=None, search_db_boston_crime_month=None, search_db_boston_crime_day_of_week=None, search_db_boston_crime_hour=None, search_db_boston_crime_street=None, search_db_boston_crime_location=None) -> web.Response:
    """Search API for &#39;Boston Crime&#39; entry type

    API to search for entries of type Boston Crime

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
    :param search_db_boston_crime_offense: Offense
    :type search_db_boston_crime_offense: str
    :param search_db_boston_crime_offense_code_group: Offense Code Group
    :type search_db_boston_crime_offense_code_group: str
    :param search_db_boston_crime_offense_description: Offense Description
    :type search_db_boston_crime_offense_description: str
    :param search_db_boston_crime_district: District
    :type search_db_boston_crime_district: str
    :param search_db_boston_crime_reporting_area: Reporting Area
    :type search_db_boston_crime_reporting_area: str
    :param search_db_boston_crime_shooting: Shooting
    :type search_db_boston_crime_shooting: str
    :param search_db_boston_crime_year: Year
    :type search_db_boston_crime_year: float
    :param search_db_boston_crime_month: Month
    :type search_db_boston_crime_month: float
    :param search_db_boston_crime_day_of_week: Day Of Week
    :type search_db_boston_crime_day_of_week: str
    :param search_db_boston_crime_hour: Hour
    :type search_db_boston_crime_hour: float
    :param search_db_boston_crime_street: Street
    :type search_db_boston_crime_street: str
    :param search_db_boston_crime_location: Location
    :type search_db_boston_crime_location: str

    """
    fromdate = util.deserialize_datetime(fromdate)
    todate = util.deserialize_datetime(todate)
    createdate_from = util.deserialize_datetime(createdate_from)
    createdate_to = util.deserialize_datetime(createdate_to)
    changedate_from = util.deserialize_datetime(changedate_from)
    changedate_to = util.deserialize_datetime(changedate_to)
    return web.Response(status=200)
