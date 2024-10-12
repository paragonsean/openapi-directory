from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def search_boulder2017_election_contributions(request: web.Request, text=None, name=None, description=None, fromdate=None, todate=None, createdate_from=None, createdate_to=None, changedate_from=None, changedate_to=None, group=None, filesuffix=None, maxlatitude=None, minlongitude=None, minlatitude=None, maxlongitude=None, max=None, skip=None, search_db_boulder_2017_election_contributions_committee=None, search_db_boulder_2017_election_contributions_last_name=None, search_db_boulder_2017_election_contributions_first_name=None, search_db_boulder_2017_election_contributions_street=None, search_db_boulder_2017_election_contributions_city=None, search_db_boulder_2017_election_contributions_state=None, search_db_boulder_2017_election_contributions_zip=None, search_db_boulder_2017_election_contributions_contribution_type=None, search_db_boulder_2017_election_contributions_from_candidate=None, search_db_boulder_2017_election_contributions_date=None, search_db_boulder_2017_election_contributions_amount=None, search_db_boulder_2017_election_contributions_match_amount=None, search_db_boulder_2017_election_contributions_ytd_amount=None, search_db_boulder_2017_election_contributions_location=None) -> web.Response:
    """Search API for &#39;Boulder 2017 Election Contributions&#39; entry type

    API to search for entries of type Boulder 2017 Election Contributions

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
    :param search_db_boulder_2017_election_contributions_committee: Committee
    :type search_db_boulder_2017_election_contributions_committee: str
    :param search_db_boulder_2017_election_contributions_last_name: Last Name
    :type search_db_boulder_2017_election_contributions_last_name: str
    :param search_db_boulder_2017_election_contributions_first_name: First Name
    :type search_db_boulder_2017_election_contributions_first_name: str
    :param search_db_boulder_2017_election_contributions_street: Street
    :type search_db_boulder_2017_election_contributions_street: str
    :param search_db_boulder_2017_election_contributions_city: City
    :type search_db_boulder_2017_election_contributions_city: str
    :param search_db_boulder_2017_election_contributions_state: State
    :type search_db_boulder_2017_election_contributions_state: str
    :param search_db_boulder_2017_election_contributions_zip: Zip
    :type search_db_boulder_2017_election_contributions_zip: str
    :param search_db_boulder_2017_election_contributions_contribution_type: Contribution Type
    :type search_db_boulder_2017_election_contributions_contribution_type: str
    :param search_db_boulder_2017_election_contributions_from_candidate: From Candidate
    :type search_db_boulder_2017_election_contributions_from_candidate: str
    :param search_db_boulder_2017_election_contributions_date: Date
    :type search_db_boulder_2017_election_contributions_date: str
    :param search_db_boulder_2017_election_contributions_amount: Amount
    :type search_db_boulder_2017_election_contributions_amount: float
    :param search_db_boulder_2017_election_contributions_match_amount: Match Amount
    :type search_db_boulder_2017_election_contributions_match_amount: float
    :param search_db_boulder_2017_election_contributions_ytd_amount: Ytd Amount
    :type search_db_boulder_2017_election_contributions_ytd_amount: float
    :param search_db_boulder_2017_election_contributions_location: Location
    :type search_db_boulder_2017_election_contributions_location: str

    """
    fromdate = util.deserialize_datetime(fromdate)
    todate = util.deserialize_datetime(todate)
    createdate_from = util.deserialize_datetime(createdate_from)
    createdate_to = util.deserialize_datetime(createdate_to)
    changedate_from = util.deserialize_datetime(changedate_from)
    changedate_to = util.deserialize_datetime(changedate_to)
    return web.Response(status=200)
