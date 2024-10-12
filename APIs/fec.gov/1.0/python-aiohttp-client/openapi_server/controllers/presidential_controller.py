from typing import List, Dict
from aiohttp import web

from openapi_server.models.presidential_by_candidate_page import PresidentialByCandidatePage
from openapi_server.models.presidential_by_size_page import PresidentialBySizePage
from openapi_server.models.presidential_by_state_page import PresidentialByStatePage
from openapi_server.models.presidential_coverage_page import PresidentialCoveragePage
from openapi_server.models.presidential_summary_page import PresidentialSummaryPage
from openapi_server import util


async def presidential_contributions_by_candidate_get(request: web.Request, api_key, sort_nulls_last=None, page=None, sort_null_only=None, sort_hide_null=None, per_page=None, election_year=None, contributor_state=None, sort=None) -> web.Response:
    """presidential_contributions_by_candidate_get

     Net receipts per candidate.  Filter with &#x60;contributor_state&#x3D;&#39;US&#39;&#x60; for national totals 

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param sort_nulls_last: Toggle that sorts null values last
    :type sort_nulls_last: bool
    :param page: For paginating through results, starting at page 1
    :type page: int
    :param sort_null_only: Toggle that filters out all rows having sort column that is non-null
    :type sort_null_only: bool
    :param sort_hide_null: Hide null values on sorted column(s).
    :type sort_hide_null: bool
    :param per_page: The number of results returned per page. Defaults to 20.
    :type per_page: int
    :param election_year: Year of election
    :type election_year: List[int]
    :param contributor_state: State of contributor
    :type contributor_state: List[str]
    :param sort: Provide a field to sort by. Use &#x60;-&#x60; for descending order. 
    :type sort: str

    """
    return web.Response(status=200)


async def presidential_contributions_by_size_get(request: web.Request, api_key, sort_nulls_last=None, page=None, sort_null_only=None, size=None, sort_hide_null=None, candidate_id=None, per_page=None, election_year=None, sort=None) -> web.Response:
    """presidential_contributions_by_size_get

     Contribution receipts by size per candidate.  Filter by candidate_id, election_year and/or size 

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param sort_nulls_last: Toggle that sorts null values last
    :type sort_nulls_last: bool
    :param page: For paginating through results, starting at page 1
    :type page: int
    :param sort_null_only: Toggle that filters out all rows having sort column that is non-null
    :type sort_null_only: bool
    :param size:  The total all contributions in the following ranges: &#x60;&#x60;&#x60;   -0    $200 and under   -200  $200.01 - $499.99   -500  $500 - $999.99   -1000 $1000 - $1999.99   -2000 $2000 + &#x60;&#x60;&#x60; Unitemized contributions are included in the &#x60;0&#x60; category. 
    :type size: List[int]
    :param sort_hide_null: Hide null values on sorted column(s).
    :type sort_hide_null: bool
    :param candidate_id:  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence.   -P00000001    All candidates   -P00000002    Democrasts   -P00000003    Republicans 
    :type candidate_id: List[str]
    :param per_page: The number of results returned per page. Defaults to 20.
    :type per_page: int
    :param election_year: Year of election
    :type election_year: List[int]
    :param sort: Provide a field to sort by. Use &#x60;-&#x60; for descending order. 
    :type sort: str

    """
    return web.Response(status=200)


async def presidential_contributions_by_state_get(request: web.Request, api_key, sort_nulls_last=None, page=None, sort_null_only=None, sort_hide_null=None, candidate_id=None, per_page=None, election_year=None, sort=None) -> web.Response:
    """presidential_contributions_by_state_get

     Contribution receipts by state per candidate.  Filter by candidate_id and/or election_year 

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param sort_nulls_last: Toggle that sorts null values last
    :type sort_nulls_last: bool
    :param page: For paginating through results, starting at page 1
    :type page: int
    :param sort_null_only: Toggle that filters out all rows having sort column that is non-null
    :type sort_null_only: bool
    :param sort_hide_null: Hide null values on sorted column(s).
    :type sort_hide_null: bool
    :param candidate_id:  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence.   -P00000001    All candidates   -P00000002    Democrasts   -P00000003    Republicans 
    :type candidate_id: List[str]
    :param per_page: The number of results returned per page. Defaults to 20.
    :type per_page: int
    :param election_year: Year of election
    :type election_year: List[int]
    :param sort: Provide a field to sort by. Use &#x60;-&#x60; for descending order. 
    :type sort: str

    """
    return web.Response(status=200)


async def presidential_coverage_end_date_get(request: web.Request, api_key, sort_nulls_last=None, page=None, sort_null_only=None, sort_hide_null=None, candidate_id=None, per_page=None, election_year=None, sort=None) -> web.Response:
    """presidential_coverage_end_date_get

     Coverage end date per candidate.  Filter by candidate_id and/or election_year 

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param sort_nulls_last: Toggle that sorts null values last
    :type sort_nulls_last: bool
    :param page: For paginating through results, starting at page 1
    :type page: int
    :param sort_null_only: Toggle that filters out all rows having sort column that is non-null
    :type sort_null_only: bool
    :param sort_hide_null: Hide null values on sorted column(s).
    :type sort_hide_null: bool
    :param candidate_id:  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence.   -P00000001    All candidates   -P00000002    Democrasts   -P00000003    Republicans 
    :type candidate_id: List[str]
    :param per_page: The number of results returned per page. Defaults to 20.
    :type per_page: int
    :param election_year: Year of election
    :type election_year: List[int]
    :param sort: Provide a field to sort by. Use &#x60;-&#x60; for descending order. 
    :type sort: str

    """
    return web.Response(status=200)


async def presidential_financial_summary_get(request: web.Request, api_key, sort_nulls_last=None, page=None, sort_null_only=None, sort_hide_null=None, candidate_id=None, per_page=None, election_year=None, sort=None) -> web.Response:
    """presidential_financial_summary_get

     Financial summary per candidate.  Filter by candidate_id and/or election_year 

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param sort_nulls_last: Toggle that sorts null values last
    :type sort_nulls_last: bool
    :param page: For paginating through results, starting at page 1
    :type page: int
    :param sort_null_only: Toggle that filters out all rows having sort column that is non-null
    :type sort_null_only: bool
    :param sort_hide_null: Hide null values on sorted column(s).
    :type sort_hide_null: bool
    :param candidate_id:  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence.   -P00000001    All candidates   -P00000002    Democrasts   -P00000003    Republicans 
    :type candidate_id: List[str]
    :param per_page: The number of results returned per page. Defaults to 20.
    :type per_page: int
    :param election_year: Year of election
    :type election_year: List[int]
    :param sort: Provide a field to sort by. Use &#x60;-&#x60; for descending order. 
    :type sort: str

    """
    return web.Response(status=200)
