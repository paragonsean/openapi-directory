from typing import List, Dict
from aiohttp import web

from openapi_server.models.rad_analyst_page import RadAnalystPage
from openapi_server.models.state_election_office_info_page import StateElectionOfficeInfoPage
from openapi_server import util


async def rad_analyst_get(request: web.Request, api_key, min_assignment_update_date=None, telephone_ext=None, analyst_id=None, sort_null_only=None, page=None, committee_id=None, sort_nulls_last=None, sort_hide_null=None, name=None, per_page=None, email=None, title=None, sort=None, max_assignment_update_date=None, analyst_short_id=None) -> web.Response:
    """rad_analyst_get

     Use this endpoint to look up the RAD Analyst for a committee.  The mission of the Reports Analysis Division (RAD) is to ensure that campaigns and political committees file timely and accurate reports that fully disclose their financial activities.  RAD is responsible for reviewing statements and financial reports filed by political committees participating in federal elections, providing assistance and guidance to the committees to properly file their reports, and for taking appropriate action to ensure compliance with the Federal Election Campaign Act (FECA). 

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param min_assignment_update_date: Filter results for assignment updates made after this date
    :type min_assignment_update_date: str
    :param telephone_ext: Telephone extension of RAD analyst
    :type telephone_ext: List[int]
    :param analyst_id: ID of RAD analyst
    :type analyst_id: List[int]
    :param sort_null_only: Toggle that filters out all rows having sort column that is non-null
    :type sort_null_only: bool
    :param page: For paginating through results, starting at page 1
    :type page: int
    :param committee_id:  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits. 
    :type committee_id: List[str]
    :param sort_nulls_last: Toggle that sorts null values last
    :type sort_nulls_last: bool
    :param sort_hide_null: Hide null values on sorted column(s).
    :type sort_hide_null: bool
    :param name: Name of RAD analyst
    :type name: List[str]
    :param per_page: The number of results returned per page. Defaults to 20.
    :type per_page: int
    :param email: Email of RAD analyst
    :type email: List[str]
    :param title: Title of RAD analyst
    :type title: List[str]
    :param sort: Provide a field to sort by. Use &#x60;-&#x60; for descending order. 
    :type sort: str
    :param max_assignment_update_date: Filter results for assignment updates made before this date
    :type max_assignment_update_date: str
    :param analyst_short_id: Short ID of RAD analyst
    :type analyst_short_id: List[int]

    """
    min_assignment_update_date = util.deserialize_date(min_assignment_update_date)
    max_assignment_update_date = util.deserialize_date(max_assignment_update_date)
    return web.Response(status=200)


async def state_election_office_get(request: web.Request, state, api_key, page=None, sort_hide_null=None, per_page=None, sort_null_only=None, sort=None, sort_nulls_last=None) -> web.Response:
    """state_election_office_get

     State laws and procedures govern elections for state or local offices as well as how candidates appear on election ballots. Contact the appropriate state election office for more information. 

    :param state:  Enter a state (Ex: AK, TX, VA etc..) to find the local election offices contact information.  
    :type state: str
    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param page: For paginating through results, starting at page 1
    :type page: int
    :param sort_hide_null: Hide null values on sorted column(s).
    :type sort_hide_null: bool
    :param per_page: The number of results returned per page. Defaults to 20.
    :type per_page: int
    :param sort_null_only: Toggle that filters out all rows having sort column that is non-null
    :type sort_null_only: bool
    :param sort: Provide a field to sort by. Use &#x60;-&#x60; for descending order. 
    :type sort: str
    :param sort_nulls_last: Toggle that sorts null values last
    :type sort_nulls_last: bool

    """
    return web.Response(status=200)
