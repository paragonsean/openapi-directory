from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def search_boulder_county_voter_details(request: web.Request, text=None, name=None, description=None, fromdate=None, todate=None, createdate_from=None, createdate_to=None, changedate_from=None, changedate_to=None, group=None, filesuffix=None, maxlatitude=None, minlongitude=None, minlatitude=None, maxlongitude=None, max=None, skip=None, search_db_boulder_county_voter_details_first_name=None, search_db_boulder_county_voter_details_last_name=None, search_db_boulder_county_voter_details_registration_date=None, search_db_boulder_county_voter_details_last_updated_date=None, search_db_boulder_county_voter_details_residential_address=None, search_db_boulder_county_voter_details_residential_city=None, search_db_boulder_county_voter_details_mailing_zip_code=None, search_db_boulder_county_voter_details_voter_status=None, search_db_boulder_county_voter_details_party=None, search_db_boulder_county_voter_details_gender=None, search_db_boulder_county_voter_details_birth_year=None, search_db_boulder_county_voter_details_precinct_code=None, search_db_boulder_county_voter_details_congressional=None, search_db_boulder_county_voter_details_state_senate=None, search_db_boulder_county_voter_details_state_house=None, search_db_boulder_county_voter_details_municipality=None, search_db_boulder_county_voter_details_city_ward_district=None, search_db_boulder_county_voter_details_school_district=None, search_db_boulder_county_voter_details_location=None) -> web.Response:
    """Search API for &#39;Boulder County Voter Details&#39; entry type

    API to search for entries of type Boulder County Voter Details

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
    :param search_db_boulder_county_voter_details_first_name: First Name
    :type search_db_boulder_county_voter_details_first_name: str
    :param search_db_boulder_county_voter_details_last_name: Last Name
    :type search_db_boulder_county_voter_details_last_name: str
    :param search_db_boulder_county_voter_details_registration_date: Registration Date
    :type search_db_boulder_county_voter_details_registration_date: str
    :param search_db_boulder_county_voter_details_last_updated_date: Last Updated Date
    :type search_db_boulder_county_voter_details_last_updated_date: str
    :param search_db_boulder_county_voter_details_residential_address: Residential Address
    :type search_db_boulder_county_voter_details_residential_address: str
    :param search_db_boulder_county_voter_details_residential_city: Residential City
    :type search_db_boulder_county_voter_details_residential_city: str
    :param search_db_boulder_county_voter_details_mailing_zip_code: Mailing Zip Code
    :type search_db_boulder_county_voter_details_mailing_zip_code: str
    :param search_db_boulder_county_voter_details_voter_status: Voter Status
    :type search_db_boulder_county_voter_details_voter_status: str
    :param search_db_boulder_county_voter_details_party: Party
    :type search_db_boulder_county_voter_details_party: str
    :param search_db_boulder_county_voter_details_gender: Gender
    :type search_db_boulder_county_voter_details_gender: str
    :param search_db_boulder_county_voter_details_birth_year: Birth Year
    :type search_db_boulder_county_voter_details_birth_year: int
    :param search_db_boulder_county_voter_details_precinct_code: Precinct Code
    :type search_db_boulder_county_voter_details_precinct_code: str
    :param search_db_boulder_county_voter_details_congressional: Congressional
    :type search_db_boulder_county_voter_details_congressional: str
    :param search_db_boulder_county_voter_details_state_senate: State Senate
    :type search_db_boulder_county_voter_details_state_senate: str
    :param search_db_boulder_county_voter_details_state_house: State House
    :type search_db_boulder_county_voter_details_state_house: str
    :param search_db_boulder_county_voter_details_municipality: Municipality
    :type search_db_boulder_county_voter_details_municipality: str
    :param search_db_boulder_county_voter_details_city_ward_district: City Ward/district
    :type search_db_boulder_county_voter_details_city_ward_district: str
    :param search_db_boulder_county_voter_details_school_district: School District
    :type search_db_boulder_county_voter_details_school_district: str
    :param search_db_boulder_county_voter_details_location: Location
    :type search_db_boulder_county_voter_details_location: str

    """
    fromdate = util.deserialize_datetime(fromdate)
    todate = util.deserialize_datetime(todate)
    createdate_from = util.deserialize_datetime(createdate_from)
    createdate_to = util.deserialize_datetime(createdate_to)
    changedate_from = util.deserialize_datetime(changedate_from)
    changedate_to = util.deserialize_datetime(changedate_to)
    return web.Response(status=200)
