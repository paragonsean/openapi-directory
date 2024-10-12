from typing import List, Dict
from aiohttp import web

from openapi_server.models.cc_totals_by_candidate_page import CCTotalsByCandidatePage
from openapi_server.models.communication_cost_by_candidate_page import CommunicationCostByCandidatePage
from openapi_server.models.communication_cost_page import CommunicationCostPage
from openapi_server import util


async def communication_costs_aggregates_get(request: web.Request, api_key, support_oppose_indicator=None, cycle=None, sort_null_only=None, page=None, committee_id=None, sort_nulls_last=None, sort_hide_null=None, candidate_id=None, per_page=None, sort=None) -> web.Response:
    """communication_costs_aggregates_get

    Communication cost aggregated by candidate ID and committee ID.

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param support_oppose_indicator: Support or opposition
    :type support_oppose_indicator: str
    :param cycle:  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
    :type cycle: List[int]
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
    :param candidate_id:  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence. 
    :type candidate_id: List[str]
    :param per_page: The number of results returned per page. Defaults to 20.
    :type per_page: int
    :param sort: Provide a field to sort by. Use &#x60;-&#x60; for descending order. 
    :type sort: str

    """
    return web.Response(status=200)


async def communication_costs_by_candidate_get(request: web.Request, api_key, district=None, support_oppose=None, election_full=None, cycle=None, sort_null_only=None, page=None, state=None, sort_nulls_last=None, sort_hide_null=None, candidate_id=None, per_page=None, office=None, sort=None) -> web.Response:
    """communication_costs_by_candidate_get

    Communication cost aggregated by candidate ID and committee ID.

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param district: Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00.
    :type district: str
    :param support_oppose: Support or opposition
    :type support_oppose: str
    :param election_full: &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle.
    :type election_full: bool
    :param cycle:  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
    :type cycle: List[int]
    :param sort_null_only: Toggle that filters out all rows having sort column that is non-null
    :type sort_null_only: bool
    :param page: For paginating through results, starting at page 1
    :type page: int
    :param state: US state or territory where a candidate runs for office
    :type state: str
    :param sort_nulls_last: Toggle that sorts null values last
    :type sort_nulls_last: bool
    :param sort_hide_null: Hide null values on sorted column(s).
    :type sort_hide_null: bool
    :param candidate_id:  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence. 
    :type candidate_id: List[str]
    :param per_page: The number of results returned per page. Defaults to 20.
    :type per_page: int
    :param office: Federal office candidate runs for: H, S or P
    :type office: str
    :param sort: Provide a field to sort by. Use &#x60;-&#x60; for descending order. 
    :type sort: str

    """
    return web.Response(status=200)


async def communication_costs_get(request: web.Request, api_key, min_date=None, support_oppose_indicator=None, max_image_number=None, min_image_number=None, sort_null_only=None, sort_hide_null=None, min_amount=None, per_page=None, candidate_id=None, line_number=None, sort=None, sort_nulls_last=None, page=None, committee_id=None, image_number=None, max_date=None, max_amount=None) -> web.Response:
    """communication_costs_get

     52 U.S.C. 30118 allows \&quot;communications by a corporation to its stockholders and executive or administrative personnel and their families or by a labor organization to its members and their families on any subject,\&quot; including the express advocacy of the election or defeat of any Federal candidate.  The costs of such communications must be reported to the Federal Election Commission under certain circumstances. 

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param min_date: Minimum date
    :type min_date: str
    :param support_oppose_indicator: Support or opposition
    :type support_oppose_indicator: List[str]
    :param max_image_number: Maxium image number of the page where the schedule item is reported
    :type max_image_number: str
    :param min_image_number: Minium image number of the page where the schedule item is reported
    :type min_image_number: str
    :param sort_null_only: Toggle that filters out all rows having sort column that is non-null
    :type sort_null_only: bool
    :param sort_hide_null: Hide null values on sorted column(s).
    :type sort_hide_null: bool
    :param min_amount: Filter for all amounts greater than a value.
    :type min_amount: str
    :param per_page: The number of results returned per page. Defaults to 20.
    :type per_page: int
    :param candidate_id:  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence. 
    :type candidate_id: List[str]
    :param line_number: Filter for form and line number using the following format: &#x60;FORM-LINENUMBER&#x60;.  For example an argument such as &#x60;F3X-16&#x60; would filter down to all entries from form &#x60;F3X&#x60; line number &#x60;16&#x60;.
    :type line_number: str
    :param sort: Provide a field to sort by. Use &#x60;-&#x60; for descending order. 
    :type sort: str
    :param sort_nulls_last: Toggle that sorts null values last
    :type sort_nulls_last: bool
    :param page: For paginating through results, starting at page 1
    :type page: int
    :param committee_id:  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits. 
    :type committee_id: List[str]
    :param image_number:  An unique identifier for each page where the electronic or paper filing is reported. 
    :type image_number: List[str]
    :param max_date: Maximum date
    :type max_date: str
    :param max_amount: Filter for all amounts less than a value.
    :type max_amount: str

    """
    min_date = util.deserialize_date(min_date)
    max_date = util.deserialize_date(max_date)
    return web.Response(status=200)


async def communication_costs_totals_by_candidate_get(request: web.Request, api_key, election_full=None, cycle=None, sort_nulls_last=None, page=None, sort_null_only=None, sort_hide_null=None, candidate_id=None, per_page=None, sort=None) -> web.Response:
    """communication_costs_totals_by_candidate_get

     Total communications costs aggregated across committees on supported or opposed candidates by cycle or candidate election year. 

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param election_full: &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle.
    :type election_full: bool
    :param cycle:  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
    :type cycle: List[int]
    :param sort_nulls_last: Toggle that sorts null values last
    :type sort_nulls_last: bool
    :param page: For paginating through results, starting at page 1
    :type page: int
    :param sort_null_only: Toggle that filters out all rows having sort column that is non-null
    :type sort_null_only: bool
    :param sort_hide_null: Hide null values on sorted column(s).
    :type sort_hide_null: bool
    :param candidate_id:  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence. 
    :type candidate_id: List[str]
    :param per_page: The number of results returned per page. Defaults to 20.
    :type per_page: int
    :param sort: Provide a field to sort by. Use &#x60;-&#x60; for descending order. 
    :type sort: str

    """
    return web.Response(status=200)
