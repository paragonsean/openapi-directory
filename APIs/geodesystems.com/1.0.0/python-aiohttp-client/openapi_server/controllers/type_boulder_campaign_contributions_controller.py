from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def search_boulder_campaign_contributions(request: web.Request, text=None, name=None, description=None, fromdate=None, todate=None, createdate_from=None, createdate_to=None, changedate_from=None, changedate_to=None, group=None, filesuffix=None, maxlatitude=None, minlongitude=None, minlatitude=None, maxlongitude=None, max=None, skip=None, search_db_boulder_campaign_contributions_committee=None, search_db_boulder_campaign_contributions_type=None, search_db_boulder_campaign_contributions_committee_num=None, search_db_boulder_campaign_contributions_candidate=None, search_db_boulder_campaign_contributions_filing_date=None, search_db_boulder_campaign_contributions_amended_date=None, search_db_boulder_campaign_contributions_official_filing=None, search_db_boulder_campaign_contributions_transaction_date=None, search_db_boulder_campaign_contributions_last_name=None, search_db_boulder_campaign_contributions_first_name=None, search_db_boulder_campaign_contributions_street=None, search_db_boulder_campaign_contributions_city=None, search_db_boulder_campaign_contributions_state=None, search_db_boulder_campaign_contributions_zip=None, search_db_boulder_campaign_contributions_contribution=None, search_db_boulder_campaign_contributions_contribution_type=None, search_db_boulder_campaign_contributions_anonymous=None, search_db_boulder_campaign_contributions_from_candidate=None, search_db_boulder_campaign_contributions_match=None) -> web.Response:
    """Search API for &#39;Boulder Campaign Contributions&#39; entry type

    API to search for entries of type Boulder Campaign Contributions

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
    :param search_db_boulder_campaign_contributions_committee: Committee
    :type search_db_boulder_campaign_contributions_committee: str
    :param search_db_boulder_campaign_contributions_type: Type
    :type search_db_boulder_campaign_contributions_type: str
    :param search_db_boulder_campaign_contributions_committee_num: Committee Num
    :type search_db_boulder_campaign_contributions_committee_num: str
    :param search_db_boulder_campaign_contributions_candidate: Candidate
    :type search_db_boulder_campaign_contributions_candidate: str
    :param search_db_boulder_campaign_contributions_filing_date: Filing Date
    :type search_db_boulder_campaign_contributions_filing_date: str
    :param search_db_boulder_campaign_contributions_amended_date: Amended Date
    :type search_db_boulder_campaign_contributions_amended_date: str
    :param search_db_boulder_campaign_contributions_official_filing: Official Filing
    :type search_db_boulder_campaign_contributions_official_filing: str
    :param search_db_boulder_campaign_contributions_transaction_date: Transaction Date
    :type search_db_boulder_campaign_contributions_transaction_date: str
    :param search_db_boulder_campaign_contributions_last_name: Last Name
    :type search_db_boulder_campaign_contributions_last_name: str
    :param search_db_boulder_campaign_contributions_first_name: First Name
    :type search_db_boulder_campaign_contributions_first_name: str
    :param search_db_boulder_campaign_contributions_street: Street
    :type search_db_boulder_campaign_contributions_street: str
    :param search_db_boulder_campaign_contributions_city: City
    :type search_db_boulder_campaign_contributions_city: str
    :param search_db_boulder_campaign_contributions_state: State
    :type search_db_boulder_campaign_contributions_state: str
    :param search_db_boulder_campaign_contributions_zip: Zip
    :type search_db_boulder_campaign_contributions_zip: str
    :param search_db_boulder_campaign_contributions_contribution: Contribution
    :type search_db_boulder_campaign_contributions_contribution: float
    :param search_db_boulder_campaign_contributions_contribution_type: Contribution Type
    :type search_db_boulder_campaign_contributions_contribution_type: str
    :param search_db_boulder_campaign_contributions_anonymous: Anonymous
    :type search_db_boulder_campaign_contributions_anonymous: str
    :param search_db_boulder_campaign_contributions_from_candidate: From Candidate
    :type search_db_boulder_campaign_contributions_from_candidate: str
    :param search_db_boulder_campaign_contributions_match: Match
    :type search_db_boulder_campaign_contributions_match: float

    """
    fromdate = util.deserialize_datetime(fromdate)
    todate = util.deserialize_datetime(todate)
    createdate_from = util.deserialize_datetime(createdate_from)
    createdate_to = util.deserialize_datetime(createdate_to)
    changedate_from = util.deserialize_datetime(changedate_from)
    changedate_to = util.deserialize_datetime(changedate_to)
    return web.Response(status=200)
