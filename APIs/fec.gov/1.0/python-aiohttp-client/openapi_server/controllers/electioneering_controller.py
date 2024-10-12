from typing import List, Dict
from aiohttp import web

from openapi_server.models.ec_totals_by_candidate_page import ECTotalsByCandidatePage
from openapi_server.models.electioneering_by_candidate_page import ElectioneeringByCandidatePage
from openapi_server.models.electioneering_page import ElectioneeringPage
from openapi_server import util


async def electioneering_aggregates_get(request: web.Request, api_key, cycle=None, sort_nulls_last=None, page=None, committee_id=None, sort_null_only=None, sort_hide_null=None, candidate_id=None, per_page=None, sort=None) -> web.Response:
    """electioneering_aggregates_get

    Electioneering communications costs aggregates

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param cycle:  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
    :type cycle: List[int]
    :param sort_nulls_last: Toggle that sorts null values last
    :type sort_nulls_last: bool
    :param page: For paginating through results, starting at page 1
    :type page: int
    :param committee_id:  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits. 
    :type committee_id: List[str]
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


async def electioneering_by_candidate_get(request: web.Request, api_key, district=None, election_full=None, cycle=None, sort_null_only=None, page=None, state=None, sort_nulls_last=None, sort_hide_null=None, candidate_id=None, per_page=None, office=None, sort=None) -> web.Response:
    """electioneering_by_candidate_get

    Electioneering costs aggregated by candidate

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param district: Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00.
    :type district: str
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


async def electioneering_get(request: web.Request, api_key, min_date=None, description=None, sort_null_only=None, page=None, committee_id=None, report_year=None, last_index=None, sort_nulls_last=None, sort_hide_null=None, candidate_id=None, per_page=None, min_amount=None, max_date=None, max_amount=None, sort=None) -> web.Response:
    """electioneering_get

     An electioneering communication is any broadcast, cable or satellite communication that fulfills each of the following conditions:  _The communication refers to a clearly identified federal candidate._  _The communication is publicly distributed by a television station, radio station, cable television system or satellite system for a fee._  _The communication is distributed within 60 days prior to a general election or 30 days prior to a primary election to federal office._ 

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param min_date: Minimum disbursement date
    :type min_date: str
    :param description: 
    :type description: str
    :param sort_null_only: Toggle that filters out all rows having sort column that is non-null
    :type sort_null_only: bool
    :param page: For paginating through results, starting at page 1
    :type page: int
    :param committee_id:  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits. 
    :type committee_id: List[str]
    :param report_year:  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date. 
    :type report_year: List[int]
    :param last_index: Index of last result from previous page
    :type last_index: int
    :param sort_nulls_last: Toggle that sorts null values last
    :type sort_nulls_last: bool
    :param sort_hide_null: Hide null values on sorted column(s).
    :type sort_hide_null: bool
    :param candidate_id:  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence. 
    :type candidate_id: List[str]
    :param per_page: The number of results returned per page. Defaults to 20.
    :type per_page: int
    :param min_amount: Filter for all amounts greater than a value.
    :type min_amount: str
    :param max_date: Maximum disbursement date
    :type max_date: str
    :param max_amount: Filter for all amounts less than a value.
    :type max_amount: str
    :param sort: Provide a field to sort by. Use &#x60;-&#x60; for descending order. 
    :type sort: str

    """
    min_date = util.deserialize_date(min_date)
    max_date = util.deserialize_date(max_date)
    return web.Response(status=200)


async def electioneering_totals_by_candidate_get(request: web.Request, api_key, election_full=None, cycle=None, sort_nulls_last=None, page=None, sort_null_only=None, sort_hide_null=None, candidate_id=None, per_page=None, sort=None) -> web.Response:
    """electioneering_totals_by_candidate_get

     Total electioneering communications spent on candidates by cycle or candidate election year 

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
